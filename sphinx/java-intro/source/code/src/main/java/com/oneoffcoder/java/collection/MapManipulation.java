package com.oneoffcoder.java.collection;

import java.util.HashMap;
import java.util.Map;

public class MapManipulation {

  public static void main(String[] args) throws Exception {
    Map<String, Integer> map = new HashMap<>() {{
      put("John", 18);
      put("Joe", 21);
    }};

    // check if key exists
    map.containsKey("John");

    // check if value exists
    map.containsValue(18);

    // add key-value pair
    map.put("Jack", 25);

    // remove key-value pair
    map.remove("John");

    // replace
    map.put("John", 19);

    // iteration
    for (var entry : map.entrySet()) {
      System.out.println(entry.getKey() + " " + entry.getValue());
    }
  }
  
}
