package com.oneoffcoder.java.lambda;

public class LambdaAsArg {

  interface MathFunc {
    int doIt(int v1, int v2);
  }

  static int mathOp(MathFunc f, int v1, int v2) {
    return f.doIt(v1, v2);
  }

  public static void main(String[] args) throws Exception {
    MathFunc add = (v1, v2) -> v1 + v2;
    MathFunc sub = (v1, v2) -> v1 - v2;
    MathFunc mul = (v1, v2) -> v1 * v2;
    MathFunc div = (v1, v2) -> v1 / v2;

    System.out.println(mathOp(add, 10, 8));
    System.out.println(mathOp(sub, 10, 8));
    System.out.println(mathOp(mul, 10, 8));
    System.out.println(mathOp(div, 10, 8));
  }
}
