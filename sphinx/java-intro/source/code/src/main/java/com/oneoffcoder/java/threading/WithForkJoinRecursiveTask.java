package com.oneoffcoder.java.threading;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class WithForkJoinRecursiveTask {

  public static class TokenLengthCounter extends RecursiveTask<Map<Integer, Integer>> {
    private final long workLoad = 100;
    private final String[] tokens;

    public TokenLengthCounter(String[] tokens) {
      this.tokens = tokens;
    }

    @Override
    protected Map<Integer, Integer> compute() {
      if (tokens.length > workLoad) {
        List<TokenLengthCounter> counters = createSubtasks();
        for (var counter : counters) {
          counter.fork();
        }

        Map<Integer, Integer> counts = new HashMap<>();

        for (var counter : counters) {
          Map<Integer, Integer> m = counter.join();

          for (var entry : m.entrySet()) {
            Integer key = entry.getKey();
            Integer val = entry.getValue();

            if (!counts.containsKey(key)) {
              counts.put(key, 0);
            }

            Integer total = counts.get(key) + val;
            counts.put(key, total);
          }
        }

        return counts;
      } else {
        return doCount();
      }
    }

    private List<TokenLengthCounter> createSubtasks() {
      final int n = tokens.length;
      final String[] lhs = Arrays.copyOfRange(tokens, 0, (n + 1) / 2);
      final String[] rhs = Arrays.copyOfRange(tokens, (n + 1) / 2, n);

      List<TokenLengthCounter> counters = new ArrayList<>() {{
        add(new TokenLengthCounter(lhs));
        add(new TokenLengthCounter(rhs));
      }};

      return counters;
    }

    private Map<Integer, Integer> doCount() {
      Map<Integer, Integer> counts = new HashMap<>();
      for (var token : tokens) {
        Integer length = token.length();

        if (!counts.containsKey(length)) {
          counts.put(length, 0);
        }

        Integer total = counts.get(length) + 1;
        counts.put(length, total);
      }
      return counts;
    }
  }

  public static void main(String[] args) throws Exception {
    String[] tokens = getTokens();
    TokenLengthCounter counter = new TokenLengthCounter(getTokens());

    ForkJoinPool pool = ForkJoinPool.commonPool();
    Map<Integer, Integer> counts = pool.invoke(counter);

    for (var entry : counts.entrySet()) {
      System.out.println(entry.getKey() + " : " + entry.getValue());
    }
  }

  private static String[] getTokens() throws IOException {
    String text = new String(
        Files.readAllBytes(
            Paths.get("5827-8.txt")));
    return text.split("\\s+");
  }

}
