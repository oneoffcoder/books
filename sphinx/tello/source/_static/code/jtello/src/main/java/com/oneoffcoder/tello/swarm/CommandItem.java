package com.oneoffcoder.tello.swarm;

import java.util.Arrays;

public class CommandItem {

  private final String id;
  private final String command;

  public CommandItem(String command) {
    String tokens[] = Arrays.stream(command.split(">"))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    this.id = tokens[0];
    this.command = tokens[1];
  }

  public String getId() {
    return id;
  }

  public String getCommand() {
    return command;
  }

  public boolean matchesId(int id) {
    return "*".equals(this.id) || this.id.equalsIgnoreCase(String.valueOf(id));
  }

  @Override
  public String toString() {
    return new StringBuilder()
        .append(id)
        .append(", ")
        .append(command)
        .toString();
  }
}
