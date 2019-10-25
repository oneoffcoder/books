package com.oneoffcoder.java.library;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import static java.lang.String.valueOf;
import static java.lang.String.format;

public class CalendarBasic {

  public static void main(String[] args) throws Exception {
    Calendar calendar = Calendar.getInstance();

    var month = calendar.get(Calendar.MONTH) + 1;
    var day = calendar.get(Calendar.DATE);
    var year = calendar.get(Calendar.YEAR);
    var hour = calendar.get(Calendar.HOUR);
    var minute = calendar.get(Calendar.MINUTE);
    var second = calendar.get(Calendar.SECOND);

    String date = String.join("-",
        valueOf(year),
        format("%02d", month),
        format("%02d", day));

    String time = String.join(":",
        format("%02d", hour),
        format("%02d", minute),
        format("%02d", second));

    System.out.println(date + " " + time);

    // or use SimpleDateFormat
    SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
    System.out.println(formatter.format(calendar.getTime()));
  }

}
