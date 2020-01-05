package com.oneoffcoder.tello;

import java.util.Date;
import java.util.concurrent.TimeUnit;

public class TelloUtil {

  public static long diff(Date start, Date stop) {
    long diff = stop.getTime() - start.getTime();
    return TimeUnit.MILLISECONDS.toSeconds(diff);
  }

}
