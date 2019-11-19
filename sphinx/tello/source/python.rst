Python Programming
==================

Python Setup
------------

You may actually use any programming language that can establish a UDP connection to send commands to the Tello drone, however, in this book, we will use ``Python`` to send commands to the drone. Python programming is an intermediate to advanced subject. Make sure you are comfortable and familiar with Python programming. The Python code is adapted from the ``DJI`` `GitHub <https://github.com/dji-sdk/Tello-Python>`_ repository. 


To be able to run the Python programs, you will need to have Python 3.x or higher. The use of `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ or `Anaconda <https://anaconda-installer.readthedocs.io/en/latest/>`_ is highly recommended. Setting up the environment you will need to get the Python drone programming examples working is rather involved. We recommend you select your favorite Python environment and follow the installation instruction. Additionally, please stop by `One-Off Coder <https://www.oneoffcoder.com>`_ for hands-on help.

Tello Software Development Kit
------------------------------

You may establish a ``UDP`` connection to the Tello on port ``8889`` and send commands. There are versions ``1.0`` and ``2.0`` to communicate with the ``Tello`` and ``Tello EDU``, respectively. We will be using version 1.0. The following are manuals listing the commands that may be sent.

* `Tello 1.0 SDK <https://dl-cdn.ryzerobotics.com/downloads/tello/0228/Tello+SDK+Readme.pdf>`_
* `Tello 2.0 SDK <https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf>`_

We list the Tello 1.0 commands in the following table.

.. csv-table:: Tello 1.0 Commands
   :header: Command, Description, Response

   command, Enter command mode, OK|False
   takeoff, Auto takeoff, OK|False
   land, Auto landing, OK|False
   up ``xx``, "Fly upward [20, 500] cm", OK|False
   down ``xx``, "Fly downward [20, 500] cm", OK|False
   left ``xx``, "Fly left [20, 500] cm", OK|False
   right ``xx``, "Fly right [20, 500] cm", OK|False
   forward ``xx``, "Fly forward [20, 500] cm", OK|False
   cw ``xx``, "Rotate clockwise [1, 360] degrees", OK|False
   ccw ``xx``, "Rotate counter-clockwise [1, 360] degrees", OK|False
   flip ``x``, "Flip [l, r, f, b]", OK|False
   speed ``xx``, "Set speed [1, 100] cm/s", OK|False
   Speed?, Get current speed, ``xx``
   Battery?, Get current battery percentage, ``xx``
   Time?, Get current flight time, ``xx``

