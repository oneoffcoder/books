package com.oneoffcoder.tello.swarm;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Optional;

public class SwarmReceiver extends SwarmThread {

  public SwarmReceiver(DatagramSocket socket, SwarmThreadListener listener) {
    super(socket, listener);
  }

  @Override
  public String getThreadId() {
    return new StringBuilder()
        .append("RECEIVER | ")
        .append(this.id)
        .toString();
  }

  @Override
  void started() {
    System.out.println("RECEIVER | " + this.id + " | started");
  }

  @Override
  Optional<MessageItem> doIt() {
    try {
      byte[] buffer;
      DatagramPacket packet;
      InetAddress address;
      int port;

      buffer = new byte[1024];
      packet = new DatagramPacket(buffer, buffer.length);
      socket.receive(packet);

      byte[] data = Arrays.copyOf(buffer, packet.getLength());
      String response = (new String(data, StandardCharsets.UTF_8)).trim();
      address = packet.getAddress();
      port = packet.getPort();

      return Optional.of(new ReceiveItem(new InetSocketAddress(address, port), response));
    } catch (Exception e) {
      return Optional.empty();
    }
  }

  @Override
  void stopped() {
    System.out.println("RECEIVER | " + this.id + " | stopped");
  }
}
