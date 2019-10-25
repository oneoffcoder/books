package com.oneoffcoder.java.lambda;

public class GenericFunctionalInterface {

  interface NumberFormatter<T extends Number> {
    String format(T num);
  }

  public static void main(String[] args) throws Exception {
    NumberFormatter formatter = (num) -> String.format("%.3f", num);

    var data = new Double[] { 1.22222, 3.44444, 5.823432 };
    for (var num : data) {
      System.out.println(formatter.format(num));
    }
  }
}
