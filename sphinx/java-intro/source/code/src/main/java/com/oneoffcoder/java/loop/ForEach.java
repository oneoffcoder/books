package com.oneoffcoder.java.loop;

public class ForEach {

  public static void main(String[] args) throws Exception {
    var numbers = new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    var sum = 0;

    for (int x : numbers) {
      sum += x;
    }
  }

}
