package com.oneoffcoder.java.tuple;

import java.util.stream.Collectors;
import java.util.stream.Stream;
import org.javatuples.Quintet;

public class Tuple02 {

  public static void main(String[] args) {
    var tuple = Quintet.with("John", "Doe", 23, 155.5d, true);

    var firstName = tuple.getValue0();
    var lastName = tuple.getValue1();
    var age = tuple.getValue2();
    var weight = tuple.getValue3();
    var isCoder = tuple.getValue4();

    String s = Stream.of(firstName, lastName, age, weight, isCoder)
        .map(Object::toString)
        .collect(Collectors.joining(", "));
    System.out.println(s);
  }
}
