package com.oneoffcoder.java.io;

import java.nio.file.Files;
import java.nio.file.Paths;

public class ReadingFileAllLines {

  public static void main(String[] args) throws Exception {
    for (var line : Files.readAllLines(Paths.get("test.txt"))) {
      System.out.println(line);
    }
  }

}
