package com.oneoffcoder.java.enumeration;

import java.util.Random;

public class EnumClass {

  enum Item {
    Hat(5.00d), Shirt(10.00), Pants(15.00), Shoes(50.00), Socks(3.00);

    private double price;

    Item(double price) {
      this.price = price;
    }
  }

  public static void main(String[] args) throws Exception {
    var items = Item.values();

    var purchases = new Item[3];
    Random random = new Random(37L);
    for (int i = 0; i < purchases.length; i++) {
      int index = random.nextInt(items.length);
      purchases[i] = items[index];
    }

    double total = 0.0d;
    for (Item item : purchases) {
      total += item.price;
    }

    System.out.println(total);
  }
}
