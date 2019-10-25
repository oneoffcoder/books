package com.oneoffcoder.java.threading;

import java.util.Timer;
import java.util.TimerTask;

public class WithTimer {

  public static void main(String[] args) throws Exception {
    Timer timer = new Timer();

    timer.schedule(new TimerTask() {
        @Override
        public void run() {
          System.out.println("hi");
        }
      }, 1000, 500);

    timer.schedule(new TimerTask() {
      @Override
      public void run() {
        System.out.println("bye");
      }
    }, 1000, 200);

    try {
      Thread.sleep(3000L);
    } catch (InterruptedException e) {
      // swallow
    }

    timer.cancel();
  }
}
