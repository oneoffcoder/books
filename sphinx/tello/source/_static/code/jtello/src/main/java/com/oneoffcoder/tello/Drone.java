package com.oneoffcoder.tello;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

public class Drone implements SwarmListener {
  private int id;
  private boolean active;
  private SocketAddress address;
  private Queue<String> queue;
  private List<LogItem> logItems;
  private AtomicInteger nCommands;
  private AtomicInteger nResponses;
  private DatagramSocket socket;
  private DroneListener droneListener;
  private Thread sendThread;
  private AtomicBoolean stopThread;

  public Drone(int id, SocketAddress address) {
    this.id = id;
    this.active = false;
    this.address = address;
    this.queue = new LinkedBlockingQueue<>();
    this.logItems = Collections.synchronizedList(new ArrayList<>());
    this.nCommands = new AtomicInteger();
    this.nResponses = new AtomicInteger();
  }

  public void init(DatagramSocket socket, DroneListener droneListener) {
    this.socket = socket;
    this.droneListener = droneListener;
    this.stopThread = new AtomicBoolean(false);

    this.sendThread = new Thread(new Runnable() {
      private void waitForResponse() {
        final float TIME_OUT = 10.0f;

        Date start = new Date();
        int logIndex = Drone.this.logItems.size() - 1;

        while (!Drone.this.logItems.get(logIndex).hasResponse()) {
          Date now = new Date();
          float diff = TelloUtil.diff(start, now);

          if (diff > TIME_OUT) {
            LogItem logItem = Drone.this.logItems.get(logIndex);
            System.out.println("WAIT RESPONSE | timeout | " + diff + " | " +
                logItem.getCommand() + " | " + logItem.hasResponse());
            break;
          }
        }
      }

      @Override
      public void run() {
        while (true) {
          if (Drone.this.stopThread.get()) {
            System.out.println("THREAD | send | stopped");
            break;
          }

          if (Drone.this.queue.isEmpty()) {
            continue;
          }

          if (Drone.this.nResponses.get() < Drone.this.nCommands.get()) {
            continue;
          }

          try {
            String command = Drone.this.queue.remove();
            byte[] data = command.getBytes();
            DatagramPacket packet = new DatagramPacket(data, data.length, Drone.this.address);
            Drone.this.socket.send(packet);

            InetSocketAddress addr = (InetSocketAddress)Drone.this.address;

            System.out.println("COMMAND | " +
                addr.getAddress().toString() + " | " + command);
            int id = Drone.this.nCommands.incrementAndGet();

            LogItem logItem = new LogItem(id, command);
            Drone.this.logItems.add(logItem);

            waitForResponse();
          } catch (Exception e) {
            System.out.println("THREAD | SEND | socket_error | " + e);
            e.printStackTrace();
          }
        }
      }
    });
    this.sendThread.setDaemon(true);
    this.sendThread.start();

    if (null != this.droneListener) {
      this.droneListener.finishedInit(this);
    }
  }

  public void deinit() {
    this.stopThread.set(false);
    System.out.println("DRONE DEINIT | " + this.address);
  }

  public void addCommand(String command) {
    String tokens[] = Arrays.stream(command.split(">"))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    String id = tokens[0];
    String c = tokens[1];

    String droneId = String.valueOf(this.id);
    if (droneId.equalsIgnoreCase(id) || id.equals("*")) {
      this.queue.add(c);
    }
  }

  public Queue<String> getQueue() {
    return queue;
  }

  public List<LogItem> getLogItems() {
    return logItems;
  }

  @Override
  public void responseReceived(InetAddress address, String response) {
    InetSocketAddress addr = (InetSocketAddress)Drone.this.address;
    String s1 = addr.getAddress().toString();
    String s2 = address.toString();

    if (s1.equalsIgnoreCase(s2)) {
      int logIndex = this.logItems.size() - 1;
      LogItem logItem = this.logItems.get(logIndex);
      logItem.addResponse(response, address);
      System.out.println("LOG | " + logItem.toString());

      this.nResponses.incrementAndGet();
    }
  }
}
