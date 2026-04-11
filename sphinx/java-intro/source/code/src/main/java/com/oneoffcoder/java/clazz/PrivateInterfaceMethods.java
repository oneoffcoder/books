package com.oneoffcoder.java.clazz;

public class PrivateInterfaceMethods {

  public interface ScoreFormatter {

    default String passed(String name) {
      return format(name, "passed");
    }

    default String needsReview(String name) {
      return format(name, "needs review");
    }

    private String format(String name, String result) {
      return name + ": " + result;
    }
  }

  public static void main(String[] args) throws Exception {
    var formatter = new ScoreFormatter() {
    };

    System.out.println(formatter.passed("Ada"));
    System.out.println(formatter.needsReview("Grace"));
  }

}
