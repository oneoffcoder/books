package com.oneoffcoder.tello;

import java.util.List;

public interface SwarmFinderListener {
  void finishedFindingDrones(List<Drone> drones);
}
