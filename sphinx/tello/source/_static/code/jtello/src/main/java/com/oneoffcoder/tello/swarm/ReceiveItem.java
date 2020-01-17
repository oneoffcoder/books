package com.oneoffcoder.tello.swarm;

import java.net.InetSocketAddress;

public class ReceiveItem extends MessageItem {

  public ReceiveItem(InetSocketAddress address, String message) {
    super(address, message);
  }
}
