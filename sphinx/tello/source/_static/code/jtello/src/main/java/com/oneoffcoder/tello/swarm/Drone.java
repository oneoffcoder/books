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

public class Drone {

  private static final float TIME_OUT = 10.0f;

  private final int id;
  private final String sn;
  private final InetSocketAddress address;
  private final List<LogItem> logItems;
  private final Queue<SendItem> commands;

  public Drone(int id, String sn, InetSocketAddress address) {
    this.id = id;
    this.sn = sn;
    this.address = address;
    this.logItems = Collections.synchronizedList(new ArrayList<>());
    this.commands = new LinkedBlockingQueue<>();
  }

  public void queue(CommandItem command) {
    if (command.matchesId(this.id)) {
      this.logItems.add(new LogItem(this.nextLogId(), command.getCommand()));
      this.commands.add(new SendItem(this.address, command.getCommand()));
    }
  }

  public Optional<SendItem> nextCommand() {
    if (this.ready() && !this.commands.isEmpty()) {
      return Optional.of(this.commands.remove());
    }
    return Optional.empty();
  }

  public void log(ReceiveItem receiveItem) {
    if (receiveItem.addressMatches(this.address)) {
      LogItem logItem = getLastLogItem();
      logItem.addResponse(receiveItem.getMessage(), receiveItem.getAddress().getAddress());
    }
  }

  private int nextLogId() {
    return this.logItems.size();
  }

  private boolean ready() {
    if (this.logItems.size() < 1) {
      return true;
    } else {
      LogItem logItem = this.getLastLogItem();
      if (logItem.hasResponse()) {
        return true;
      } else {
        Date start = logItem.getStartTime();
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);

        if (diff > TIME_OUT) {
          return true;
        } else {
          return false;
        }
      }
    }
  }

  private LogItem getLastLogItem() {
    int index = this.logItems.size() - 1;
    return this.logItems.get(index);
  }

  @Override
  public String toString() {
    return (new StringBuilder())
        .append(this.id)
        .append(",")
        .append(this.sn)
        .append(",")
        .append(this.address)
        .toString();
  }
}
