package com.oneoffcoder.java.library;

import java.util.Random;

public class RandomNumberGeneration {

  public static void main(String[] args) throws Exception {
    Random random = new Random(37L);

    var a = random.nextBoolean();
    var b = random.nextDouble();
    var c = random.nextInt();
    var d = random.nextInt(100);
    var e = random.nextFloat();
    var f = random.nextGaussian();
    var g = random.nextLong();
  }

}
