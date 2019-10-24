package com.oneoffcoder.java.library;

import com.opencsv.CSVWriterBuilder;
import com.opencsv.ICSVParser;
import com.opencsv.ICSVWriter;
import java.io.FileWriter;

public class OpenCsvWrite {

  public static void main(String[] args) throws Exception {
    var writer = new CSVWriterBuilder(new FileWriter("demo.csv"))
        .withSeparator(ICSVParser.DEFAULT_SEPARATOR)
        .withQuoteChar(ICSVParser.DEFAULT_QUOTE_CHARACTER)
        .withEscapeChar(ICSVParser.DEFAULT_ESCAPE_CHARACTER)
        .withLineEnd(ICSVWriter.DEFAULT_LINE_END)
        .build();

    var entries = new String[][] {
        { "first_name", "last_name" },
        { "John", "Doe" },
        { "Jane", "Smith" }
    };

    for (String[] row : entries) {
      writer.writeNext(row);
    }

    writer.close();
  }

}
