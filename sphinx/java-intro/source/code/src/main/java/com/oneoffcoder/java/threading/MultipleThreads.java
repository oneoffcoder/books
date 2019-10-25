package com.oneoffcoder.java.threading;

public class MultipleThreads {

  public static void main(String[] args) throws Exception {
    Thread[] threads = new Thread[5];

    for (int i = 0; i < threads.length; i++) {
      final int id = i;
      threads[i] = new Thread(() -> {
        for (int j = 0; j < 5; j++) {
          System.out.println("hi " + id + ": " + j);

          try {
            Thread.sleep(1000L);
          } catch (InterruptedException e) {
            e.printStackTrace();
          }
        }
      });
    }

    for (Thread t : threads) {
      t.start();
    }

    for (Thread t : threads) {
      t.join();
    }
  }

}
