package com.oneoffcoder.java.lambda;

public class BlockLambda {

  interface StringMerger {
    String f(String ... items);
  }

  public static void main(String[] args) throws Exception {
    StringMerger classicMerger = (items) -> {
      String s = "";
      for (int i = 0; i < items.length; i++) {
        s += items[i];
        if (i < items.length - 1) {
          s += ",";
        }
      }
      return s;
    };

    StringMerger sbMerger = (items) -> {
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < items.length; i++) {
        sb.append(items[i]);
        if (i < items.length - 1) {
          sb.append(',');
        }
      }
      return sb.toString();
    };

    StringMerger backwardMerger = (items) -> {
      String s = "";
      for (int i = items.length - 1; i >= 0; i--) {
        s += items[i];
        if (i > 0) {
          s += ",";
        }
      }
      return s;
    };

    var tokens = new String[] { "John", "Jack", "Jake", "Joe" };

    System.out.println(classicMerger.f(tokens));
    System.out.println(sbMerger.f(tokens));
    System.out.println(backwardMerger.f(tokens));
  }
}
