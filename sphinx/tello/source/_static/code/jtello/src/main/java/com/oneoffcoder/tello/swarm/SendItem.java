package com.oneoffcoder.tello.swarm;

import java.net.InetSocketAddress;

public class SendItem extends MessageItem {

  public SendItem(InetSocketAddress address, String message) {
    super(address, message);
  }
}
