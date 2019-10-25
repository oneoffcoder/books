package com.oneoffcoder.java.stream;

import java.util.OptionalInt;
import java.util.stream.IntStream;

public class MapFilterReduceParallel {

  public static void main(String[] args) throws Exception {
    OptionalInt result = IntStream.range(1, 10000)
        .parallel()
        .map(num -> num * 2)
        .filter(num -> num % 2 == 0)
        .reduce((a, b) -> a + b);

    System.out.println(result.getAsInt());
  }

}
