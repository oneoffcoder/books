package com.oneoffcoder.java.threading;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class WithCallable {

  public static class Tuple {
    public final String name;
    public final Integer factorial;

    public Tuple(String name, Integer factorial) {
      this.name = name;
      this.factorial = factorial;
    }

    @Override
    public String toString() {
      return name + " : " + factorial;
    }
  }

  public static class FactorialWorker implements Callable<Tuple> {
    private final String name;
    private final Integer num;

    public FactorialWorker(String name, Integer num) {
      this.name = name;
      this.num = num;
    }

    @Override
    public Tuple call() throws Exception {
      int value = 1;
      for (int i = 2; i < num; i++) {
        value *= i;
      }
      return new Tuple(name, value);
    }
  }

  public static void main(String[] args) throws Exception {
    final int numWorkers = 100;
    final Random random = new Random(37L);

    List<Callable<Tuple>> callables = new ArrayList<>();
    for (int i = 0; i < numWorkers; i++) {
      Integer num = random.nextInt(15);
      Callable<Tuple> callable = new FactorialWorker(String.valueOf(i), num);
      callables.add(callable);
    }

    ExecutorService service = Executors.newFixedThreadPool(5);
    List<Future<Tuple>> futures = new ArrayList<>();
    for (var callable : callables) {
      futures.add(service.submit(callable));
    }

    for (var future : futures) {
      System.out.println(future.get());
    }

    service.shutdown();

    System.out.println("done!");
  }

}
