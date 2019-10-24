package com.oneoffcoder.java.loop;

public class Break00 {

  public static void main(String[] args) throws Exception {
    var numbers = new int[] { 0, 1, 2, 3, 4, 5 };

    for (int i = 0; i < numbers.length; i++) {
      if (numbers[i] == 3) {
        System.out.println("found 3 at index " + i);
        break;
      }
    }
  }

}
