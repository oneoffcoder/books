Exceptions
==========

Coding is an error-prone activity. It is difficult to anticipate when something might go wrong, and even if we could anticipate problems, it is equally, if not more, difficult to decide what to do when something does go wrong. In Python, we can use ``try-except-finally`` or just ``try-except`` to handle problems that might occur. Generally speaking, there are two types of problems that will bring your program to a grinding halt: ``errors`` and ``exceptions``. Errors cannot be handled, but exceptions can be handled (handle by our code). Let's look at some examples of how to use ``try-except`` to handle problems.


.. highlight:: python

Divide by zero
--------------

In math, any (positive) number divided by zero results in infinity. In Python, if you attempt to divide a number by zero, an ``exception`` will be thrown. An exception is just a very specific signal indicating that something has gone wrong. The particular exception thrown when attempting to divide a number by zero will be a ``ZeroDivisionError`` type of exception. Once an exception is thrown, your code will crash altogether at that very point.

.. code-block:: python
   :linenos:

   10 / 0 # ZeroDivisionError thrown
   print('hello, world') # we will never reach this statement

You can use ``try-except`` to attempt to ``catch`` the exception and handle it as appropriate. Below, we simply print an informative message that the denominator is zero.

.. literalinclude:: code/oneoffcoder/exception/dividebyzero.py
   :language: python
   :linenos:
   :emphasize-lines: 7,11

If we wanted to capture the details of the exception, we can use the ``as`` keyword to alias the exception as a variable.


.. code-block:: python
   :linenos:

   try:
      a = 20
      b = 0
      c = a / b
   except ZeroDivisionError as zde:
      print(f'error: {zde}')

Many times, we just want a quick and dirty way to handle exceptions or we do not really know what types of exceptions will be thrown. In these cases, we can omit the exception type.

.. code-block:: python
   :linenos:

   try:
      a = 20
      b = 0
      c = a / b
   except:
      print(f'something went wrong')

The ``finally`` block is always guaranteed to run in a ``try-catch`` statement. The ``catch`` block is only executed if the particular exception we are trying to catch is thrown. Only one ``catch`` block will ever be executed since as soon as an exception is thrown, your program will break (exceptions are thrown one at a time). In the example below, we attempt to divide **a** by **b**. We initialize **c** to ``None``. If there is a division by zero exception, we simply log it (print out the fact that such thing has happened). Since **c** must always have a valid integer value, the ``finally`` block checks to see if **c** is set, and if not, sets it to **-1**.

.. code-block:: python
   :linenos:

   a = 20
   b = 0
   c = None
      
   try:
      c = a / b
   except:
      print(f'something went wrong')
   finally:
      c = -1 if c is None else c

Accessing invalid index
-----------------------

An ``IndexError`` will be thrown when we attempt to access an element by an index that is outside the bounds of the list indices. 

.. literalinclude:: code/oneoffcoder/exception/accessinvalidindex.py
   :language: python
   :linenos:
   :emphasize-lines: 10

Accessing invalid key
---------------------

A ``KeyError`` will be thrown when we attempt to access a value with a key that does not exists in a dictionary.

.. literalinclude:: code/oneoffcoder/exception/accessinvalidkey.py
   :language: python
   :linenos:
   :emphasize-lines: 13

Accessing invalid key
---------------------

We can catch multiple types of exceptions. In the example below, we have a dictionary where the keys are car makes and the associated values are models. If we attempt to use a key that does not exists in the dictionary, a ``KeyError`` will be thrown, and if we attempt to use an index that is out of bounds for the list, an ``IndexError`` will be thrown. 

.. literalinclude:: code/oneoffcoder/exception/multipleexceptions.py
   :language: python
   :linenos:
   :emphasize-lines: 22,24

Raising an exception
--------------------

We can also throw or raise an exception.

.. literalinclude:: code/oneoffcoder/exception/raiseexception.py
   :language: python
   :linenos:
   :emphasize-lines: 14,22

``ValueError`` is the appropriate exception type to throw when an argument has the right type but wrong value. In the example below, we have a method to compute the area of a square. Note that the side of a square must always be positive. We need to check to see if the side passed into the method is valid; if it's not valid, then an exception should be thrown.

.. code-block:: python
   :linenos:

   def get_area(side):
      if side < 1:
         raise ValueError(f'{side} is not greater than zero.')
      return side * side

   print(get_area(10))
   print(get_area(-10))

Exercise
^^^^^^^^

John and Jack took some tests. Jack missed the first test and so there was no score reported for that test. A function to compute the average score of a list of scores was written as below. Modify this code to handle the exception as a result of summing over a list of numbers (scores) with possibly invalid data types.

.. code-block:: python
   :linenos:

   def get_average(grades):
      total = sum(grades)
      n = len(grades)
      average = total / n
      return average

   john = [88, 90, 85, 100]
   jack = [None, 88, 100, 100]

   print(get_average(john))
   print(get_average(jack))

Solution.

.. code-block:: python
   :linenos:

   def get_average(grades):
      try:
         total = sum(grades)
         n = len(grades)
         average = total / n
         return average
      except TypeError:
         valid_grades = [g for g in grades if isinstance(g, int)]
         return get_average(valid_grades)

   john = [88, 90, 85, 100]
   jack = [None, 88, 100, 100]

   print(get_average(john))
   print(get_average(jack))

User-defined exceptions
-----------------------

We can define our own exceptions by extending the ``Exception`` class. All built-in Python exceptions inherits from ``Exception``, however, they all have the word ``Error`` as a part of their names (e.g. ``IndexError``, ``KeyError``, ``ValueError``, etc.). This naming convention is a bit confusing as errors cannot be handled (but exceptions can) and if the root class is ``Exception`` why not have that word as a part of the name instead of ``Error`` (e.g. ``IndexException``).

.. code-block:: python
   :linenos:

   class NegativeValueError(Exception):
      def __init__(self, value):
         self.value = value
         super().__init__(f'{value} is negative.')

   def get_area(side):
      if side < 1:
         raise NegativeValueError(side)
      return side * side

   print(get_area(10))
   print(get_area(-10))


Exercise
^^^^^^^^
Write a function to generate random dimensions for a triangle, square and rectangle. The dimensions (e.g. base, height, width, length) should be in the range [1, 10]. The function should return a dictionary that looks like the following.

* :code:`{'shape': 'triangle', 'dimensions': [4, 10]}`
* :code:`{'shape': 'square', 'dimensions': [2]}`
* :code:`{'shape': 'rectangle', 'dimensions': [8, 7]}`

If a user requests a random circle, throw an ``InvalidShapeError`` (you have to create a new exception type). Invoke this new function passing in randomly a request for triangle, square, rectangle and circle.

Solution.

.. code-block:: python
   :linenos:

   from random import randint, choice

   class InvalidShapeError(Exception):
      def __init__(self, shape):
         self.shape = shape
         super().__init__(f'{shape} is invalid.')

   def get_shape(shape):
      shapes = {
         'triangle': 2,
         'square': 1,
         'rectangle': 2
      }

      if shape not in shapes:
         raise InvalidShapeError(shape)

      return {
         'shape': shape,
         'dimensions': [randint(1, 10) for _ in range(shapes[shape])]
      }

   all_shapes = ['triangle', 'square', 'rectangle', 'circle']

   for _ in range(10):
      try:
         shape = get_shape(choice(all_shapes))
         print(shape)
      except InvalidShapeError as ise:
         print(f'Problem: {ise}')
