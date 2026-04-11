package com.oneoffcoder.java.threading;

import java.time.Duration;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class VirtualThreadDemo {

  public static void main(String[] args) {
    try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
      IntStream.range(0, 5).forEach(i ->
          executor.submit(() -> {
            Thread.sleep(Duration.ofMillis(10));
            System.out.println("task " + i + " ran on " + Thread.currentThread());
            return i;
          }));
    }
  }
}
