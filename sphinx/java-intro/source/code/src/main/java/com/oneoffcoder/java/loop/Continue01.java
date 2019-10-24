package com.oneoffcoder.java.loop;

public class Continue01 {

  public static void main(String[] args) throws Exception {
    var matrix = new int[][] { {0, 1, 2}, {3, 4, 5}, {6, 7, 8} };

    rowIter: for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] % 2 != 0) {
          System.out.println("found odd number " + matrix[i][j] + " at i = " + i + ", j = " + j);
          continue rowIter;
        }
      }
    }
  }

}
