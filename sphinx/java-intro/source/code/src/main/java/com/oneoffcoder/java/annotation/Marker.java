package com.oneoffcoder.java.annotation;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

public class Marker {

  @Retention(RetentionPolicy.RUNTIME)
  @interface OneOffCoder { }

  @OneOffCoder
  public static class Car {
    private final String make, model;
    private final int year;

    public Car(String make, String model, int year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    @OneOffCoder
    @Override
    public String toString() {
      return (new StringBuilder())
          .append(make)
          .append(' ')
          .append(model)
          .append(' ')
          .append(year)
          .toString();
    }
  }

}
