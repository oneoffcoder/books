Turtle
======

``Turtle`` is part of the Python API used to draw graphics on the screen. The main objects in Turtle are the ``Screen`` and ``Pen``. The Screen is the canvas that is being drawn onto and the Pen is the object that you use to draw. As always, the best way to learn Turtle is to see some examples and start coding your own creations. 

Draw a line
-----------

Here's a simple program to draw a square.

.. literalinclude:: code/oneoffcoder/turtle/line.py
   :language: python
   :linenos:

.. figure:: _static/images/turtle/line.png

    Line output.

Draw a square
-------------

Here's a simple program to draw a square.

.. literalinclude:: code/oneoffcoder/turtle/square.py
   :language: python
   :linenos:

.. figure:: _static/images/turtle/square.png

    Square output.

Draw stars
----------

Here's code to draw a star.

.. literalinclude:: code/oneoffcoder/turtle/star.py
   :language: python
   :linenos:
   :emphasize-lines: 8-10

.. figure:: _static/images/turtle/star.png

    Star output.

Let's draw a fancy star.

.. literalinclude:: code/oneoffcoder/turtle/fancy-star.py
   :language: python
   :linenos:
   :emphasize-lines: 8-10

.. figure:: _static/images/turtle/fancy-star.png

    Star output.

Draw rectangular spirals
------------------------

Let's draw a rectangular spiral from the inside out. We will change the color that the turtle will use to red. We will also define the ``spiral`` function to draw each spiral.

.. literalinclude:: code/oneoffcoder/turtle/inside-out.py
   :language: python
   :linenos:
   :emphasize-lines: 3-7, 13-14

.. figure:: _static/images/turtle/inside-out.png

    Inside-out rectangular spiral output.

Let's draw a rectangular spiral from the outside-in. Since we are drawing the spirals from the outside-in, we will reverse the sizes.

.. literalinclude:: code/oneoffcoder/turtle/outside-in.py
   :language: python
   :linenos:
   :emphasize-lines: 14-16

.. figure:: _static/images/turtle/outside-in.png

    Outside-in rectangular spiral output.

Draw polygons
-------------

How about polygons? Let's draw a hexagon.

.. literalinclude:: code/oneoffcoder/turtle/hexagon.py
   :language: python
   :linenos:
   :emphasize-lines: 8-10, 12-14

.. figure:: _static/images/turtle/hexagon.png

    Hexagon output.

Draw a spiral helix
-------------------

Let's draw a spiral helix. First, let's change the background color to black. Second, let's define the colors that we want the pen to use. Lastly, since there's a lot to draw, let's set the speed of the pen to 100.

.. literalinclude:: code/oneoffcoder/turtle/spiral-helix.py
   :language: python
   :linenos:
   :emphasize-lines: 5, 7, 10

.. figure:: _static/images/turtle/spiral-helix.png

    Spiral helix output.