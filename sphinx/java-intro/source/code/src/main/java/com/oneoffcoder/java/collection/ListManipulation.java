package com.oneoffcoder.java.collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListManipulation {

  public static void main(String[] args) throws Exception {
    List<String> names = new ArrayList<>() {{
      add("John");
      add("Joe");
    }};

    // access element
    String joe = names.get(1);

    // set element
    names.set(0, "Jeremy");

    // add element
    names.add("Jack");

    // iteration using for loop
    for (int i = 0; i < names.size(); i++) {
      System.out.println(names.get(i));
    }

    // iteration using for-each
    for (var name : names) {
      System.out.println(name);
    }


  }

}
