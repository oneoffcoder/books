package com.oneoffcoder.tello;

import java.net.InetAddress;

public interface SwarmListener {
  void responseReceived(InetAddress address, String response);
}
