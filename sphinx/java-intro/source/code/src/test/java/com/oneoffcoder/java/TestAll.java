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
import java.util.Set;
import org.junit.Assert;
import org.junit.Test;

public class TestAll {

  /**
   * Look at https://stackoverflow.com/questions/15582476/how-to-call-main-method-of-a-class-using-reflection-in-java.
   * @throws IOException
   * @throws ClassNotFoundException
   * @throws NoSuchMethodException
   * @throws InvocationTargetException
   * @throws IllegalAccessException
   */
  @Test
  public void testAll()
      throws IOException, ClassNotFoundException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {
    Set<String> ignore = new HashSet<>() {{
      add("com.oneoffcoder.java.TestAll");
      add("com.oneoffcoder.java.exception.ThrowException");
      add("com.oneoffcoder.java.exception.DivideByZero");
    }};

    Class[] classes = getClasses("com.oneoffcoder.java");
    for (var c : classes) {
      if (ignore.contains(c.getName())) {
        continue;
      }

      System.out.println(c.getName());

      try {
        final Method method = c.getMethod("main", String[].class);
        final Object[] args = {new String[]{}};
        method.invoke(null, args);
      } catch (NoSuchMethodException e) {
        // swallow
      } catch (Exception e) {
        Assert.assertTrue("Uknown exception: " + c, false);
      }
    }
  }

  /**
   * Look at https://stackoverflow.com/questions/520328/can-you-find-all-classes-in-a-package-using-reflection.
   * @param packageName Package name. e.g. "com.oneoffcoder.java"
   * @return Array of classes.
   * @throws ClassNotFoundException
   * @throws IOException
   */
  private static Class[] getClasses(String packageName)
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
    ArrayList<Class> classes = new ArrayList<Class>();
    for (File directory : dirs) {
      classes.addAll(findClasses(directory, packageName));
    }
    return classes.toArray(new Class[classes.size()]);
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
