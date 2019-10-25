package com.oneoffcoder.java.library;

import java.util.StringTokenizer;

public class StringTokenization {

  public static void main(String[] args) throws Exception {
    String s = "firstName=John; lastName=John; age=18";

    StringTokenizer tokenizer = new StringTokenizer(s, "=;");

    while (tokenizer.hasMoreTokens()) {
      String key = tokenizer.nextToken().strip();
      String val = tokenizer.nextToken().strip();

      System.out.println(key + " is " + val);
    }
  }

}
