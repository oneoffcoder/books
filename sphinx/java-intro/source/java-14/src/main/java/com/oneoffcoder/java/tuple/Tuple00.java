package com.oneoffcoder.java.tuple;

import java.util.Arrays;
import org.javatuples.Pair;

public class Tuple00 {

  public static void main(String[] args) {
    var pair1 = new Pair<>("John", "Doe");
    var pair2 = Pair.with("John", "Doe");
    var pair3 = Pair.fromCollection(Arrays.asList("John", "Doe"));
    var pair4 = Pair.fromArray(new String[]{"John", "Doe"});

    var pairs = new Pair[]{pair1, pair2, pair3, pair4};
    for (var p : pairs) {
      System.out.println(p);
    }
  }
}
