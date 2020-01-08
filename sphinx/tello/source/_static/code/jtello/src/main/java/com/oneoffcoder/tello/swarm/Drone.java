package com.oneoffcoder.tello.swarm;

import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Drone {

  private final int id;
  private final String sn;
  private final InetSocketAddress address;
  private final List<LogItem> logItems;

  public Drone(int id, String sn, InetSocketAddress address) {
    this.id = id;
    this.sn = sn;
    this.address = address;
    this.logItems = Collections.synchronizedList(new ArrayList<>());
  }

  public void log(String command) {
    String tokens[] = Arrays.stream(command.split(">"))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    String id = tokens[0];
    String c = tokens[1];

    String droneId = String.valueOf(this.id);
    if (droneId.equalsIgnoreCase(id) || id.equals("*")) {
      int logId = this.logItems.size();
      LogItem logItem = new LogItem(logId, command);
      this.logItems.add(logItem);
    }
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
