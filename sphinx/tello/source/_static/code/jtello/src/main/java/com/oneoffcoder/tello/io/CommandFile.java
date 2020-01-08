package com.oneoffcoder.tello.io;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

public class CommandFile {

  private class Tuple {
    public String key, val;
    public Tuple(String k, String v) {
      this.key = k;
      this.val = v;
    }
  }

  private String ipPrefix;
  private final Map<Integer, String> id2sn;
  private final List<String> commands;

  public CommandFile(Path input) throws IOException {
    this.id2sn = new HashMap<>();
    this.commands = new ArrayList<>();

    try (Stream<String> stream = Files.lines(input)) {
      stream.forEach(line -> {
        if (line.indexOf("=") != -1) {
          Tuple tuple = this.split(line);

          if ("ip".equalsIgnoreCase(tuple.key)) {
            this.ipPrefix = tuple.val;
          } else {
            int id = Integer.parseInt(tuple.key);
            String sn = tuple.val;

            this.id2sn.put(id, sn);
          }
        } else {
          this.commands.add(line);
        }
      });
    }
  }

  private Tuple split(String line) {
    String tokens[] = Arrays.stream(line.split("="))
        .map(t -> t.trim())
        .filter(t -> t.length() > 0)
        .toArray(String[]::new);
    String k = tokens[0];
    String v = tokens[1];

    return new Tuple(k, v);
  }

  public String getIpPrefix() {
    return ipPrefix;
  }

  public Map<Integer, String> getId2sn() {
    return id2sn;
  }

  public List<String> getCommands() {
    return commands;
  }

  public static void main(String[] args) throws IOException {
    CommandFile file = new CommandFile(Paths.get("cmds-01.txt"));

    System.out.println(file.getIpPrefix());

    file.getId2sn().entrySet().stream()
        .forEach(e -> System.out.println(e.getKey() + " : " + e.getValue()));

    file.getCommands().stream()
        .forEach(System.out::println);
  }
}
