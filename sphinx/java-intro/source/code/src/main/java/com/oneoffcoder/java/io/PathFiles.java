package com.oneoffcoder.java.io;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class PathFiles {

  public static void main(String[] args) throws Exception {
    Path path = Path.of("test.txt");
    List<String> names = List.of("John", "Jack", "Jane", "Joyce");

    Files.write(path, names);
    String text = Files.readString(path);

    System.out.println(text);
  }
}
