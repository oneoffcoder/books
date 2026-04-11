package com.oneoffcoder.java.modern;

import module java.base;

public class ModuleImportDemo {

  public static void main(String[] args) {
    List<String> names = List.of("Ada", "Grace", "Katherine");
    Path report = Path.of("names.txt");

    String text = names.stream()
        .map(String::toUpperCase)
        .collect(Collectors.joining(", "));

    System.out.println(report.toAbsolutePath());
    System.out.println(text);
  }
}
