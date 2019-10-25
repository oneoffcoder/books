package com.oneoffcoder.java.types;

public class TypeWrapper {

  public static void main(String[] args) throws Exception {
    // wrapping the primitives into object types
    Byte b = 127;
    Short s = 32_767;
    Integer i = 2_147_483_647;
    Long l = 9_223_372_036_854_775_807L;
    Float f = 3.4e38f;
    Double d = 1.7e308d;
    Character c = 'Z';
    Boolean o = true;

    // getting the primitives back
    byte bb = b.byteValue();
    short ss = s.shortValue();
    int ii = i.intValue();
    long ll = l.longValue();
    float ff = f.floatValue();
    double dd = d.doubleValue();
    char cc = c.charValue();
    boolean oo = o.booleanValue();
  }

}
