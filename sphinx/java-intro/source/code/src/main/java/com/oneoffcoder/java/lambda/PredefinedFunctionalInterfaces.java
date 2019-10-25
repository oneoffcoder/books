package com.oneoffcoder.java.lambda;

import java.util.function.BinaryOperator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.function.UnaryOperator;

public class PredefinedFunctionalInterfaces {

  public static void main(String[] args) throws Exception {
    UnaryOperator<Integer> addOne = a -> a + 1;
    System.out.println(addOne.apply(3));

    BinaryOperator<Integer> add = (a, b) -> a + b;
    System.out.println(add.apply(1, 2));

    Consumer<Integer> print = a -> System.out.println(a);
    print.accept(3);

    Supplier<Double> next = () -> Math.random();
    System.out.println(next.get());

    Function<Double[], Double>  sum = (numbers) -> {
      double s = 0.0d;
      for (int i = 0; i < numbers.length; i++) {
        s += numbers[i];
      }
      return s;
    };
    System.out.println(sum.apply(new Double[] { 1.0, 2.0, 3.0 }));

    Predicate<Integer> isEven = a -> a % 2 == 0;
    System.out.println(isEven.test(3));
  }
}
