package com.oneoffcoder.java.tuple;

import org.javatuples.Quintet;
import org.javatuples.Tuple;

public class Tuple04 {

  public static void main(String[] args) {
    var tuple1 = Quintet.with("John", "Doe", 23, 155.5d, true);
    var tuple2 = tuple1.setAt0("Jane");
    var tuple3 = tuple1.add(true);

    System.out.println(tuple1.equals(tuple2));
    System.out.println(tuple1.equals(tuple3));

    var tuples = new Tuple[]{tuple1, tuple2, tuple3};
    for (var t : tuples) {
      System.out.println(t);
    }
  }
}
