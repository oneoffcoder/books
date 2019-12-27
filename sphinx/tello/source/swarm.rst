Swarm Programming
=================

The Tello Edu drone may be programmed in ``swarm`` mode; meaning, you may code behavior into multiple drones at once. The Tello Edu uses the `Tello 2.0 SDK <https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf>`_. The commands for version 2.0 are similar to 1.0, but there are many more commands. Here's a table listing the major commands.

.. csv-table:: Tello 2.0 Commands
   :header: Command, Description, Response

   command, Enter command mode, ok|error
   takeoff, Auto takeoff, ok|error
   land, Auto landing, ok|error
   streamon, Enable video stream, ok|error
   streamoff, Disable video stream, ok|error
   emergency, Stop motors immediately, ok|error
   stop, Hovers in the air, ok|error
   up ``xx``, "Fly upward [20, 500] cm", ok|error
   down ``xx``, "Fly downward [20, 500] cm", ok|error
   left ``xx``, "Fly left [20, 500] cm", ok|error
   right ``xx``, "Fly right [20, 500] cm", ok|error
   forward ``xx``, "Fly forward [20, 500] cm", ok|error
   back ``xx``, "Fly backward [20, 500] cm", ok|error
   cw ``xx``, "Rotate clockwise [1, 360] degrees", ok|error
   ccw ``xx``, "Rotate counter-clockwise [1, 360] degrees", ok|error
   flip ``x``, "Flip [l, r, f, b]", ok|error
   speed ``x``, "Set speed to [10, 100] cm/s", ok|error
   go ``x`` ``y`` ``z`` ``speed``, "Fly to x, y, z at speed", ok|error
   , "``x`` ``y`` ``z`` may be in the range [-500, 500]",
   , "``speed`` is in the range [10, 100] cm/s",
   curve ``x1`` ``y1`` ``z1`` ``x2`` ``y2`` ``z2`` ``speed``, "Fly at a curve between the two given coordinates at speed", ok|error
   , "``x1`` ``y1`` ``z1`` may be in the range [-500, 500]",
   , "``x2`` ``y2`` ``z2`` may be in the range [-500, 500]",
   , "``speed`` is in the range [10, 60] cm/s",
   go ``x`` ``y`` ``z`` ``speed`` ``mid``, "Fly to x, y, z of mission pad at speed", ok|error
   , "``x`` ``y`` ``z`` may be in the range [-500, 500]",
   , "``speed`` is in the range [10, 100] cm/s",
   , "``mid`` is in the domain [m1, m2, m3, m4, m5, m6, m7, m8]",
   curve ``x1`` ``y1`` ``z1`` ``x2`` ``y2`` ``z2`` ``speed`` ``mid``, "Fly at a curve between the two given coordinates of mission pad at speed", ok|error
   , "``x1`` ``y1`` ``z1`` may be in the range [-500, 500]",
   , "``x2`` ``y2`` ``z2`` may be in the range [-500, 500]",
   , "``speed`` is in the range [10, 60] cm/s",
   , "``mid`` is in the domain [m1, m2, m3, m4, m5, m6, m7, m8]",
   jump ``x`` ``y`` ``z`` ``speed`` ``yaw`` ``mid1`` ``mid2``, "Fly to x, y, z of mission pad 1 and recognize coordinates 0, 0, z of mission pad 2 and rotate to yaw value", ok|error
   , "``x`` ``y`` ``z`` may be in the range [-500, 500]",
   , "``speed`` is in the range [10, 100] cm/s",
   , "``mid`` is in the domain [m1, m2, m3, m4, m5, m6, m7, m8]",
   wifi ``ssid`` ``pass``, Set WiFi password, ok|error
   mon, Enable mission pad detection, ok|error
   moff, Disable mission pad detection, ok|error
   mdirection ``x``, Enable mission pad detection, ok|error
   , "``x`` = 0, downward detection only",
   , "``x`` = 1, forward detection only",
   , "``x`` = 2, downward and forward detection",
   ap ``ssid`` ``pass``, Set Tello to station mode and connect to new access point, ok|error
   speed?, Get current speed, "[10, 100]" 
   battery?, Get current battery percentage, "[0, 100]"
   time?, Get current flight time, ``xx``
   wifi?, Get WiFi SNR, ``xx``
   sdk?, Get the SDK version, ``xx``
   sn?, Get the serial number, ``xx``

To start using Python to manipulate the Tello Swarm, make sure you install the following packages ``netifaces`` and ``netaddr``.

.. code-block:: bash
    :linenos:

    conda install -y -c conda-forge netifaces netaddr

Each Tello Edu can exist in ``AP Mode`` or ``Station Mode``.

* ``AP Mode`` or ``Access Point Mode`` is when the Tello becomes a client to a router.
* ``Station Mode`` is when the Tello acts like a router.

Only when a Tello Edu is set to ``AP Mode`` will you be able to use Python to do swarm programming. The script ``set-ap-mode.py`` will help you set the Tello Edu to ``AP Mode``. To reset the Tello Edu back to ``Station Mode``, turn on the drone and then hold the power button for 5 seconds. Below is an example usage of the script; you will need to provide the ``SSID`` and password of the router to the program. Additionally, make sure your router supports the 2.4 GHz bandwidth, as the drone will not connect to the 5.0 GHz bandwidth.

.. code-block:: bash
    :linenos:

    python set-ap-mode.py -s [SSID] -p [PASSWORD]