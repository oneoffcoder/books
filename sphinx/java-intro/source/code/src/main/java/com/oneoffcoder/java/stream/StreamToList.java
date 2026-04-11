package com.oneoffcoder.java.stream;

import java.util.List;

public class StreamToList {

  public static void main(String[] args) throws Exception {
    var names = List.of("Ada", "Grace", "Katherine", "Margaret");

    var shortNames = names.stream()
        .filter(name -> name.length() <= 5)
        .toList();

    System.out.println(shortNames);
  }

}
