package com.oneoffcoder.java.lambda;

import java.lang.annotation.ElementType;
import java.lang.annotation.Target;
import java.util.List;

public class VarLambdaParameters {

  @Target(ElementType.PARAMETER)
  public @interface NonBlank {
  }

  public static void main(String[] args) throws Exception {
    var names = List.of("Ada", "Grace", "Katherine");

    var upperNames = names.stream()
        .map((@NonBlank var name) -> name.toUpperCase())
        .toList();

    System.out.println(String.join(", ", upperNames));
  }

}
