package com.oneoffcoder.java.types.string;

public class TextBlocks {

  public static void main(String[] args) throws Exception {
    String json = """
        {
          "name": "Ada Lovelace",
          "language": "Java"
        }
        """;

    String message = """
        Dear Ada,

        Your program is ready.
        """;

    System.out.println(json.strip());
    System.out.println(message.strip());
  }

}
