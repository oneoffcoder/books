package com.oneoffcoder.java.library;

import java.util.Optional;

public class OptionalBasic {

  public static void main(String[] args) throws Exception {
    var x = Optional.of("John");
    // check if empty
    System.out.println(x.isEmpty()); // false

    // get value
    System.out.println(x.get()); // John
  }

}
