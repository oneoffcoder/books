Python, Auto Flight Path
========================

The code below will use Python to fly your Tello drone on a pre-determined flight path. There are four main Python files.

* ``stats.py`` defines the ``Stats`` object to store statistics on command request and response
* ``tello.py`` defines the ``Tello`` object to abstract and represent the Tello drone 
* ``command.txt`` stores the commands that will be sent to the Tello drone
* ``app.py`` is the application program, or the ``driver``, that will be executed as an entrypoint to start sending commands

Stats
-----

The ``Stats`` class is used to log command requests and responses.

.. literalinclude:: _static/code/python/command-program/stats.py
   :language: python
   :linenos:

:download:`Code <_static/code/python/command-program/stats.py>`

Tello
-----

The ``Tello`` class is used to abstract the drone.

.. literalinclude:: _static/code/python/command-program/tello.py
   :language: python
   :linenos:

:download:`Code <_static/code/python/command-program/tello.py>`

Commands
--------

The ``command.txt`` file stores the sequence of string commands that we will send to the drone. Note how we have to put a ``delay 5`` in between commands? This delay gives time for the drone and your program/computer to process the data that being sent back and forth.

.. literalinclude:: _static/code/python/command-program/command.txt
   :language: text
   :linenos:

:download:`Code <_static/code/python/command-program/command.txt>`

Application
-----------

The ``app.py`` file is the application program entry point.

.. literalinclude:: _static/code/python/command-program/app.py
   :language: python
   :linenos:

:download:`Code <_static/code/python/command-program/app.py>`

Running the application
-----------------------

To run the program, type in the following from a terminal. The program will output the logs to the directory ``log/``.

.. code:: bash

    python app.py -f command.txt