package com.oneoffcoder.tello;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class Tinker {

  private static void sendCommand(String command, DatagramSocket socket, InetSocketAddress address)
      throws IOException {
    System.out.println("SEND | command | " + address + " | " + command);
    byte[] data = command.getBytes();
    DatagramPacket packet = new DatagramPacket(data, data.length, address);
    socket.send(packet);
  }

  private static String waitForResponse(DatagramSocket socket) throws IOException {
    byte[] data = new byte[1024];
    DatagramPacket packet = new DatagramPacket(data, data.length);

    socket.receive(packet);

    String response = (new String(Arrays.copyOf(data, packet.getLength()), StandardCharsets.UTF_8))
        .trim();
    InetAddress address = packet.getAddress();

    System.out.println("RESPONSE | " + address + " | " + response);

    return response;
  }

  private static Thread getListeningThread(final DatagramSocket socket) {
    Thread thread = new Thread(new Runnable() {
      @Override
      public void run() {
        while (true) {
          try {
            waitForResponse(socket);
          } catch (IOException e) {
            e.printStackTrace();
          }
        }
      }
    });
    return thread;
  }

  public static void main(String[] args) throws Exception {
    try (DatagramSocket socket = new DatagramSocket(8889, InetAddress.getByName("0.0.0.0"))) {
      Thread listeningThread = getListeningThread(socket);
      listeningThread.setDaemon(true);
      listeningThread.start();

      InetSocketAddress telloAddress = new InetSocketAddress("192.168.3.108", 8889);

      sendCommand("command", socket, telloAddress);
//      waitForResponse(socket);

      sendCommand("sn?", socket, telloAddress);
//      waitForResponse(socket);
    }
  }
}
