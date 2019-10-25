package com.oneoffcoder.java.collection;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

public class ListForEach {

  public static void main(String[] args) throws Exception {
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

    numbers.forEach(n -> System.out.println(n));

    numbers.forEach(System.out::println);
  }

}
