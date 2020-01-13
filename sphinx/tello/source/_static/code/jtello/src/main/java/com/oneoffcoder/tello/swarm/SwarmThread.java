package com.oneoffcoder.tello.swarm;

import java.net.DatagramSocket;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicBoolean;

public abstract class SwarmThread extends Thread {

  interface SwarmThreadListener {

    void processMessage(MessageItem message);
  }

  protected final long id;
  protected final DatagramSocket socket;
  private final AtomicBoolean stop;
  private final SwarmThreadListener listener;

  public SwarmThread(DatagramSocket socket, SwarmThreadListener listener) {
    this.id = System.currentTimeMillis();
    this.socket = socket;
    this.stop = new AtomicBoolean(false);
    this.listener = listener;
  }

  public void stopNow() {
    this.stop.set(true);
  }

  @Override
  public void run() {
    started();
    while (!this.stop.get()) {
      Optional<MessageItem> message = doIt();
      if (null != this.listener && message.isPresent()) {
        this.listener.processMessage(message.get());
      }

      if (!getThreadId().startsWith("SENDER")) {
        System.out.println(getThreadId() + " | still alive");
      }
    }
    stopped();
  }

  abstract String getThreadId();

  abstract void started();

  abstract Optional<MessageItem> doIt();

  abstract void stopped();
}
