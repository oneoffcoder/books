package com.oneoffcoder.java.library;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class CalendarManipulation {

  public static void main(String[] args) throws Exception {
    SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");

    Calendar calendar = Calendar.getInstance();

    // add 1 year
    calendar.add(Calendar.YEAR, 1);
    System.out.println(formatter.format(calendar.getTime()));

    // subtract 2 years
    calendar.add(Calendar.YEAR,-2);
    System.out.println(formatter.format(calendar.getTime()));
  }

}
