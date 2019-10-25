package com.oneoffcoder.java.threading;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.atomic.AtomicInteger;

public class WithAtomicInteger {

  private static final Random _random = new Random(37L);

  public static class Worker implements Callable<Integer> {
    private final AtomicInteger counter;
    private final int delay;

    public Worker(AtomicInteger counter) {
      this.counter = counter;
      this.delay = _random.nextInt(2000);
    }

    @Override
    public Integer call() throws Exception {
      try {
        Thread.sleep(delay);
      } catch (InterruptedException e) {
        // swallow
      } finally {
        counter.addAndGet(1);
      }

      return delay;
    }
  }

  public static void main(String[] args) throws Exception {
    final AtomicInteger counter = new AtomicInteger(0);

    final int numWorkers = 100;
    List<Callable<Integer>> callables = new ArrayList<>();
    for (int i = 0; i < numWorkers; i++) {
      callables.add(new Worker(counter));
    }

    ExecutorService service = Executors.newFixedThreadPool(5);
    List<Future<Integer>> futures = new ArrayList<>();
    for (var callable : callables) {
      futures.add(service.submit(callable));
    }

    for (var future : futures) {
      System.out.println(future.get());
    }

    service.shutdown();

    System.out.println("done!");
    System.out.println(counter.get());
  }

}
