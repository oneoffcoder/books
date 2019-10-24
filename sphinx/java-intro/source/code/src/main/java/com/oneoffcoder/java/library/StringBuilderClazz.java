package com.oneoffcoder.java.library;

public class StringBuilderClazz {

  public static void main(String[] args) throws Exception {
    var entity = "One-Off Coder";
    var address = "7526 Old Linton Hall Road";
    var city = "Gainesville";
    var state = "VA";
    var zip = 20155;
    var www = "https://www.oneoffcoder.com";
    var email = "info@oneoffcoder.com";

    var label = new StringBuilder()
        .append(entity).append('\n')
        .append(address).append('\n')
        .append(city).append(' ')
        .append(state).append(' ')
        .append(zip).append('\n')
        .append(www).append('\n')
        .append(email)
        .toString();

    System.out.println(label);
  }

}
