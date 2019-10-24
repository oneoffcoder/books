package com.oneoffcoder.java.operators;

public class OperatorBitwise {

  public static void main(String[] args) throws Exception {
    var a = 42;
    var b = 15;

    var q = ~42; // bitwise not
    var r = a | b; // bitwise or
    var s = a & b; // btiwise and
    var t = a ^ b; // bitwise XOR
  }

}
