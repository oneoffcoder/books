package com.oneoffcoder.java.annotation;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;

public class Basic {

  @Retention(RetentionPolicy.RUNTIME)
  @interface Author {
    String name() default "No One";
    String org() default "FooBar, LLC";
  }

  @Author(name = "John Doe", org = "One-Off Coder")
  public static class Car {
    private final String make, model;
    private final int year;

    public Car(String make, String model, int year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    @Author(name = "Jane Smith", org = "One-Off Coder")
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

  public static void main(String[] args) throws Exception {
    var car = new Car("Honda", "Accord", 2019);

    Class<?> clazz = car.getClass();
    var clazzAuthor = clazz.getAnnotation(Author.class);

    System.out.println(clazzAuthor.name() + " from " + clazzAuthor.org());

    Method method = clazz.getMethod("toString");
    var methodAuthor = method.getAnnotation(Author.class);

    System.out.println(methodAuthor.name() + " from " + methodAuthor.org());
  }


}
