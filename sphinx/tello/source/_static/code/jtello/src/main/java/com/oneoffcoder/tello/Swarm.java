package com.oneoffcoder.tello;

import com.oneoffcoder.tello.finder.SwarmFinder;
import com.oneoffcoder.tello.finder.SwarmFinder.Builder;
import com.oneoffcoder.tello.io.CommandFile;
import com.oneoffcoder.tello.swarm.CommandItem;
import com.oneoffcoder.tello.swarm.Drone;
import com.oneoffcoder.tello.swarm.MessageItem;
import com.oneoffcoder.tello.swarm.ReceiveItem;
import com.oneoffcoder.tello.swarm.SendItem;
import com.oneoffcoder.tello.swarm.SwarmManager;
import com.oneoffcoder.tello.swarm.SwarmManager.SwarmManagerListener;
import com.oneoffcoder.tello.util.TelloUtil;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;

public class Swarm implements SwarmManagerListener {

  private class SenderThread extends Thread {
    final private AtomicBoolean stop;
    final private SwarmManager manager;
    final private List<Drone> drones;

    public SenderThread(SwarmManager manager, List<Drone> drones) {
      this.stop = new AtomicBoolean(false);
      this.manager = manager;
      this.drones = drones;
    }

    public void stopNow() {
      this.stop.set(true);
    }

    @Override
    public void run() {
      while (true) {
        if (stop.get()) {
          break;
        }

        drones.stream()
            .map(drone -> drone.nextCommand())
            .filter(sendItem -> sendItem.isPresent())
            .map(sendItem -> sendItem.get())
            .forEach(sendItem -> manager.send(sendItem));
      }
    }
  }

  final private SwarmManager manager;
  final private List<String> commands;
  final private List<Drone> drones;
  final private SenderThread senderThread;

  private Swarm(Builder b) {
    this.manager = SwarmManager.newInstance(b.socket, this);
    this.drones = b.drones;
    this.commands = b.commands;
    this.senderThread = new SenderThread(manager, drones);
  }

  @Override
  public void processMessage(MessageItem message) {
    if (message instanceof SendItem) {
      System.out.println("SENT | " + message);
    } else {
      ReceiveItem receiveItem = (ReceiveItem) message;
      System.out.println("RECEIVED | " + message);
      this.drones.forEach(drone -> drone.log(receiveItem));
    }
  }

  private void start() {
    this.manager.start();
    this.senderThread.start();

    for (String command : this.commands) {
      if (command.indexOf(">") != -1) {
        this.handleCommand(command);
      } else if (command.indexOf("sync") != -1) {
        this.handleSync(command);
      }
    }

    waitAndBlock();

    this.senderThread.stopNow();
    this.manager.stopNow();
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

  public static Builder newSwarm() {
    return new Builder();
  }

  public static final class Builder {
    private DatagramSocket socket;
    private List<Drone> drones;
    private List<String> commands;

    private Builder() {

    }

    public Builder socket(DatagramSocket socket) {
      this.socket = socket;
      return this;
    }

    public Builder drones(List<Drone> drones) {
      this.drones = drones;
      return this;
    }

    public Builder commands(List<String> commands) {
      this.commands = commands;
      return this;
    }

    public Swarm build() {
      return new Swarm(this);
    }
  }

  public static void main(String[] args) throws Exception {
    final CommandFile file = new CommandFile(Paths.get("./commands/cmds-01.txt"));
    final DatagramSocket socket = new DatagramSocket(8889, InetAddress.getByName("0.0.0.0"));

    SwarmFinder.newSwarmFinder()
        .socket(socket)
        .ipPrefix(file.getIpPrefix())
        .id2sn(file.getId2sn())
        .listener(drones -> {
          System.out.println("FINDER | finished");
          drones.forEach(System.out::println);

          Swarm.newSwarm()
              .drones(drones)
              .commands(file.getCommands())
              .socket(socket)
              .build()
              .start();
        })
        .build()
        .start();
  }
}
