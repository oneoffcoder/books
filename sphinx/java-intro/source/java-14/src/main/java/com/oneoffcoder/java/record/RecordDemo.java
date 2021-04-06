package com.oneoffcoder.java.record;

public class RecordDemo {
  public record Person(String firstName, String lastName) {
    public String getFullName() {
      return firstName + " " + lastName;
    }
  }

  public static void main(String[] args) {
    Person p1 = new Person("John", "Doe");
    Person p2 = new Person("John", "Doe");
    Person p3 = new Person("Jane", "Doe");

    System.out.println(p1);
    System.out.println(p1.equals(p2));
    System.out.println(p1.equals(p3));
    System.out.println(p1.hashCode() + ", " + p2.hashCode() + ", " + p3.hashCode());
    System.out.println(p1.firstName + ", " + p1.firstName());
    System.out.println(p1.getFullName());

    // p1.firstName = "Tom"; // Cannot assign a value to a final variable
  }
}
