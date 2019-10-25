package com.oneoffcoder.java.library;

import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.ICSVParser;
import java.io.FileReader;

public class OpenCsvRead {

  public static void main(String[] args) throws Exception {
    final var parser = new CSVParserBuilder()
        .withSeparator(ICSVParser.DEFAULT_SEPARATOR)
        .withQuoteChar(ICSVParser.DEFAULT_QUOTE_CHARACTER)
        .withEscapeChar(ICSVParser.DEFAULT_ESCAPE_CHARACTER)
        .build();

    final var reader = new CSVReaderBuilder(new FileReader("demo.csv"))
        .withSkipLines(1)
        .withCSVParser(parser)
        .build();

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

    reader.close();
  }

}
