package com.oneoffcoder.java.types.string;

public class StringValueOf {

  public static void main(String[] args) throws Exception {
    Byte b = 127;
    Short s = 32_767;
    Integer i = 2_147_483_647;
    Long l = 9_223_372_036_854_775_807L;
    Float f = 3.4e38f;
    Double d = 1.7e308d;
    Character c = 'Z';
    Boolean o = true;

    String bb = String.valueOf(b);
    String ss = String.valueOf(s);
    String ii = String.valueOf(i);
    String ff = String.valueOf(f);
    String dd = String.valueOf(d);
    String cc = String.valueOf(c);
    String oo = String.valueOf(o);

    bb = b.toString();
    ss = s.toString();
    ii = i.toString();
    ff = f.toString();
    dd = f.toString();
    cc = c.toString();
    oo = c.toString();
  }

}
