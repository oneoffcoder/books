package com.oneoffcoder.java.exception;

public class TryCatchFinally {

  public static void main(String[] args) throws Exception {
    var a = 10;
    var b = 0;
    var c = -1;

    try {
      c = a / b;
    } catch (ArithmeticException e) {
      // swallow
    } finally {
      if (c == -1) {
        System.err.println(a + " / " + b + " cannot be computed");
      }
    }
  }

}
