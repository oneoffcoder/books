package com.oneoffcoder.java.tuple;

import org.javatuples.Quintet;

public class Tuple06 {

  public static void main(String[] args) {
    var tuple1 = Quintet.with("John", "Doe", 23, 155.5d, true);
    var list = tuple1.toList();
    var arr = tuple1.toArray();

    var objects = new Object[]{tuple1, list, arr};
    for (var o : objects) {
      System.out.println(o);
    }
  }
}
