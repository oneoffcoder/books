package com.oneoffcoder.tello.swarm;

import com.oneoffcoder.tello.util.TelloUtil;
import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Optional;
import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicBoolean;

public class Drone {

  private static final float TIME_OUT = 10.0f;

  private final int id;
  private final String sn;
  private final InetSocketAddress address;
  private final List<LogItem> logItems;
  private final Queue<SendItem> commands;
  private final AtomicBoolean isReady;

  public Drone(int id, String sn, InetSocketAddress address) {
    this.id = id;
    this.sn = sn;
    this.address = address;
    this.logItems = Collections.synchronizedList(new ArrayList<>());
    this.commands = new LinkedBlockingQueue<>();
    this.isReady = new AtomicBoolean(true);
  }

  public void queue(CommandItem command) {
    if (command.matchesId(this.id)) {
      LogItem logItem = new LogItem(this.nextLogId(), command.getCommand());
      System.out.println("QUEUED | " + logItem);
      this.logItems.add(logItem);


      this.commands.add(new SendItem(this.address, command.getCommand()));
    }
  }

  public Optional<SendItem> nextCommand() {
    if (this.ready() && !this.commands.isEmpty()) {
      this.isReady.set(false);
      return Optional.of(this.commands.remove());
    }
    return Optional.empty();
  }

  public void log(ReceiveItem receiveItem) {
    if (receiveItem.addressMatches(this.address)) {
      LogItem logItem = getLastLogItem();
      logItem.addResponse(receiveItem.getMessage(), receiveItem.getAddress().getAddress());
      System.out.println("RECEIVED | " + logItem);
      this.isReady.set(true);
    }
  }

  public int logSize() {
    return this.logItems.size();
  }

  private int nextLogId() {
    return this.logItems.size();
  }

  private boolean ready() {
    return this.isReady.get();
  }

  public LogItem getLastLogItem() {
    int index = this.logItems.stream()
        .filter(logItem -> !logItem.hasResponse())
        .sorted((a, b) -> a.getId().compareTo(b.getId()))
        .findFirst()
        .get()
        .getId();
    return this.logItems.get(index);
  }

  public boolean isCommandQueueEmpty() {
    return this.commands.isEmpty();
  }

  @Override
  public String toString() {
    return (new StringBuilder())
        .append(this.id)
        .append(", ")
        .append(this.sn)
        .append(", ")
        .append(this.address)
        .toString();
  }
}
