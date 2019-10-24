package com.oneoffcoder.java.clazz;

public class GetterSetter {

  public static class Car {
    private String make;
    private String model;
    private int year;

    public Car(String make, String model, int year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    public String getMake() {
      return make;
    }

    public String getModel() {
      return model;
    }

    public int getYear() {
      return year;
    }

    public void setMake(String make) {
      this.make = make;
    }

    public void setModel(String model) {
      this.model = model;
    }

    public void setYear(int year) {
      this.year = year;
    }
  }

  public static void main(String[] args) throws Exception {
    var car = new Car("Honda", "Accord", 2019);

    System.out.println(car.getMake() + " " + car.getModel() + " " + car.getYear());
  }

}
