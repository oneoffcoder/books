package com.oneoffcoder.java.clazz;

public class Inheritance {

  public static abstract class Pet {
    protected final String name;

    public Pet(String name) {
      this.name = name;
    }

    public final String whoAmI() {
      return "Pet";
    }

    public abstract String getNoise();

    @Override
    public String toString() {
      return name;
    }
  }

  public static class Dog extends Pet {
    public Dog(String name) {
      super(name);
    }

    @Override
    public String getNoise() {
      return "woof!";
    }

    @Override
    public String toString() {
      return "Dog: " + name;
    }
  }

  public static class Cat extends Pet {
    public Cat(String name) {
      super(name);
    }

    @Override
    public String getNoise() {
      return "meow!";
    }

    @Override
    public String toString() {
      return "Cat: " + name;
    }
  }

  public static void main(String[] args) throws Exception {
    Pet dog = new Dog("Max");
    Pet cat = new Cat("Nancy");

    System.out.println(dog + " says " + dog.getNoise());
    System.out.println(cat + " says " + cat.getNoise());

    System.out.println(dog + " is a " + dog.whoAmI());
    System.out.println(cat + " is a " + cat.whoAmI());
  }

}
