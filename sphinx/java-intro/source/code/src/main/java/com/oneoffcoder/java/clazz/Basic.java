package com.oneoffcoder.java.clazz;

public class Basic {

  public static class Car {
    String make;
    String model;
    int year;

    public Car(String make, String model, int year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }
  }

  public static void main(String[] args) throws Exception {
    var car = new Car("Honda", "Accord", 2019);

    System.out.println(car.make + " " + car.model + " " + car.year);
  }

}
