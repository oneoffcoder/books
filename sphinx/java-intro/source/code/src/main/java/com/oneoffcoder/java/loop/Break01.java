package com.oneoffcoder.java.loop;

public class Break01 {

  public static void main(String[] args) throws Exception {
    var matrix = new int[][] { {0, 1}, {2, 3}, {4, 5} };

    rowIter: for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] == 3) {
          System.out.println("found 3 at i = " + i + ", j = " + j);
          break rowIter;
        }
      }
    }
  }

}
