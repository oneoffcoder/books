package com.oneoffcoder.java.generic;

public class TwoTypeGeneric {

  public static class Record<I, T> {
    I id;
    T[] data;

    public Record(I id, T[] data) {
      this.id = id;
      this.data = data;
    }

    @Override
    public String toString() {
      StringBuilder sb = new StringBuilder();
      sb.append(id).append(':');

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
    var record1 = new Record<Integer, Integer>(0, new Integer[] { 1, 2, 3});
    var record2 = new Record<String, Double>("a", new Double[] { 1d, 2d, 3d });

    System.out.println(record1);
    System.out.println(record2);
  }


}
