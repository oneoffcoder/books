package com.oneoffcoder.java.enumeration;

public class BasicValueOf {

  enum Gender {
    Male, Female
  }

  public static class Person {

    private String firstName;
    private String lastName;
    private Gender gender;

    public Person(String firstName, String lastName, Gender gender) {
      this.firstName = firstName;
      this.lastName = lastName;
      this.gender = gender;
    }

    public Gender getGender() {
      return gender;
    }

    @Override
    public String toString() {
      return (new StringBuilder())
          .append(firstName)
          .append(' ')
          .append(lastName)
          .toString();
    }
  }

  public static void main(String[] args) throws Exception {
    Person[] people = {
        new Person("John", "Doe", Gender.valueOf("Male")),
        new Person("Jane", "Smith", Gender.valueOf("Female"))
    };

    for (Person person : people) {
      switch (person.getGender()) {
        case Male -> System.out.println(person + " is a male");
        case Female -> System.out.println(person + " is a female");
        default -> System.out.println(person + " has an unknown gender");
      }
    }
  }
}
