package com.oneoffcoder.tello;

import com.oneoffcoder.tello.finder.SwarmFinder.SwarmFinderListener;
import com.oneoffcoder.tello.util.TelloUtil;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

public class Swarm implements SwarmFinderListener {

  public interface SwarmListener {
    void responseReceived(InetAddress address, String response);
  }

  final private int port;
  final private List<String> commands;
  final private AtomicInteger nDronesReady;
  private List<Drone> drones;
  private DatagramSocket socket;
  private AtomicBoolean stopThread;
  private Thread receiveThread;

  public Swarm(int port, List<String> commands) {
    this.port = port;
    this.commands = commands;
    this.nDronesReady = new AtomicInteger(0);
  }

  public void init(Map<Integer, String> id2sn, String ipPrefix)
      throws SocketException, UnknownHostException {
    this.socket = new DatagramSocket(this.port, InetAddress.getByName("0.0.0.0"));
    this.socket.setBroadcast(true);

    (new SwarmFinder(id2sn, this.socket, ipPrefix, this)).start();
  }

  @Override
  public void finishedFindingDrones(List<Drone> drones) {
    this.drones = drones;

    this.stopThread = new AtomicBoolean(false);

    this.receiveThread = new Thread(new Runnable() {
      @Override
      public void run() {
        while (true) {
          if (Swarm.this.stopThread.get()) {
            System.out.println("THREAD | receive | stopped");
            break;
          }

          try {
            byte[] data = new byte[1024];
            DatagramPacket packet = new DatagramPacket(data, data.length);

            socket.receive(packet);

            String response = (new String(Arrays.copyOf(data, packet.getLength()),
                StandardCharsets.UTF_8)).trim();
            InetAddress address = packet.getAddress();

            System.out.println("RESPONSE | " + address + " | " + response);
            Swarm.this.drones.forEach(d -> d.responseReceived(address, response));
          } catch (IOException e) {
            e.printStackTrace();
          }
        }
      }
    });
    this.receiveThread.setDaemon(true);
    this.receiveThread.start();

    this.drones.forEach(d -> d.init(this.socket, this));

    final int nDrones = this.drones.size();
    while (true) {
      if (this.nDronesReady.get() != nDrones) {
        try {
          Thread.sleep(500);
        } catch (InterruptedException e) {
          // swallow
        }
      } else {
        System.out.println("SWARM | " + nDrones + " initialized");
        break;
      }
    }

    this.start();
  }

  public void deinit() {
    this.drones.forEach(d -> d.deinit());

    this.stopThread.set(true);

    try {
      this.socket.close();
      System.out.println("SWARM DEINIT | socket_close | success");
    } catch (Exception e) {
      System.out.println("SWARM DEINIT | socket_close | " + e);
    }
  }

  private void start() {
    for (String command : this.commands) {
      if (command.indexOf(">") != -1) {
        this.handleCommand(command);
      } else if (command.indexOf("sync") != -1) {
        this.handleSync(command);
      }
    }
  }

  private void handleCommand(String command) {
    this.drones.forEach(d -> d.addCommand(command));
  }

  private void handleSync(String command) {
    String[] tokens = Arrays.stream(command.split(" "))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    float timeOut = Float.parseFloat(tokens[1]);
    sync(timeOut);
  }

  private void waitAndBlock() {
    sync(-1.0f);
  }

  private boolean allQueuesEmpty() {
    long n = this.drones.stream()
        .map(d -> d.getQueue())
        .filter(q -> !q.isEmpty())
        .count();
    return (n > 0) ? false : true;
  }

  private boolean allResponsesReceived() {
    long n = this.drones.stream()
        .map(d -> d.getLogItems())
        .filter(list -> list.size() > 0)
        .map(list -> list.get(list.size() - 1))
        .filter(logItem -> !logItem.hasResponse())
        .count();
    return (n > 0) ? false : true;
  }

  private void sync(float timeOut) {
    Date start = new Date();

    while (!allQueuesEmpty()) {
      if (timeOut < 0.0) {
        try {
          Thread.sleep(500);
        } catch (InterruptedException e) {
          // swallow
        }
      } else {
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);
        if (diff > timeOut) {
          System.out.println(
              "SYNC | FAILED | queues_not_empty | waited " + diff + " | exceeded " + timeOut);
          break;
        }
      }
    }

    while (!allResponsesReceived()) {
      if (timeOut < 0.0) {
        try {
          Thread.sleep(500);
        } catch (InterruptedException e) {
          // swallow
        }
      } else {
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);
        if (diff > timeOut) {
          System.out.println(
              "SYNC | FAILED | responses_not_received | waited " + diff + " | exceeded " + timeOut);
          break;
        }
      }
    }
  }

  public static void main(String[] args) {
    Map<Integer, String> id2sn = new HashMap<Integer, String>() {{
      put(1, "0TQZGANED0021X");
      put(2, "0TQZGANED0020C");
      put(3, "0TQZGARED000KN");
      put(4, "0TQZGANED0023H");
    }};

    List<String> commands = Arrays.asList(
        "* > battery?"
    );

    Swarm swarm = new Swarm(8889, commands);

    try {
      swarm.init(id2sn, "192.168.3");
      swarm.waitAndBlock();
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      swarm.deinit();
    }
  }
}
