package com.oneoffcoder.java.threading;

public class TikTokRunnable implements Runnable {
  final int maxIters = 5;
  final int sleepTime = 500;

  public void run() {
    for (int i = 0; i < maxIters; i++) {
      System.out.println("hi");

      try {
        Thread.sleep(sleepTime);
      } catch (InterruptedException e) {
        // swallow
      }
    }
  }
}
