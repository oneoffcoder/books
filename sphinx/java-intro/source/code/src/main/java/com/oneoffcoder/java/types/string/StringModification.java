package com.oneoffcoder.java.types.string;

public class StringModification {

  public static void main(String[] args) throws Exception {
    String s = " Hello, world! ";

    System.out.println(s.trim());
    System.out.println(s.strip());
    System.out.println(s.replace('o', 'a'));
    System.out.println(s.replaceAll("o", "a"));
    System.out.println(s.toLowerCase());
    System.out.println(s.toUpperCase());
  }

}
