package com.oneoffcoder.java.collection;

import java.util.HashSet;
import java.util.Set;

public class SetManipulation {

  public static void main(String[] args) throws Exception {
    Set<String> set = new HashSet<>() {{
      add("John");
      add("Joe");
      add("John");
    }};

    // check if element exists
    set.contains("Jack");

    // add element
    set.add("Jack");

    // remove element
    set.remove("John");

    // iteration
    for (var name : set) {
      System.out.println(name);
    }
  }
  
}
