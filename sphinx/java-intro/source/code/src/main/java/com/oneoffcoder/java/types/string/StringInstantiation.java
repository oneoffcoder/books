package com.oneoffcoder.java.types.string;

public class StringInstantiation {

  public static void main(String[] args) throws Exception {
    String s1 = "Hello, world!";
    String s2 = new String("Hello, world!");

    var characters = new char[] {'H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!'};
    String s3 = new String(characters);
    String s4 = new String(characters, 0, 5);

    var ascii = new byte[] {72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33};
    String s5 = new String(ascii);
  }
}
