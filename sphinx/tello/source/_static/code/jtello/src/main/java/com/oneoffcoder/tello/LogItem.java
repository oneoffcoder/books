package com.oneoffcoder.tello;

import java.net.InetAddress;
import java.util.Date;

public class LogItem {

  final private int id;
  final private String command;
  final private Date startTime;
  private String response;
  private Date stopTime;
  private long duration;
  private InetAddress ip;

  public LogItem(int id, String command) {
    this.id = id;
    this.command = command;
    this.startTime = new Date();
  }

  public String getCommand() {
    return command;
  }

  public void addResponse(String response, InetAddress ip) {
    this.response = response;
    this.stopTime = new Date();
    this.duration = TelloUtil.diff(this.startTime, this.stopTime);
    this.ip = ip;
  }

  public boolean hasResponse() {
    return (null == this.response) ? false : true;
  }

  @Override
  public String toString() {
    return new StringBuilder()
        .append("id=").append(id)
        .append(",")
        .append("ip=").append(ip)
        .append(",")
        .append("command=").append(command)
        .append(",")
        .append("response=").append(response)
        .append(",")
        .append("duration=").append(duration)
        .toString();
  }
}
