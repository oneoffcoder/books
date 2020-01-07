package com.oneoffcoder.tello;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class SwarmFinder {

  final private int nDrones;
  final private DatagramSocket socket;
  final private InetSocketAddress[] addresses;
  final private Map<Integer, String> id2sn;
  final private Map<InetAddress, String> ip2sn;
  final private Thread receiveThread;
  final private SwarmFinderListener listener;

  public SwarmFinder(Map<Integer, String> id2sn, DatagramSocket socket, String ipPrefix,
      SwarmFinderListener listener) {
    this.id2sn = id2sn;
    this.ip2sn = Collections.synchronizedMap(new HashMap<>());
    this.nDrones = id2sn.size();
    this.socket = socket;
    this.addresses = IntStream.range(2, 254)
        .mapToObj(i -> String.valueOf(i))
        .map(s -> ipPrefix + "." + s)
        .map(s -> new InetSocketAddress(s, 8889))
        .toArray(InetSocketAddress[]::new);
    this.listener = listener;

    this.receiveThread = new Thread(new Runnable() {
      @Override
      public void run() {
        while (!SwarmFinder.this.shouldStopThread()) {
          try {
            byte[] data = new byte[1024];
            DatagramPacket packet = new DatagramPacket(data, data.length);

            SwarmFinder.this.socket.receive(packet);

            String response = (new String(Arrays.copyOf(data, packet.getLength()),
                StandardCharsets.UTF_8)).trim();
            InetAddress address = packet.getAddress();

            System.out.println("RESPONSE | " + address + " | " + response);

            if (response.equalsIgnoreCase("ok")) {
              SwarmFinder.this.ip2sn.put(address, null);
              SwarmFinder.this.sendCommand("sn?", new InetSocketAddress(address, 8889));
            } else {
              SwarmFinder.this.ip2sn.put(address, response);
            }
          } catch (IOException e) {
            // swallow
          }

          try {
            Thread.sleep(200);
          } catch (InterruptedException e) {
            // swallow
          }
        }

        if (SwarmFinder.this.listener != null) {
          Map<String, InetAddress> sn2ip = SwarmFinder.this.ip2sn.entrySet()
              .stream()
              .collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey));
          List<Drone> drones = SwarmFinder.this.id2sn.entrySet()
              .stream()
              .map(e -> {
                Integer id = e.getKey();
                String sn = e.getValue();
                InetSocketAddress address = new InetSocketAddress(sn2ip.get(sn), 8889);

                return new Drone(id, sn, address);
              })
              .collect(Collectors.toList());

          SwarmFinder.this.listener.finishedFindingDrones(drones);
        }
      }
    });
    this.receiveThread.setDaemon(true);
  }

  public void start() {
    this.receiveThread.start();
    Arrays.stream(this.addresses).forEach(a -> sendCommand("command", a));
  }

  private boolean shouldStopThread() {
    if (this.ip2sn.size() == this.nDrones) {
      int n = (int) this.ip2sn.values().stream()
          .filter(s -> s != null)
          .count();
      if (n == this.nDrones) {
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }

  private void sendCommand(String command, InetSocketAddress address) {
    try {
      System.out.println("SEND | command | " + command);
      byte[] data = command.getBytes();
      DatagramPacket packet = new DatagramPacket(data, data.length, address);
      this.socket.send(packet);
    } catch (IOException e) {
      System.err.println("SEND | command | " + command + " | " + e);
    }
  }

  public static void main(String[] args) throws UnknownHostException, SocketException {
    try (DatagramSocket socket = new DatagramSocket(8889, InetAddress.getByName("0.0.0.0"))) {
      socket.setBroadcast(true);

      Map<Integer, String> id2sn = new HashMap<Integer, String>() {{
        put(1, "0TQZGANED0021X");
        put(2, "0TQZGANED0020C");
        put(3, "0TQZGARED000KN");
        put(4, "0TQZGANED0023H");
      }};
      String ipPrefix = "192.168.3";
      SwarmFinderListener listener = new SwarmFinderListener() {

        @Override
        public void finishedFindingDrones(List<Drone> drones) {
          drones.stream().forEach(System.out::println);
        }
      };

      SwarmFinder finder = new SwarmFinder(id2sn, socket, ipPrefix, listener);
      finder.start();
    }
  }

}
