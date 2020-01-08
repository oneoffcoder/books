package com.oneoffcoder.tello;

import com.oneoffcoder.tello.swarm.CommandItem;
import com.oneoffcoder.tello.swarm.Drone;
import com.oneoffcoder.tello.util.TelloUtil;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Swarm {


  final private List<String> commands;
  final private List<Drone> drones;

  public Swarm(List<Drone> drones, List<String> commands) {
    this.drones = drones;
    this.commands = commands;
  }

  private void start() {
    for (String command : this.commands) {
      if (command.indexOf(">") != -1) {
        this.handleCommand(command);
      } else if (command.indexOf("sync") != -1) {
        this.handleSync(command);
      }
    }

    waitAndBlock();
  }

  private void handleCommand(String command) {
    CommandItem commandItem = new CommandItem(command);
    this.drones.forEach(d -> d.queue(commandItem));
  }

  private void handleSync(String command) {
    String[] tokens = Arrays.stream(command.split(" "))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    float timeOut = Float.parseFloat(tokens[1]);
    sync(timeOut);
  }

  private void waitAndBlock() {
    sync(-1.0f);
  }

  private boolean allQueuesEmpty() {
    long n = this.drones.stream()
        .map(d -> !d.isCommandQueueEmpty())
        .count();
    return (n > 0) ? false : true;
  }

  private boolean allResponsesReceived() {
    long n = this.drones.stream()
        .filter(d -> d.logSize() > 0)
        .filter(d -> !d.getLastLogItem().hasResponse())
        .count();
    return (n > 0) ? false : true;
  }

  private void sync(float timeOut) {
    Date start = new Date();

    while (!allQueuesEmpty()) {
      if (timeOut < 0.0) {
        try {
          Thread.sleep(500);
        } catch (InterruptedException e) {
          // swallow
        }
      } else {
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);
        if (diff > timeOut) {
          System.out.println(
              "SYNC | FAILED | queues_not_empty | waited " + diff + " | exceeded " + timeOut);
          break;
        }
      }
    }

    while (!allResponsesReceived()) {
      if (timeOut < 0.0) {
        try {
          Thread.sleep(500);
        } catch (InterruptedException e) {
          // swallow
        }
      } else {
        Date now = new Date();
        float diff = TelloUtil.diff(start, now);
        if (diff > timeOut) {
          System.out.println(
              "SYNC | FAILED | responses_not_received | waited " + diff + " | exceeded " + timeOut);
          break;
        }
      }
    }
  }

  public static void main(String[] args) {
    Map<Integer, String> id2sn = new HashMap<Integer, String>() {{
      put(1, "0TQZGANED0021X");
      put(2, "0TQZGANED0020C");
      put(3, "0TQZGARED000KN");
      put(4, "0TQZGANED0023H");
    }};

    List<String> commands = Arrays.asList(
        "* > battery?"
    );

//    Swarm swarm = new Swarm(8889, commands);
//
//    try {
//      swarm.waitAndBlock();
//    } catch (Exception e) {
//      e.printStackTrace();
//    }
  }
}
