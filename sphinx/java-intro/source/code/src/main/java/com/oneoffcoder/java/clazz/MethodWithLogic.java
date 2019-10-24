package com.oneoffcoder.java.clazz;

public class MethodWithLogic {

  public static class Car {
    private String make;
    private String model;
    private int year;
    private double milesPerGallon;

    public Car() {
      this("None", "None", -1, 0.0d);
    }

    public Car(String make, String model, int year, double milesPerGallon) {
      this.make = make;
      this.model = model;
      this.year = year;
      this.milesPerGallon = milesPerGallon;
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

    public double getMilesPerGallon() {
      return milesPerGallon;
    }

    public double getMiles(double gallons) {
      return milesPerGallon * gallons;
    }

    public double getGallons(double miles) {
      return (1.0 / milesPerGallon) * miles;
    }

    @Override
    public String toString() {
      return make + " " + model + " " + year;
    }

    @Override
    public boolean equals(Object object) {
      if (object == this) {
        return true;
      }

      if (null == object || !(object instanceof Car)) {
        return false;
      }

      var that = (Car)object;
      if (this.make.equals(that.make)
          && this.model.equals(that.model)
          && this.year == that.year
          && this.milesPerGallon == that.milesPerGallon) {
        return true;
      }

      return false;
    }

    @Override
    public int hashCode() {
      int result = 17;
      result = 31 * result + make.hashCode();
      result = 31 * result + model.hashCode();
      result = 31 * result + (new Integer(year)).hashCode();
      result = 31 * result + (new Double(milesPerGallon).hashCode());
      return result;
    }
  }

  public static void main(String[] args) throws Exception {
    Car car = new Car("Honda", "Accord", 2019, 22.0d);

    var miles = 100;
    var gallons = 20;

    var gallonsRequired = car.getGallons(miles);
    var mileage = car.getMiles(gallons);

    System.out.println(car + " can travel " + miles +
        " but needs " + String.format("%.2f", gallonsRequired) + " gallons of gas");

    System.out.println(car + " with " + gallons +
        " gallons of gas can travel " + mileage + " miles");
  }

}
