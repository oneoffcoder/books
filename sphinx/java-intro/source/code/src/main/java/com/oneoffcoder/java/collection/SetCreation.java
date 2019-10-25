package com.oneoffcoder.java.collection;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SetCreation {

  public static void main(String[] args) throws Exception {
    Set<String> set1 = new HashSet<>();
    set1.add("John");
    set1.add("Joe");
    set1.add("John");

    Set<String> set2 = new HashSet<>(Arrays.asList("John", "Joe", "John"));

    // cannot add duplicates
    // immutable
    Set<String> set3 = Set.of("John", "Joe");

    Set<String> set4 = new HashSet<>() {{
      add("John");
      add("Joe");
      add("John");
    }};
  }
  
}
