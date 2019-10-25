package com.oneoffcoder.java.threading;

public class WithLambda {

  public static void main(String[] args) throws Exception {
    Thread t = new Thread(() -> {
      final int maxIters = 5;
      final int sleepTime = 500;

      for (int i = 0; i < maxIters; i++) {
        System.out.println("hi");

        try {
          Thread.sleep(sleepTime);
        } catch (InterruptedException e) {
          // swallow
        }
      }
    });

    t.start();
  }

}
