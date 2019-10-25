package com.oneoffcoder.java.types.string;

public class StringExtraction {

  public static void main(String[] args) throws Exception {
    String s = "Hello, world!";

    var c = s.charAt(0);

    var buffer = new char[5];
    s.getChars(0, 5, buffer, 0);

    var bytes = s.getBytes();

    var sub1 = s.substring(0, 5);
    var sub2 = s.substring(8);
  }

}
