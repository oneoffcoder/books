package com.oneoffcoder.java.stream;

import java.util.OptionalInt;
import java.util.stream.IntStream;

public class MapFilterReduceWithIntStream {

  public static void main(String[] args) throws Exception {
    OptionalInt result = IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        .map(num -> num * 2)
        .filter(num -> num % 2 == 0)
        .reduce((a, b) -> a + b);

    System.out.println(result.getAsInt());
  }

}
