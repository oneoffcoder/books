package com.oneoffcoder.java.clazz;

public class StaticMethod {

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

    public static Car getBetterMileage(Car lhs, Car rhs) {
      return lhs.milesPerGallon > rhs.milesPerGallon ? lhs : rhs;
    }
  }

  public static void main(String[] args) throws Exception {
    Car car1 = new Car("Honda", "Accord", 2019, 22.0);
    Car car2 = new Car("Honda", "Civic", 2019, 25.0);

    System.out.println(car1 + " vs " + car2);
    System.out.println(Car.getBetterMileage(car1, car2) + " has better mileage");
  }

}
