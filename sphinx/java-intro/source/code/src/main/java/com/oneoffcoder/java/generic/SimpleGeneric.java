package com.oneoffcoder.java.generic;

public class SimpleGeneric {

  public static class Record<T> {
    T[] data;

    public Record(T[] data) {
      this.data = data;
    }

    @Override
    public String toString() {
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < data.length; i++) {
        sb.append(data[i]);
        if (i < data.length - 1) {
          sb.append(',');
        }
      }
      return sb.toString();
    }
  }

  public static void main(String[] args) throws Exception {
    var record1 = new Record<Integer>(new Integer[] { 1, 2, 3});
    var record2 = new Record<Double>(new Double[] { 1d, 2d, 3d });

    System.out.println(record1);
    System.out.println(record2);
  }


}
