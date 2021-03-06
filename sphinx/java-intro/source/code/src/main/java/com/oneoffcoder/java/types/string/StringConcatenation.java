package com.oneoffcoder.java.types.string;

public class StringConcatenation {

  public static void main(String[] args) throws Exception {
    var s1 = "Hi"; // basic string
    var s2 = "Hello, I am " + " very hungry."; // string concatenation
    var s3 = "I am " + String.format("%.2f", 55.555) + " inches tall."; // string formatting
    var s4 = "Hello, ".concat("world!");
    var s5 = String.join(",", "John", "Jack", "Mary");
  }
}
