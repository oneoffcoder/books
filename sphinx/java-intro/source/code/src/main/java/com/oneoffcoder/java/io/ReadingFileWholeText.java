package com.oneoffcoder.java.io;

import java.nio.file.Files;
import java.nio.file.Paths;

public class ReadingFileWholeText {

  public static void main(String[] args) throws Exception {
    String text = new String(
        Files.readAllBytes(
            Paths.get("test.txt")));

    System.out.println(text);
  }

}
