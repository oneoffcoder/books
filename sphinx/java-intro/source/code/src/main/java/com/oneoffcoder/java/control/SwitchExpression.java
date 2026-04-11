package com.oneoffcoder.java.control;

public class SwitchExpression {

  public static void main(String[] args) throws Exception {
    char grade = 'B';

    String feedback = switch (grade) {
      case 'A' -> "great job!";
      case 'B' -> "good job!";
      case 'C' -> "let's do better!";
      case 'D' -> "need serious improvement!";
      default -> {
        String message = "unknown grade: " + grade;
        yield message;
      }
    };

    System.out.println(feedback);
  }

}
