package com.oneoffcoder.java.annotation;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

public class Repeatable {

  @Retention(RetentionPolicy.RUNTIME)
  @java.lang.annotation.Repeatable(TodoRepeat.class)
  @interface Todo {
    String description();
  }

  @Retention(RetentionPolicy.RUNTIME)
  @interface TodoRepeat {
    Todo[] value();
  }

  public static class Car {
    private final String make, model;
    private final int year;

    public Car(String make, String model, int year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    @Todo(description = "use regular string concatenation?")
    @Todo(description = "unit test?")
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
