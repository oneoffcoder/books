package com.oneoffcoder.java.exception;

import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVParser;
import com.opencsv.ICSVWriter;
import java.io.FileReader;
import java.io.FileWriter;

public class TryCatchFinallyResource {

  public static void main(String[] args) throws Exception {
    try (var writer = new CSVWriterBuilder(new FileWriter("demo.csv"))
        .withSeparator(ICSVParser.DEFAULT_SEPARATOR)
        .withQuoteChar(ICSVParser.DEFAULT_QUOTE_CHARACTER)
        .withEscapeChar(ICSVParser.DEFAULT_ESCAPE_CHARACTER)
        .withLineEnd(ICSVWriter.DEFAULT_LINE_END)
        .build()) {

      var entries = new String[][] {
          { "first_name", "last_name" },
          { "John", "Doe" },
          { "Jane", "Smith" }
      };

      for (String[] row : entries) {
        writer.writeNext(row);
      }
    }

    final var parser = new CSVParserBuilder()
        .withSeparator(ICSVParser.DEFAULT_SEPARATOR)
        .withQuoteChar(ICSVParser.DEFAULT_QUOTE_CHARACTER)
        .withEscapeChar(ICSVParser.DEFAULT_ESCAPE_CHARACTER)
        .build();

    try (var reader = new CSVReaderBuilder(new FileReader("demo.csv"))
        .withSkipLines(1)
        .withCSVParser(parser)
        .build()) {
      String[] line;
      while ((line = reader.readNext()) != null) {
        for (int i = 0; i < line.length; i++) {
          System.out.print(line[i]);
          if (i < line.length - 1) {
            System.out.print(", ");
          } else if (i == line.length - 1) {
            System.out.println();
          }
        }
      }
    }
  }

}
