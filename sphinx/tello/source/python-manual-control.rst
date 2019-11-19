Python, Manual Control
======================

The code below will use Python to fly and control your Tello drone with your keyboard. There are three main Python files.

* ``tello.py`` defines the ``Tello`` object to abstract and represent the Tello drone 
* ``ui.py`` is defines the ``User Interface`` to control your Tello drone
* ``app.py`` is the application program, or the ``driver``, that will be executed as an entrypoint to start sending commands

Tello
-----

The ``Tello`` class is used to abstract the drone.

.. literalinclude:: _static/code/python/control-program/tello.py
   :language: python
   :linenos:

:download:`Code <_static/code/python/control-program/tello.py>`

User Interface
--------------

The ``TelloUI`` class defines the User Interface (UI). The UI listens for the following keys pressed.

* ``↑`` go forward
* ``↓`` go backward
* ``←`` go left
* ``→`` go right
* ``w`` go up
* ``a`` turn counter-clockwise
* ``s`` turn clockwise
* ``d`` go down
* ``l`` flip left
* ``r`` flip right
* ``f`` flip front
* ``b`` flip back

.. literalinclude:: _static/code/python/control-program/ui.py
   :language: python
   :linenos:

:download:`Code <_static/code/python/control-program/ui.py>`

Application
-----------

The ``app.py`` file is the application program entry point.

.. literalinclude:: _static/code/python/control-program/app.py
   :language: python
   :linenos:

:download:`Code <_static/code/python/control-program/app.py>`

Running the application
-----------------------

To run the program, type in the following from a terminal.

.. code:: bash

    python app.py