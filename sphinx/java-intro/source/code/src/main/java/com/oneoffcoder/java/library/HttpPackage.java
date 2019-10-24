package com.oneoffcoder.java.library;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class HttpPackage {

  public static void main(String[] args) throws Exception {
    String uri = "http://www.oneoffcoder.com";

    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(uri))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());

    String body = response.body();

    System.out.println(body.length());
  }

}
