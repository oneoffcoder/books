package com.oneoffcoder.java.modern;

public class RecordData {

  public record Student(String id, String firstName, String lastName, int grade) {

    public String fullName() {
      return firstName + " " + lastName;
    }

    public boolean passing() {
      return grade >= 60;
    }
  }

  public static void main(String[] args) {
    var student = new Student("s-1001", "Ada", "Lovelace", 98);

    System.out.println(student);
    System.out.println(student.id());
    System.out.println(student.fullName());
    System.out.println(student.passing());
  }
}
