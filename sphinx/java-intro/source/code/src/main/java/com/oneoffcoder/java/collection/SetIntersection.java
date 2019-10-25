package com.oneoffcoder.java.collection;

import java.util.HashSet;
import java.util.Set;

public class SetIntersection {

  public static void main(String[] args) throws Exception {
    Set<String> set1 = new HashSet<>() {{
      add("John");
      add("Joe");
      add("Jack");
    }};

    Set<String> set2 = new HashSet<>() {{
      add("John");
      add("Joe");
      add("Mary");
    }};

    set1.retainAll(set2);
  }
  
}
