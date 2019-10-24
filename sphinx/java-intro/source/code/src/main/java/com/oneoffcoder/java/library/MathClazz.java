package com.oneoffcoder.java.library;

public class MathClazz {

  public static void main(String[] args) throws Exception {
    for (int i = 0; i < 5; i++) {
      var num = Math.random();
      var s = String.format("%.5f", num);
      System.out.println(s);
    }
  }

}
