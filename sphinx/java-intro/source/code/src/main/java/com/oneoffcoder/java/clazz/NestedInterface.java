package com.oneoffcoder.java.clazz;

public class NestedInterface {

  public interface Pet {
    public interface TYPE {
      public int DOG = 1;
      public int CAT = 2;
    }
    public String getName();
    public String getNoise();
    public int getType();
  }

}
