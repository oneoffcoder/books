package com.oneoffcoder.java.control;

public class SwitchNested {

  public static void main(String[] args) throws Exception {
    int ethnicity = 1;
    String gender = "female";

    switch (ethnicity) {
      case 0:
        switch (gender) {
          case "male":
            System.out.println("white male");
            break;
          default:
            System.out.println("white female");
        }
      case 1:
        switch (gender) {
          case "male":
            System.out.println("minority male");
            break;
          default:
            System.out.println("minority female");
        }
    }
  }

}
