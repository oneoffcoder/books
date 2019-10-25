package com.oneoffcoder.java.generic;

public class WildCard {

  public static class Data<T extends Number> {
    private T[] data;

    public Data(T[] data) {
      this.data = data;
    }

    public double getSum() {
      double sum = 0.0d;
      for (T item : data) {
        sum += item.doubleValue();
      }
      return sum;
    }

    public T[] getData() {
      return data;
    }

    public boolean isSameLength(Data<?> that) {
      return this.data.length == that.data.length;
    }
  }

  public static void main(String[] args) throws Exception {
    var data1 = new Data<Integer>(new Integer[] { 1, 2, 3, 4, 9, 10});
    var data2 = new Data<Double>(new Double[] { 5d, 6d, 7d, 8d});

    System.out.println(data1.isSameLength(data2));
  }

}
