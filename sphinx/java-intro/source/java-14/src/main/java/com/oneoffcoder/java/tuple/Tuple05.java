package com.oneoffcoder.java.tuple;

import org.javatuples.Quintet;
import org.javatuples.Tuple;

public class Tuple05 {

  public static void main(String[] args) {
    var tuple1 = Quintet.with("John", "Doe", 23, 155.5d, true);
    var tuple2 = tuple1.removeFrom0();

    System.out.println(tuple1.equals(tuple2));

    var tuples = new Tuple[]{tuple1, tuple2};
    for (var t : tuples) {
      System.out.println(t);
    }
  }
}
