package com.oneoffcoder.java.lombok;

import lombok.Builder;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import lombok.experimental.Accessors;

public class Lombok00 {


  public static void main(String[] args) {
    var p1 = new Person("John", "Doe", 23, 155.5, true);
    var p2 = new Person("John", "Doe", 23, 155.5, true);
    var p3 = Person.builder()
        .firstName("Jane")
        .lastName("Smith")
        .age(21)
        .weight(125.5)
        .isCoder(true)
        .build();

    System.out.println(p1.equals(p2));
    System.out.println(p1.equals(p3));

    // p1.firstName = "Jane"; // Cannot assign a value to a final variable
  }

  @Getter
  @Setter
  @RequiredArgsConstructor
  @Accessors(fluent = true)
  @Builder(toBuilder = true)
  @ToString
  @EqualsAndHashCode
  static public class Person {

    @NonNull
    private final String firstName;
    @NonNull
    private final String lastName;
    @NonNull
    private final int age;
    @NonNull
    private final double weight;
    @NonNull
    private final boolean isCoder;
  }
}
