package com.oneoffcoder.tello.finder;

import com.oneoffcoder.tello.io.CommandFile;
import com.oneoffcoder.tello.swarm.Drone;
import com.oneoffcoder.tello.swarm.MessageItem;
import com.oneoffcoder.tello.swarm.ReceiveItem;
import com.oneoffcoder.tello.swarm.SendItem;
import com.oneoffcoder.tello.swarm.SwarmManager;
import com.oneoffcoder.tello.swarm.SwarmManager.SwarmManagerListener;
import com.oneoffcoder.tello.util.AddressUtil;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.SocketException;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class SwarmFinder extends Thread implements SwarmManagerListener {

  public interface SwarmFinderListener {

    void finishedFindingDrones(List<Drone> drones);
  }

  private final SwarmManager manager;
  private final List<InetSocketAddress> addresses;
  private final SwarmFinderListener listener;
  private final Map<Integer, String> id2sn;
  private final Map<String, InetSocketAddress> sn2ip;

  private SwarmFinder(Builder b) throws SocketException {
    this.manager = SwarmManager.newInstance(b.socket, this);
    this.listener = b.listener;
    this.id2sn = b.id2sn;
    this.sn2ip = Collections.synchronizedMap(new HashMap<>());
    this.addresses = AddressUtil.getAddresses(b.ipPrefix);
  }

  @Override
  public void run() {
    this.manager.start();
    this.addresses.stream()
        .map(a -> new SendItem(a, "command"))
        .forEach(command -> this.manager.send(command));

    while (!this.shouldStop()) {
      try {
        Thread.sleep(500);
      } catch (Exception e) {
        // swallow
      }
    }

    this.manager.stopNow();

    if (null != this.listener) {
      List<Drone> drones = this.id2sn.entrySet().stream()
          .map(e -> new Drone(e.getKey(), e.getValue(), this.sn2ip.get(e.getValue())))
          .collect(Collectors.toList());
      this.listener.finishedFindingDrones(drones);
    }
  }

  @Override
  public void processMessage(MessageItem message) {
    if (message instanceof ReceiveItem) {
      ReceiveItem receiveItem = (ReceiveItem) message;
      if (receiveItem.getMessage().equalsIgnoreCase("ok")) {
        SendItem command = new SendItem(receiveItem.getAddress(), "sn?");
        this.manager.send(command);
      } else {
        this.sn2ip.put(receiveItem.getMessage(), receiveItem.getAddress());
      }
    }
  }

  private boolean shouldStop() {
    return (this.sn2ip.size() == this.id2sn.size());
  }


  public static Builder newSwarmFinder() {
    return new Builder();
  }

  public static final class Builder {

    private DatagramSocket socket;
    private String ipPrefix;
    private SwarmFinderListener listener;
    private Map<Integer, String> id2sn;

    private Builder() {
    }

    public SwarmFinder build() throws SocketException {
      return new SwarmFinder(this);
    }

    public Builder socket(DatagramSocket socket) {
      this.socket = socket;
      return this;
    }

    public Builder ipPrefix(String ipPrefix) {
      this.ipPrefix = ipPrefix;
      return this;
    }

    public Builder listener(SwarmFinderListener listener) {
      this.listener = listener;
      return this;
    }

    public Builder id2sn(Map<Integer, String> id2sn) {
      this.id2sn = id2sn;
      return this;
    }
  }

  public static void main(String[] args) throws Exception {
    CommandFile file = new CommandFile(Paths.get("cmds-01.txt"));

    DatagramSocket socket = new DatagramSocket(8889, InetAddress.getByName("0.0.0.0"));
    SwarmFinder finder = SwarmFinder.newSwarmFinder()
        .socket(socket)
        .ipPrefix(file.getIpPrefix())
        .id2sn(file.getId2sn())
        .listener(drones -> {
          drones.forEach(System.out::println);
          socket.close();
        })
        .build();
    finder.start();
  }
}
