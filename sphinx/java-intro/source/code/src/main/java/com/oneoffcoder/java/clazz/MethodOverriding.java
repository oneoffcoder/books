package com.oneoffcoder.java.clazz;

public class MethodOverriding {

  public static class Car {
    private String make;
    private String model;
    private int year;

    public Car() {
      this.make = "None";
      this.model = "None";
      this.year = -1;
    }

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
          && this.year == that.year) {
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
      return result;
    }
  }

  public static void main(String[] args) throws Exception {
    var car = new Car("Honda", "Accord", 2019);

    System.out.println(car);

    var car1 = new Car("Honda", "Accord", 2019);
    var car2 = new Car("Honda", "Accord", 2019);
    var car3 = new Car("Honda", "Accord", 2020);

    System.out.println(car1.equals(car2));
    System.out.println(car1.equals(car3));

    System.out.println(car1.hashCode());
    System.out.println(car2.hashCode());
    System.out.println(car3.hashCode());
  }

}
