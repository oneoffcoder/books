package com.oneoffcoder.java.threading;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class WithExecutor {

  public static class Worker extends Thread {
    private final int delay;
    private final CountDownLatch latch;

    public Worker(String name, int delay, CountDownLatch latch) {
      super(name);
      this.delay = delay;
      this.latch = latch;
    }

    @Override
    public void run() {
      while (latch.getCount() > 0) {
        System.out.println(getName() + ": " + latch.getCount());

        latch.countDown();

        try {
          Thread.sleep(delay);
        } catch (InterruptedException e) {
          // swallow
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    String[] names = { "a", "b", "c" };
    int[] delays = { 500, 1000, 2000 };
    CountDownLatch[] latches = {
        new CountDownLatch(5),
        new CountDownLatch(10),
        new CountDownLatch(3)
    };

    Thread[] threads = new Thread[3];
    for (int i = 0; i < threads.length; i++) {
      threads[i] = new Worker(names[i], delays[i], latches[i]);
    }

    ExecutorService service = Executors.newFixedThreadPool(5);
    for (Thread thread : threads) {
      service.execute(thread);
    }

    for (CountDownLatch latch : latches) {
      try {
        latch.await();
      } catch (InterruptedException e) {
        // swallow
      }
    }

    service.shutdown();

    System.out.println("done!");
  }

}
