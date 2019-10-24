package com.oneoffcoder.java.types;

public class TypesString {

  public static void main(String[] args) throws Exception {
    var s1 = "Hi"; // basic string
    var s2 = "Hello, I am " + " very hungry."; // string concatenation
    var s3 = "I am " + String.format("%.2f", 55.555) + " inches tall."; // string formatting
  }
}
