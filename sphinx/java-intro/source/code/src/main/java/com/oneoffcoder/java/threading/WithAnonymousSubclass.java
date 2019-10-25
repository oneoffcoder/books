package com.oneoffcoder.java.threading;

public class WithAnonymousSubclass {

  public static void main(String[] args) throws Exception {
    var t = new Thread("test") {
      final int maxIters = 5;
      final int sleepTime = 500;

      @Override
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
    };

    t.start();
  }

}
