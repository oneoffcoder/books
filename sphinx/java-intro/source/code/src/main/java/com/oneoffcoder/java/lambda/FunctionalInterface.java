package com.oneoffcoder.java.lambda;

public class FunctionalInterface {

  interface IntegerTest {
    boolean test(int n);
  }

  public static void main(String[] args) throws Exception {
    IntegerTest isEven = (n) -> n % 2 == 0;

    var numbers = new Integer[] { 1, 2, 3, 4, 5 };
    for (var num : numbers) {
      System.out.println(isEven.test(num));
    }
  }
}
