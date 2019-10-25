package com.oneoffcoder.java.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

public class TargetAnnotation {

  @Retention(RetentionPolicy.RUNTIME)
  @Target({ElementType.METHOD, ElementType.CONSTRUCTOR})
  @interface NeedsWork {}


  public static class Car {
    private final String make, model;
    private final int year;

    @NeedsWork
    public Car(String make, String model, int year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    @NeedsWork
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
