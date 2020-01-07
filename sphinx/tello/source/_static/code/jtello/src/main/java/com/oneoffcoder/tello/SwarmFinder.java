package com.oneoffcoder.tello;

import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

public class SwarmFinder {

  final private int nDrones;
  final private DatagramSocket socket;
  final private InetSocketAddress[] addresses;
  final private AtomicInteger dronesDected;

  public SwarmFinder(int nDrones, DatagramSocket socket, String ipPrefix) {
    this.nDrones = nDrones;
    this.dronesDected = new AtomicInteger(0);
    this.socket = socket;
    this.addresses = IntStream.range(2, 254)
        .mapToObj(i -> String.valueOf(i))
        .map(s -> ipPrefix + "." + s)
        .map(s -> new InetSocketAddress(s, 8889))
        .toArray(InetSocketAddress[]::new);
  }

}
