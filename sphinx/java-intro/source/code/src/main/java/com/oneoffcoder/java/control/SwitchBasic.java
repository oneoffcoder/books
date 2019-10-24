package com.oneoffcoder.java.control;

public class SwitchBasic {

  public static void main(String[] args) throws Exception {
    char grade = 'B';

    switch (grade) {
      case 'A':
        System.out.println("great job!");
        break;
      case 'B':
        System.out.println("good job!");
        break;
      case 'C':
        System.out.println("let's do better!");
        break;
      case 'D':
        System.out.println("need serious improvement!");
        break;
      default:
        System.out.println("ouch!");
    }
  }

}
