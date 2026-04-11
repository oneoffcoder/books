package com.oneoffcoder.java.threading;

public class ScopedValueDemo {

  private static final ScopedValue<String> REQUEST_ID = ScopedValue.newInstance();

  public static void main(String[] args) {
    ScopedValue.where(REQUEST_ID, "request-1001")
        .run(ScopedValueDemo::handle);
  }

  private static void handle() {
    System.out.println("handling " + REQUEST_ID.get());
  }
}
