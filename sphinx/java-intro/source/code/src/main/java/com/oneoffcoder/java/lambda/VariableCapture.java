package com.oneoffcoder.java.lambda;

public class VariableCapture {

  interface StringOp {
    String f(String s);
  }

  public static void main(String[] args) throws Exception {
    final int max = 10;
    StringOp op = (s) -> {
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < max; i++) {
        sb.append(s);
        if (i < max - 1) {
          sb.append(',');
        }
      }
      return sb.toString();
    };

    System.out.println(op.f("dog"));
    System.out.println(op.f("cat"));
  }
}
