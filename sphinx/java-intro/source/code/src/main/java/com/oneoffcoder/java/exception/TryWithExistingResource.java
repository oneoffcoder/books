package com.oneoffcoder.java.exception;

import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;

public class TryWithExistingResource {

  public static void main(String[] args) throws Exception {
    BufferedReader reader = Files.newBufferedReader(Path.of("test.txt"));

    try (reader) {
      System.out.println(reader.readLine());
    }
  }

}
