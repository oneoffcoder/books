package com.oneoffcoder.tello.swarm;

import com.oneoffcoder.tello.swarm.SwarmThread.SwarmThreadListener;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;

public class SwarmManager extends Thread  implements SwarmThreadListener {

  public interface SwarmManagerListener {
    void processMessage(MessageItem message);
  }

  private final SwarmReceiver receiver;
  private final SwarmSender sender;
  private final SwarmManagerListener listener;

  public SwarmManager(DatagramSocket socket, SwarmManagerListener listener) {
    this.receiver = new SwarmReceiver(socket, this);
    this.sender = new SwarmSender(socket, this);
    this.listener = listener;
  }

  @Override
  public void processMessage(MessageItem message) {
    if (null != this.listener) {
      this.listener.processMessage(message);
    }
  }

  public void send(SendItem command) {
    this.sender.addCommand(command);
  }

  public void stopNow() {
    this.sender.stopNow();
    this.receiver.stopNow();
  }

  @Override
  public void run() {
    this.receiver.start();
    this.sender.start();
  }

  public static SwarmManager newInstance(DatagramSocket socket, SwarmManagerListener listener) {
    return new SwarmManager(socket, listener);
  }

  public static void main(String[] args) throws Exception {
    InetSocketAddress address = new InetSocketAddress("192.168.3.108", 8889);

    DatagramSocket socket = new DatagramSocket(8889, InetAddress.getByName("0.0.0.0"));

    SwarmManager manager = new SwarmManager(socket,
        new SwarmManagerListener() {
          @Override
          public void processMessage(MessageItem message) {
            if (message instanceof ReceiveItem) {
              System.out.println("RECEIVED | " + message);
            } else {
              System.out.println("SENT | " + message);
            }
          }
        });

    manager.start();

    manager.send(new SendItem(address, "command"));
  }
}
