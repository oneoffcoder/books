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
import java.util.Date;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

public class Swarm implements DroneListener {

  final private AtomicInteger nDronesReady;
  final private int port;
  final private List<Drone> drones;
  private DatagramSocket socket;
  private AtomicBoolean stopThread;
  private Thread receiveThread;

  public Swarm(int port, List<Drone> drones) {
    this.port = port;
    this.drones = drones;
    this.nDronesReady = new AtomicInteger();
  }

  public void init() throws SocketException, InterruptedException, UnknownHostException {
    this.socket = new DatagramSocket(this.port, InetAddress.getByName("0.0.0.0"));
    this.socket.setBroadcast(true);

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

            String response = (new String(Arrays.copyOf(data, packet.getLength()), StandardCharsets.UTF_8)).trim();
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
        Thread.sleep(500);
      } else {
        System.out.println("SWARM | " + nDrones + " initialized");
        break;
      }
    }
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

  public void start(List<String> commands) throws InterruptedException {
    for (String command : commands) {
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

  private void handleSync(String command) throws InterruptedException {
    String[] tokens = Arrays.stream(command.split(" "))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    float timeOut = Float.parseFloat(tokens[1]);
    sync(timeOut);
  }

  private void waitAndBlock() throws InterruptedException {
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

  private void sync(float timeOut) throws InterruptedException {
    Date start = new Date();

    while (!allQueuesEmpty()) {
      if (timeOut < 0.0) {
        Thread.sleep(500);
      } else {
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);
        if (diff > timeOut) {
          System.out.println("SYNC | FAILED | queues_not_empty | waited " + diff + " | exceeded " + timeOut);
          break;
        }
      }
    }

    while (!allResponsesReceived()) {
      if (timeOut < 0.0) {
        Thread.sleep(500);
      } else {
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);
        if (diff > timeOut) {
          System.out.println("SYNC | FAILED | responses_not_received | waited " + diff + " | exceeded " + timeOut);
          break;
        }
      }
    }
  }

  @Override
  public void finishedInit(Drone drone) {
    this.nDronesReady.incrementAndGet();
  }

  @Override
  public void commandSent(Drone drone, String command) {

  }

  public static void main(String[] args) {
    List<Drone> drones = Arrays.asList(
        new Drone(0, new InetSocketAddress("192.168.3.101", 8889))
    );

    List<String> commands = Arrays.asList(
        "* > command",
        "* > battery?"
    );

    Swarm swarm = new Swarm(8889, drones);

    try {
      swarm.init();
      swarm.start(commands);
      swarm.waitAndBlock();
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      swarm.deinit();
    }
  }
}
