package com.oneoffcoder.java.stream;

import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class FlatMap {

  public static void main(String[] args) throws Exception {
    String s = IntStream.rangeClosed(1, 5)
        .flatMap(num -> IntStream.rangeClosed(-num, num))
        .sorted()
        .mapToObj(n -> String.valueOf(n))
        .collect(Collectors.joining(","));

    System.out.println(s);
  }

}
