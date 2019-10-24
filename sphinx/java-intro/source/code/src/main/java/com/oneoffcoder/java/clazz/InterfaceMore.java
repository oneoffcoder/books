package com.oneoffcoder.java.clazz;

public class InterfaceMore {

  public interface Pet {
    public interface TYPE {
      public int DOG = 1;
      public int CAT = 2;
    }
    public String getName();
    public String getNoise();
    public int getType();

    default String whoAmI() {
      return "Pet";
    }

    static String getNaturalType(int type) {
      switch (type) {
        case TYPE.DOG:
          return "Dog";
        case TYPE.CAT:
          return "Cat";
        default:
          return "Uknown";
      }
    }
  }

  public static abstract class AbstractPet implements Pet {
    protected final String name;
    protected final int type;

    public AbstractPet(String name, int type) {
      this.name = name;
      this.type = type;
    }

    public String getName() { return name; }
    public int getType() { return type; }

    @Override
    public String toString() {
      return name;
    }
  }

  public static class Dog extends AbstractPet {
    public Dog(String name) {
      super(name, Pet.TYPE.DOG);
    }

    @Override
    public String whoAmI() {
      return "Dog";
    }

    @Override
    public String getNoise() {
      return "woof!";
    }
  }

  public static class Cat extends AbstractPet {
    public Cat(String name) {
      super(name, Pet.TYPE.CAT);
    }

    @Override
    public String getNoise() {
      return "meow!";
    }
  }

  public static void main(String[] args) throws Exception {
    var pets = new Pet[] { new Dog("Max"), new Cat("Nancy") };

    for (Pet pet : pets) {
      System.out.println(pet + " says " + pet.getNoise());
      System.out.println("\t" + pet + " is a " + pet.whoAmI());
      System.out.println("\t" + pet + " is naturally a " + Pet.getNaturalType(pet.getType()));
    }
  }

}
