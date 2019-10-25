package com.oneoffcoder.java.stream;

import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

public class IntStreamDemos {

  public static void main(String[] args) throws Exception {
    // create stream of numbers: 1, 2, 3
    IntStream a = IntStream.range(1, 4);

    // create stream of numbers: 1, 2, 3, 4
    IntStream b = IntStream.rangeClosed(1, 4);

    // create stream of even numbers endlessly
    IntStream c = IntStream.iterate(0, n -> n + 2);

    // create stream of even numbers and take only 3
    IntStream d = IntStream.iterate(0, n -> n + 2)
        .limit(3);

    // generate random numbers
    IntStream e = IntStream.generate(() -> ThreadLocalRandom.current().nextInt(10))
        .limit(3);

    // mapping integers in stream to double their values
    IntStream f = IntStream.range(1, 5)
        .map(n -> n * 2);

    // mapping integers to strings
    Stream<String> g = IntStream.range(1, 5)
        .mapToObj(n -> String.valueOf(n));

    // mapping integers to longs
    LongStream h = IntStream.range(1, 5).mapToLong(n -> n);
    Stream<Long> i = IntStream.range(1, 5)
        .mapToLong(n -> n)
        .boxed();

    // mapping integers to doubles
    DoubleStream j = IntStream.range(1, 5).mapToDouble(n -> n);
    Stream<Double> k = IntStream.range(1, 5)
        .mapToDouble(n -> n)
        .boxed();

    // matching, check if there's at least 1 even number
    boolean l = IntStream.range(1, 5).anyMatch(n -> n % 2 == 0);

    // matching, check if all numbers are even
    boolean m = IntStream.range(1, 5).allMatch(n -> n % 2 == 0);

    // no matches, check if all numbers do not match
    boolean o = IntStream.range(1, 5).noneMatch(n -> n % 2 == 0);

    // get the min
    int p = IntStream.range(1, 5).min().getAsInt();

    // get the max
    int q = IntStream.range(1, 5).max().getAsInt();

    // do a count, note a long is returned
    long r = IntStream.range(1, 5).count();

    // get the average
    double s = IntStream.range(1, 5).average().getAsDouble();

    // get all the distinct elements
    IntStream t = IntStream.of(1, 2, 1, 1, 3, 4, 5).distinct();
  }

}
