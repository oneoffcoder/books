package com.oneoffcoder.tello.ap;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;

public class SetAccessPoint {

  private static Namespace parseArgs(String[] args) {
    ArgumentParser parser = ArgumentParsers.newFor("Set Access Point")
        .build()
        .defaultHelp(true)
        .description("Sets a Tello in access point mode")
        .version("0.0.1")
        .epilog("One-Off Coder, https://oneoffcoder.com");
    parser.addArgument("-s", "--ssid")
        .help("SSID")
        .required(true);
    parser.addArgument("-p", "--pwd")
        .help("password")
        .required(true);
    parser.addArgument("--ip")
        .help("Tello IP")
        .setDefault("192.168.10.1")
        .required(false);
    parser.addArgument("--port")
        .help("Tello port")
        .type(Integer.class)
        .setDefault(new Integer(8889))
        .required(false);

    Namespace ns = null;
    try {
      ns = parser.parseArgs(args);
    } catch (ArgumentParserException e) {
      parser.handleError(e);
      System.exit(1);
    }

    return ns;
  }

  private static void sendCommand(String command, DatagramSocket socket, InetSocketAddress address)
      throws IOException {
    System.out.println("SEND | command | " + command);
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
    System.out.println("RESPONSE | " + response);

    return response;
  }

  private static void setApMode(String ssid, String pwd, InetSocketAddress telloAddress)
      throws IOException {
    DatagramSocket socket = new DatagramSocket(8889, InetAddress.getByName("0.0.0.0"));

    sendCommand("command", socket, telloAddress);
    waitForResponse(socket);

    sendCommand("ap " + ssid + " " + pwd, socket, telloAddress);
    waitForResponse(socket);
  }

  public static void main(String[] args) throws IOException {
    Namespace ns = parseArgs(args);

    String ssid = ns.getString("ssid");
    String pwd = ns.getString("pwd");
    String telloIp = ns.getString("ip");
    int telloPort = ns.getInt("port");
    InetSocketAddress address = new InetSocketAddress(telloIp, telloPort);

    setApMode(ssid, pwd, address);
  }
}
