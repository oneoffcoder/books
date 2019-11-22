Functions
=========

Basic functions
---------------

.. figure:: _static/images/functions/ex1.png
   :scale: 50%

In the figure above, there are five basic functions:

    1.  ``Sum``
    2.  ``Average``
    3.  ``Count``
    4.  ``Max``
    5.  ``Min``

Sum
^^^

The ``sum`` function adds a selection cells and takes on the following form:

    ``=sum(number1,number2,number3,...)``

There are three ways to go about using sum. 

The first way is to manually type ``=sum(A1,A2,A3,A4,A5,A6,A7,A8)`` in a blank cell.

.. figure:: _static/images/functions/sum/ex4.png
   :scale: 50%

Excel automatically shows the function's parameters underneath the ``=sum(`` to aid the user in finishing
the formula. This helpful dialog box appears every time a function is in use. The results of the sum of
the numbers are shown below.

.. figure:: _static/images/functions/sum/ex5.png
   :scale: 50%

The second way is to use the shortcut ``Alt+=``. 

.. image:: _static/images/functions/sum/ex6.png
   :scale: 50%
.. image:: _static/images/functions/sum/ex8.png
   :scale: 50%

When using the ``Alt+=`` shortcut in the cells of the figures above, note that Excel automatically
recommends the range of cells to add for the user. Observe one of major differences between method one and two.
In the first method, we manually typed in each cell we wanted to calculate. In the second method,
Excel uses a ``:`` to select the start of the sum range to the end of the sum range. The rest of this book
will use a ``:`` when selecting a range of contiguous cells in a formula. 
The two figures below demonstrate using the 
``Alt+=`` shortcut horizontally. 

.. image:: _static/images/functions/sum/ex9.png
   :scale: 50%
.. image:: _static/images/functions/sum/ex10.png
   :scale: 50%

The third way is to click on the sigma button in the Editing section of the Home ribbon. Please note that
doing this produces the same results as the second method above.

.. figure:: _static/images/functions/sum/ex11.png
   :scale: 50%

Average
^^^^^^^

The ``average`` function adds a selection of cells and then divides that sum by the number of cells it added.
Below is the form of the average function. Notice that its form is the same as the ``sum`` function. 

``=average(number1,number2,number3,...)``

The ``average`` function does not have a shortcut. Thus, only methods 1 and 3 for ``sum`` function will work for the 
``average`` function. Start by selecting the cell that will hold the average calculation and type 
``=average(``. Once that has been typed, select the cells that will be included in the calculation. To 
select cells that are not adjacent to one another, press the ``Ctrl`` button and click on the cells to be 
included in the calculation. 

.. image:: _static/images/functions/average/ex1.png
   :scale: 50%
.. image:: _static/images/functions/average/ex2.png
   :scale: 50%

Using method three, select the cell that will hold the average calculation. Click on the down arrow to 
the right of the sigma button and select ``Average``. Just like the ``sum`` function, Excel will recommend
a range of cells to average. It should be noted that even though 9 cells are selected, it will only take 
the average of the 8 cells which contain numbers. It will not calculate the 9th cell.

.. image:: _static/images/functions/average/ex3.png
   :scale: 50%
.. image:: _static/images/functions/average/ex4.png
   :scale: 50%
.. image:: _static/images/functions/average/ex5.png
   :scale: 50%

Count
^^^^^

The ``count`` function evaluates a selection of cells and counts how many of those cells contain numeric values.
``count``, ``max``, and ``min`` have forms just like the functions ``sum`` and ``average``.

``=count(value1,value2,...)``

Using methods 1 and 3 above produces the following results:

.. image:: _static/images/functions/count/ex2.png
   :scale: 50%
.. image:: _static/images/functions/count/ex4.png
   :scale: 50%

.. image:: _static/images/functions/count/ex1.png
   :scale: 50%
.. image:: _static/images/functions/count/ex3.png
   :scale: 50%

Max
^^^

The ``max`` function evaluates a selection of cells and returns the maximum numerical value of those cells.

``=max(number1,number2,...)``

.. image:: _static/images/functions/max/ex1.png
   :scale: 50%
.. image:: _static/images/functions/max/ex2.png
   :scale: 50%

.. image:: _static/images/functions/max/ex3.png
   :scale: 50%
.. image:: _static/images/functions/max/ex4.png
   :scale: 50%

Min
^^^

The ``min`` function evaluates a selection of cells and returns the minimum numerical value of those cells.

``=min(number1,number2,...)``

.. image:: _static/images/functions/min/ex1.png
   :scale: 50%
.. image:: _static/images/functions/min/ex2.png
   :scale: 50%

.. image:: _static/images/functions/min/ex3.png
   :scale: 50%
.. image:: _static/images/functions/min/ex4.png
   :scale: 50%