package com.oneoffcoder.java.generic;

public class GenericInterface {

  public interface Pet<I> {
    I getId();
    String getName();
    String makeNoise();
  }

  public static class PetImpl implements Pet<Integer> {
    private final Integer id;
    private final String name;
    private final String noise;

    public PetImpl(Integer id, String name, String noise) {
      this.id = id;
      this.name = name;
      this.noise = noise;
    }

    @Override
    public Integer getId() {
      return id;
    }

    @Override
    public String getName() {
      return name;
    }

    @Override
    public String makeNoise() {
      return noise;
    }
  }

  public static void main(String[] args) throws Exception {
    var dog1 = new PetImpl(0, "Max", "woof!");
    var dog2 = new PetImpl(0, "Dax", "bark!");
    var dogs = new Pet[] { dog1, dog2 };

    for (Pet pet : dogs) {
      System.out.println(pet.getId() + ": " + pet.getName() + " says " + pet.makeNoise());
    }
  }
}
