package com.oneoffcoder.tello;

public interface DroneListener {

  void finishedInit(Drone drone);

  void commandSent(Drone drone, String command);
}
