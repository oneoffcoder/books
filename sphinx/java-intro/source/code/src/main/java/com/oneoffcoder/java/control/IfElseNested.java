package com.oneoffcoder.java.control;

public class IfElseNested {

  public static void main(String[] args) throws Exception {
    int a = 9;

    if (a > 20) {
      System.out.println("a > 20");
    } else if (a > 10) {
      System.out.println("a > 10");
    } else {
      if (a > 5) {
        System.out.println("a > 5");
      } else {
        System.out.println("a <= 5");
      }
    }
  }

}
