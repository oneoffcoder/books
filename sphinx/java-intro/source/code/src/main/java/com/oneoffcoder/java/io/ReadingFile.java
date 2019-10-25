package com.oneoffcoder.java.io;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class ReadingFile {

  public static void main(String[] args) throws Exception {
    try (var reader = new BufferedReader(new FileReader(new File("test.txt")))) {
      String line = null;
      while ((line = reader.readLine()) != null) {
        System.out.println(line);
      }
    }
  }

}
