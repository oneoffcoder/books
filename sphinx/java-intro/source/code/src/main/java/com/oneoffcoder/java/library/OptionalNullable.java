package com.oneoffcoder.java.library;

import java.util.Optional;

public class OptionalNullable {

  public static void main(String[] args) throws Exception {
    var x = Optional.ofNullable(null);
    // check if empty and presentOptionalExample
    System.out.println(x.isEmpty()); // true
    System.out.println(x.isPresent()); // false

    System.out.println(x.orElse("No name!"));
  }

}
