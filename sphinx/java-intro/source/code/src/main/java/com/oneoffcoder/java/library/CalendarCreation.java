package com.oneoffcoder.java.library;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class CalendarCreation {

  public static void main(String[] args) throws Exception {
    Calendar calendar = new GregorianCalendar(2019, 0, 31);

    SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
    System.out.println(formatter.format(calendar.getTime()));
  }

}
