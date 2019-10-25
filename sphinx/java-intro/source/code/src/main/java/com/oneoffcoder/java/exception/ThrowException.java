package com.oneoffcoder.java.exception;

public class ThrowException {

  public static void main(String[] args) throws Exception {
    var a = 10;
    var b = 0;

    try {
      var c = a / b;
      System.out.println(a + " / " + b + " = " + c);
    } catch (ArithmeticException e) {
      throw new ArithmeticException(a + " / " + b + " => " + e);
    }
  }

}
