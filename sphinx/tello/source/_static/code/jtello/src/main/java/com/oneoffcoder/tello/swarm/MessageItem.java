package com.oneoffcoder.tello.swarm;

import java.net.InetSocketAddress;

public abstract class MessageItem {

  private final InetSocketAddress address;
  private final String message;

  public MessageItem(InetSocketAddress address, String message) {
    this.address = address;
    this.message = message;
  }

  public InetSocketAddress getAddress() {
    return address;
  }

  public String getMessage() {
    return message;
  }

  @Override
  public String toString() {
    return new StringBuilder()
        .append(address)
        .append(" | ")
        .append(message)
        .toString();
  }
}
