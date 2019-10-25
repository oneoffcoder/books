package com.oneoffcoder.java.stream;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

public class MapFilterReduce {

  public static void main(String[] args) throws Exception {
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

    Optional<Integer> result = numbers.stream()
        .map(num -> num * 2)
        .filter(num -> num % 2 == 0)
        .reduce((a, b) -> a + b);

    System.out.println(result.get());
  }

}
