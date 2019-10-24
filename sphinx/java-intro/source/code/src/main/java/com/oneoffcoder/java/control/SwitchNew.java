package com.oneoffcoder.java.control;

public class SwitchNew {

  public static void main(String[] args) throws Exception {
    char grade = 'B';

    switch (grade) {
      case 'A' -> System.out.println("great job!");
      case 'B' -> System.out.println("good job!");
      case 'C' -> System.out.println("let's do better!");
      case 'D' -> System.out.println("need serious improvement!");
      default -> System.out.println("ouch!");
    }
  }

}
