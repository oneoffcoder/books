Functions
=========

We have been using functions all along. In fact, the ``Hello, world!`` example used the ``print()`` function to print to the terminal. Here, we take an in-depth look at how to create functions. Remember, functions are just verbs or actions, they do something. The basic syntax for defining a function is as follows.

.. code:: python

   def <function_name>(<parameters:optional>):
      # perform logic
      # optional return

The ``<function_name>`` is the name of the function, and the ``<parameters:optional>`` denote variables that are passed into the function. A function may or may not return data. In the case where something is returned back to the caller, a ``return`` command must be used, followed by what is being returned back. The ``print()`` function is an example of a function that does not return anything. 

.. note::
   Naming things is hard in computer science. Typically, variables should be ``nouny`` and functions should be ``verby``. Meaning, variable names should look like nouns and function names should look like verbs.

.. note::
   The values, variables, parameters or arguments that are passed into a function are called ``inputs`` while the item being passed back out through the ``return`` statement is called the ``output``. Typically, a function can have any number of inputs, but only one output. In the case where multiple outputs are required, such outputs are stored in a single data structure such as a list, set, tuple or dictionary.

Basic function
--------------

Your most basic function could just print **Hello, world!**. Notice that there are no variables passed to the function (thare are no variables defined inside the parentheses). Also, nothing is returned from this function (there is no ``return`` statement).

.. code-block:: python
   :linenos:

   def say_hello():
      print('Hello, world!')

To use this function, we simply type in the name followed by parentheses :code:`say_hello()`. Functions are a way to group logic that can be reused. If we want to reuse the function, simply call it again. When we call a function, this usage is sometimes referred to as ``invoking`` the function. When we say use, call or invoke the function, we mean the same thing.

.. code-block:: python
   :linenos:

   def say_hello():
      print('Hello, world!')

   # call the function above twice
   say_hello()
   say_hello()

   # call the function above 10 times using a loop
   # note we use the range() function which generates a range of numbers 
   # from zero up to (and excluding) the specified number
   for _ in range(10):
      say_hello()

Now, we want to modify ``say_hello()`` to accept an argument ``name`` and invoke it 10 times.

.. code-block:: python
   :linenos:

   def say_hello(name):
      print(f'Hello, {name}!')

   # invoke the function once
   say_hello('Sarah')

   # invoke the function many times using a loop
   names = ['John', 'Jack', 'Sam', 'Jeff']

   for name in names:
      say_hello(name)

What if we want to say hello to a person using their first and last name?

.. code-block:: python
   :linenos:

   def say_hello(first_name, last_name):
      print(f'Hello, {first_name} {last_name}!')

   # invoke the function once
   say_hello('Sarah', 'Smith')

   # invoke the function many times using a loop
   names = [('John', 'Smith'), ('Jack', 'Johnson'), ('Sam', 'Smith'), ('Jeff', 'Johnson')]

   for fname, lname in names:
      say_hello(fname, lname)

Exercise
^^^^^^^^

Write a function called ``say_bye()`` that prints ``Bye, world!``. Call this function once and then call this function 20 times.

Solution.

.. code-block:: python
   :linenos:

   def say_bye():
      print('Bye, world!')

   say_bye()

   for _ in range(20):
      say_bye()

Exercise
^^^^^^^^

Write a function to characterize the weather qualitatively based on the temperature (the temperature is a required parameter).

* if the temperature is less than or equal to 60, print **cold**
* else if the temperature is less than or equal to 80, print **cool**
* else if the temperature is less than or equal to 90, print **warm**
* else print **hot**

Solution.

.. code-block:: python
   :linenos:

   def describe_weather(temperature):
      if temperature <= 60.0:
         print(f'{temperature} is cold')
      elif temperature <= 80.0:
         print(f'{temperature} is cool')
      elif temperature <= 90.0:
         print(f'{temperature} is warm')
      else:
         print(f'{temperature} is hot')

   # invoke the function once
   describe_weather(77.7)

   # invoke the function many times using a loop
   temperatures = [30.2, 77.5, 80.2, 101.1]

   for temperature in temperatures:
      describe_weather(temperature)

Function with one arguments
---------------------------

Here are two functions ``add_one()`` and ``minus_one()``. Each of these functions take in a parameter, argument or variable named ``num``. While ``add_one()`` adds one to the passed in integer and returns that result, ``subtract_one()`` subtracts one from the passed in integer and returns that result.

.. literalinclude:: code/oneoffcoder/function/basicfunction.py
   :language: python
   :linenos:
   :emphasize-lines: 1,2,5,6

Exercise
^^^^^^^^

Write two functions.

* ``times_two(num)`` should multiply the passed in number by 2 and return the result
* ``divide_by_two(num)`` should divide the passed in number by 2 and return the result

Invoke these functions for a variety of numbers.

Solution.

.. code-block:: python
   :linenos:

   def times_two(num):
      return num * 2

   def divide_by_two(num):
      return num / 2

   numbers = [32, 17, 8, 5, 18]

   for number in numbers:
      result_1 = times_two(number)
      result_2 = divide_by_two(number)

      print(f'results of passing in {number} to functions are {result_1} and {result_2}')

Exercise
^^^^^^^^

Write a function to characterize the weather qualitatively based on the temperature (the temperature is a required parameter).

* if the temperature is less than or equal to 60, return **cold**
* else if the temperature is less than or equal to 80, return **cool**
* else if the temperature is less than or equal to 90, return **warm**
* else return **hot**

Solution.

.. code-block:: python
   :linenos:

   def describe_weather(temperature):
      if temperature <= 60.0:
         return 'cold'
      elif temperature <= 80.0:
         return 'cool'
      elif temperature <= 90.0:
         return 'warm'
      else:
         return 'hot'

   # invoke the function once
   describe_weather(77.7)

   # invoke the function many times using a loop
   temperatures = [30.2, 77.5, 80.2, 101.1]

   for temperature in temperatures:
      describe_weather(temperature)

Function with two arguments
---------------------------

.. literalinclude:: code/oneoffcoder/function/twoargs.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3

Function with three arguments
-----------------------------

.. literalinclude:: code/oneoffcoder/function/threeargs.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3

Function with a list argument
-----------------------------

.. literalinclude:: code/oneoffcoder/function/listarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3

Function with default value argument
------------------------------------

.. literalinclude:: code/oneoffcoder/function/defaultvalarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3,11

Non-keyworded, variable-length argument
---------------------------------------

.. literalinclude:: code/oneoffcoder/function/nonkeywordedarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2-4,7-9

Keyworded, variable-length argument
-----------------------------------

.. literalinclude:: code/oneoffcoder/function/keywordedarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2-4,7-9

Mixed arguments
---------------

.. literalinclude:: code/oneoffcoder/function/mixedargs.py
   :language: python
   :linenos:
   :emphasize-lines: 2-9

Unpacking tuple return type
---------------------------

.. literalinclude:: code/oneoffcoder/function/unpackingtuple.py
   :language: python
   :linenos:
   :emphasize-lines: 1,2,12