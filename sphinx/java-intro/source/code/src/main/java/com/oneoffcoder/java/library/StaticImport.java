package com.oneoffcoder.java.library;

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

public class StaticImport {

  public static void main(String[] args) throws Exception {
    var num = 100.0d;
    var s = sqrt(num);
    var p = pow(num, 2.0d);
  }
}
