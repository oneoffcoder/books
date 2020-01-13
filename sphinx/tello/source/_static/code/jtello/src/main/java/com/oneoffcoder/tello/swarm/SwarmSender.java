package com.oneoffcoder.tello.swarm;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.util.Optional;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class SwarmSender extends SwarmThread {

  private final Queue<SendItem> commands;

  public SwarmSender(DatagramSocket socket, SwarmThreadListener listener) {
    super(socket, listener);
    this.commands = new LinkedBlockingQueue<>();
  }

  public void addCommand(SendItem command) {
    this.commands.add(command);
  }

  @Override
  public String getThreadId() {
    return new StringBuilder()
        .append("SENDER | ")
        .append(this.id)
        .toString();
  }

  @Override
  void started() {
    System.out.println("SENDER | " + this.id + " | started");
  }

  @Override
  Optional<MessageItem> doIt() {
    if (this.commands.isEmpty()) {
      return Optional.empty();
    }

    try {
      SendItem sendItem = this.commands.remove();
      InetSocketAddress address = sendItem.getAddress();
      String message = sendItem.getMessage();

      byte[] data = message.getBytes();
      DatagramPacket packet = new DatagramPacket(data, data.length, address);
      socket.send(packet);

      return Optional.of(sendItem);
    } catch (Exception e) {
      return Optional.empty();
    }
  }

  @Override
  void stopped() {
    System.out.println("SENDER | " + this.id + " | stopped");
  }
}
