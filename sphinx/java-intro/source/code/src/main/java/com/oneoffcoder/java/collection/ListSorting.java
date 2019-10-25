package com.oneoffcoder.java.collection;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ListSorting {

  public static void main(String[] args) throws Exception {
    // unsorted
    List<String> names = Arrays.asList("John", "Jack", "Jimmy");

    for (var name : names) {
      System.out.println(name);
    }

    // sorted ascendingly
    Collections.sort(names);

    for (var name : names) {
      System.out.println(name);
    }

    // sorted descendingly
    Collections.sort(names, Collections.reverseOrder());

    for (var name : names) {
      System.out.println(name);
    }

    // custom sorting, sort by second character
    Collections.sort(names, (lhs, rhs) -> {
      Character lhsChar = lhs.charAt(1);
      Character rhsChar = lhs.charAt(1);
      return lhsChar.compareTo(rhsChar);
    });

    for (var name : names) {
      System.out.println(name);
    }
  }

}
