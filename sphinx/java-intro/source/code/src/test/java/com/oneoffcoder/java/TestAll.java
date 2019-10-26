package com.oneoffcoder.java;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.URL;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.Collectors;
import org.junit.Assert;
import org.junit.Test;

public class TestAll {

  public static class Tuple {
    private final Class clazz;
    private final Exception exception;
    private final boolean success;

    public Tuple(Class clazz, Exception exception, boolean success) {
      this.clazz = clazz;
      this.exception = exception;
      this.success = success;
    }

    @Override
    public String toString() {
      if (!success) {
        return clazz.getName() + ": " + exception.toString();
      } else {
        return clazz.getName();
      }
    }
  }

  public static class TestWorker implements Callable<Tuple> {
    private final Class clazz;

    public TestWorker(Class clazz) {
      this.clazz = clazz;
    }

    @Override
    public Tuple call() throws Exception {
      Exception exception = null;
      boolean success = true;

      try {
        final Method method = clazz.getMethod("main", String[].class);
        final Object[] args = {new String[]{}};
        method.invoke(null, args);
      } catch (NoSuchMethodException e) {
        // swallow
      } catch (Exception e) {
        exception = e;
        success = false;
      }

      return new Tuple(clazz, exception, success);
    }
  }

  /**
   * Look at https://stackoverflow.com/questions/15582476/how-to-call-main-method-of-a-class-using-reflection-in-java.
   * @throws IOException
   * @throws ClassNotFoundException
   */
  @Test
  public void testAll()
      throws IOException, ClassNotFoundException, ExecutionException, InterruptedException {
    final Set<String> ignore = new HashSet<>() {{
      add("com.oneoffcoder.java.TestAll");
      add("com.oneoffcoder.java.exception.ThrowException");
      add("com.oneoffcoder.java.exception.DivideByZero");
    }};

    List<Callable<Tuple>> callables = getClasses("com.oneoffcoder.java")
        .stream()
        .filter(c -> !ignore.contains(c.getName()))
        .map(c -> new TestWorker(c))
        .collect(Collectors.toList());

    ExecutorService service = Executors.newFixedThreadPool(10);
    List<Future<Tuple>> futures = new ArrayList<>();
    for (var callable : callables) {
      futures.add(service.submit(callable));
    }

    List<Tuple> results = futures.stream()
        .map(f -> {
          try {
            return Optional.of(f.get());
          } catch (Exception e) {
            // swallow
          }
          return Optional.ofNullable(null);
        })
        .filter(o -> o.isPresent())
        .map(o -> (Tuple)o.get())
        .collect(Collectors.toList());

    results.forEach(tuple -> {
      if (!tuple.success) {
        Assert.assertTrue(tuple.toString(), false);
      }
    });

    service.shutdown();

    System.out.println("done testing!");
  }

  /**
   * Look at https://stackoverflow.com/questions/520328/can-you-find-all-classes-in-a-package-using-reflection.
   * @param packageName Package name. e.g. "com.oneoffcoder.java"
   * @return Array of classes.
   * @throws ClassNotFoundException
   * @throws IOException
   */
  private static List<Class> getClasses(String packageName)
      throws ClassNotFoundException, IOException {
    ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
    assert classLoader != null;
    String path = packageName.replace('.', '/');
    Enumeration<URL> resources = classLoader.getResources(path);
    List<File> dirs = new ArrayList<File>();
    while (resources.hasMoreElements()) {
      URL resource = resources.nextElement();
      dirs.add(new File(resource.getFile()));
    }

    List<Class> classes = new ArrayList<Class>();
    for (File directory : dirs) {
      classes.addAll(findClasses(directory, packageName));
    }
    return classes;
  }

  /**
   * Look at https://stackoverflow.com/questions/520328/can-you-find-all-classes-in-a-package-using-reflection.
   * @param directory Directory.
   * @param packageName Package name.
   * @return List of classes.
   * @throws ClassNotFoundException
   */
  private static List<Class> findClasses(File directory, String packageName)
      throws ClassNotFoundException {
    List<Class> classes = new ArrayList<Class>();
    if (!directory.exists()) {
      return classes;
    }
    File[] files = directory.listFiles();
    for (File file : files) {
      if (file.isDirectory()) {
        assert !file.getName().contains(".");
        classes.addAll(findClasses(file, packageName + "." + file.getName()));
      } else if (file.getName().endsWith(".class")) {
        classes.add(Class
            .forName(packageName + '.' + file.getName().substring(0, file.getName().length() - 6)));
      }
    }
    return classes;
  }
}
