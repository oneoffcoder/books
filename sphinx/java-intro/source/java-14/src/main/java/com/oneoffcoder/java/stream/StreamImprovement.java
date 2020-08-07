package com.oneoffcoder.java.stream;

import java.util.stream.IntStream;

public class StreamImprovement {

  public static void main(String[] args) {
    IntStream.iterate(1, i -> i < 10, i -> i + 1)
        .forEach(System.out::println);
  }

}
