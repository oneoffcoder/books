package com.oneoffcoder.java.io;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.Arrays;
import java.util.List;

public class WritingFile {

  public static void main(String[] args) throws Exception {
    List<String> names = Arrays.asList("John", "Jack", "Jane", "Joyce");

    try (var writer = new BufferedWriter(new FileWriter(new File("test.txt")))) {
      for (var name : names) {
        writer.write(name);
        writer.write('\n');
      }
    }
  }

}
