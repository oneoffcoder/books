package com.oneoffcoder.java.operators;

public class OperatorBooleanLogical {

  public static void main(String[] args) throws Exception {
    var a = false;
    var b = false;

    var a_or_b = a | b;
    var a_and_b = a & b;
    var a_xor_b = a ^ b;
    var not_a = !a;
    var a_short_or_b = a || b;
    var a_short_and_b = a && b;
    var ternary = a ? true : false;
  }

}
