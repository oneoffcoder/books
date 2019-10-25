package com.oneoffcoder.java.threading;

public class WithExtendingThread {

  public static class TikTok extends Thread {
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
  }


  public static void main(String[] args) throws Exception {
    var t = new Thread(new TikTok());
    t.start();
  }

}
