package com.oneoffcoder.java.tuple;

import org.javatuples.Pair;
import org.javatuples.Quartet;
import org.javatuples.Quintet;
import org.javatuples.Triplet;
import org.javatuples.Tuple;
import org.javatuples.Unit;

public class Tuple01 {

  public static void main(String[] args) {
    var unit = Unit.with("John");
    var pair = Pair.with("John", "Doe");
    var triplet = Triplet.with("John", "Doe", 23);
    var quartet = Quartet.with("John", "Doe", 23, 155.5d);
    var quintet = Quintet.with("John", "Doe", 23, 155.5d, true);
    // 6-tuple => Sextet
    // 7-tuple => Septet
    // 8-tuple => Octet
    // 9-tuple => Ennead
    // 10-tuple => Decade

    var tuples = new Tuple[]{unit, pair, triplet, quartet, quintet};
    for (Tuple t : tuples) {
      System.out.println(t);
    }
  }
}
