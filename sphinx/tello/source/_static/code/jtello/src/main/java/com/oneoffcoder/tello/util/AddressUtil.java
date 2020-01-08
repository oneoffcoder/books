package com.oneoffcoder.tello.util;

import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class AddressUtil {

  private AddressUtil() {

  }

  public static List<InetSocketAddress> getAddresses(String ipPrefix) throws SocketException {
    Set<String> localIps = getLocalIps()
        .stream()
        .map(inetAddress -> inetAddress.toString().replace("/", ""))
        .collect(Collectors.toSet());

    return IntStream.range(2, 254)
        .mapToObj(i -> String.valueOf(i))
        .map(s -> ipPrefix + "." + s)
        .filter(s -> !localIps.contains(s))
        .map(s -> new InetSocketAddress(s, 8889))
        .collect(Collectors.toList());
  }

  public static Set<InetAddress> getLocalIps() throws SocketException {
    return Collections.list(NetworkInterface.getNetworkInterfaces())
        .stream()
        .flatMap(networkInterface -> Collections.list(networkInterface.getInetAddresses()).stream())
        .filter(inetAddress -> inetAddress.toString().indexOf(':') == -1)
        .collect(Collectors.toSet());
  }
}
