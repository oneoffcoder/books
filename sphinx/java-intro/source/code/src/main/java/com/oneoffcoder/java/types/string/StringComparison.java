package com.oneoffcoder.java.types.string;

public class StringComparison {

  public static void main(String[] args) throws Exception {
    String s1 = "Hello, world!";
    String s2 = new String("Hello, world!");
    String s3 = "hello, world!";

    // equals and equalsIgnoreCase
    System.out.println(s1.equals(s2));
    System.out.println(s1.equals(s3));
    System.out.println(s1.equalsIgnoreCase(s3));

    // equals vs ==
    System.out.println(s1 == s1);
    System.out.println(s1 == s2);

    // regionMatches
    System.out.println(s1.regionMatches(0, s2, 0, 5));
    System.out.println(s1.regionMatches(0, s3, 0, 5));
    System.out.println(s1.regionMatches(true, 0, s3, 0, 5));

    // startsWith and endsWith
    System.out.println(s1.startsWith("Hello"));
    System.out.println(s1.startsWith("hello"));

    System.out.println(s1.endsWith("world!"));
    System.out.println(s1.endsWith("World!"));

    // compareTo
    System.out.println(s1.compareTo(s2));
    System.out.println(s1.compareTo(s3));
  }

}
