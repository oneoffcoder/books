package com.oneoffcoder.java.stream;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Collecting {

  public static void main(String[] args) throws Exception {
    // collecting the stream to a list
    List<Integer> numberList = IntStream
        .generate(() -> ThreadLocalRandom.current().nextInt(10))
        .limit(100)
        .boxed()
        .collect(Collectors.toList());

    // collecting the stream to a set
    Set<Integer> numberSet = IntStream
        .generate(() -> ThreadLocalRandom.current().nextInt(10))
        .limit(100)
        .boxed()
        .collect(Collectors.toSet());

    // String concatenation again
    String s = Arrays.asList("John", "Jack", "Mary", "Nancy")
        .stream()
        .collect(Collectors.joining(","));

    // create a map; keys are names; values are length of names
    Map<String, Integer> m1 =
        Arrays.asList("Jack", "John", "Jeremy", "Mary", "Nancy")
            .stream()
            .collect(Collectors.toMap(e -> e, e -> e.length()));

    // create a map; keys are length of names; values are list of names
    Map<Integer, List<String>> m2 =
        Arrays.asList("Jack", "John", "Jeremy", "Mary", "Nancy")
            .stream()
            .collect(Collectors.groupingBy(
                name -> name.length(),
                Collectors.toList()
            ));
  }

}
