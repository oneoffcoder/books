package com.oneoffcoder.java.collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ListCreation {

  public static void main(String[] args) throws Exception {
    List<String> list1 = new ArrayList<>();
    list1.add("John");
    list1.add("Joe");

    List<String> list2 = new ArrayList<>(){{
      add("John");
      add("Joe");
    }};

    // immutable
    List<String> list3 = List.of("John", "Joe");

    List<String> list4 = Arrays.asList(new String[] { "John", "Joe" });

    List<String> list5 = Arrays.asList("John", "Joe");
  }

}
