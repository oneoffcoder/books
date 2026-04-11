package com.oneoffcoder.java.modern;

public class PatternMatching {

  sealed interface Media permits Book, Movie {}

  record Book(String title, String author, int pages) implements Media {}

  record Movie(String title, int minutes) implements Media {}

  static String describe(Media media) {
    return switch (media) {
      case Book(String title, String author, int pages) when pages > 500 ->
          "long book: " + title + " by " + author;
      case Book(String title, String author, int pages) ->
          "book: " + title + " by " + author;
      case Movie(String title, int minutes) ->
          "movie: " + title + " (" + minutes + " minutes)";
    };
  }

  static int length(Object value) {
    if (value instanceof String text) {
      return text.length();
    }

    return 0;
  }

  public static void main(String[] args) {
    Media book = new Book("Effective Java", "Joshua Bloch", 416);
    Media movie = new Movie("Hidden Figures", 127);

    System.out.println(describe(book));
    System.out.println(describe(movie));
    System.out.println(length("pattern matching"));
  }
}
