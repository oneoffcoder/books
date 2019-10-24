package com.oneoffcoder.java.threading;

public class ThreadingLesson {

  public static void main(String[] args) throws Exception {
//    Thread t = new Thread(new TikTokRunnable());
//    t.start();

//    TikTokThread t = new TikTokThread();
//    t.start();

//    var t = new Thread("test") {
//      final int maxIters = 5;
//      final int sleepTime = 500;
//
//      @Override
//      public void run() {
//        for (int i = 0; i < maxIters; i++) {
//          System.out.println("hi");
//
//          try {
//            Thread.sleep(sleepTime);
//          } catch (InterruptedException e) {
//            // swallow
//          }
//        }
//      }
//    };
//    t.start();

//    var t = new Thread(() -> {
//      final int maxIters = 5;
//      final int sleepTime = 500;
//
//      for (int i = 0; i < maxIters; i++) {
//        System.out.println("hi");
//
//        try {
//          Thread.sleep(sleepTime);
//        } catch (InterruptedException e) {
//          // swallow
//        }
//      }
//    });
//    t.start();

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
