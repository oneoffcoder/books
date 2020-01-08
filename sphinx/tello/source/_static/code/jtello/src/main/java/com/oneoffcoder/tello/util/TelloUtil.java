package com.oneoffcoder.tello.util;

import java.util.Date;
import java.util.concurrent.TimeUnit;

public class TelloUtil {

  private TelloUtil() {

  }

  public static long diff(Date start, Date stop) {
    long diff = stop.getTime() - start.getTime();
    return TimeUnit.MILLISECONDS.toSeconds(diff);
  }

}
