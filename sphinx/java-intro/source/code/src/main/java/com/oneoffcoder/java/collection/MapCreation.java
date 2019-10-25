package com.oneoffcoder.java.collection;

import java.util.HashMap;
import java.util.Map;

public class MapCreation {

  public static void main(String[] args) throws Exception {
    Map<String, Integer> map1 = new HashMap<>();
    map1.put("John", 18);
    map1.put("Joe", 21);

    Map<String, Integer> map2 = new HashMap<>() {{
      put("John", 18);
      put("Joe", 21);
    }};
  }
  
}
