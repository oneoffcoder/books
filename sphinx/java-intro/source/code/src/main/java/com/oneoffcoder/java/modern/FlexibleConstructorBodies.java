package com.oneoffcoder.java.modern;

public class FlexibleConstructorBodies {

  static class Rectangle {
    private final int width;
    private final int height;

    Rectangle(int width, int height) {
      this.width = width;
      this.height = height;
    }

    int area() {
      return width * height;
    }
  }

  static class PositiveRectangle extends Rectangle {

    PositiveRectangle(int width, int height) {
      if (width <= 0 || height <= 0) {
        throw new IllegalArgumentException("dimensions must be positive");
      }

      super(width, height);
    }
  }

  public static void main(String[] args) {
    var rectangle = new PositiveRectangle(10, 5);
    System.out.println(rectangle.area());
  }
}
