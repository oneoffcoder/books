Control Statements
==================

Control statements are also called ``if/else`` statements or ``conditional`` statements. These types of statements control the flow of your program based on boolean logic, expressions, values, evaluations or outcomes. The ``intelligence`` in computational intelligence, machine learning or artificial intelligence are based on these control statements. For example, an **intelligent** self-driving car may have a control flow as follows:

* if the traffic light is yellow, then slow down
* if the traffic light is red, then stop
* if the traffic light is green, then go

Control statements are how computers (and, most likely, even humans) make categorical decisions and take actions based upon those decisions.

.. highlight:: python

if
--

The most basic form of ``if/else`` statements comes when you are only using ``if``. Below, you have the state of the traffic light (which is yellow), and you want to test to see if the traffic light is yellow. If the traffic light is yellow, you print **slow down**.

.. literalinclude:: code/oneoffcoder/control/if.py
   :language: python
   :linenos:
   :emphasize-lines: 3

There is a lot going on with just this simple if/else statement. First, note that after ``if`` we have a comparison that evaluates to true or false: :code:`traffic_light == 'yellow'`. This comparison is using the **equality comparison operator** ``==`` which must evaluate to ``True`` or ``False``. The way to read this comparison naturally is: is the traffic light yellow? 

Second, note the use of the block operator ``:`` after the comparison. This block operator signals that a **block of code** is going to follow. A block of code is just a sequential set of statements that are indented at the same level. Which leads us to the third point.

Third, did you observe that we **indented** the ``print`` statement in the next line following the ``if`` statement? This indentation says that the print statement belongs to the ``if`` statement. Only if the comparison evaluates to ``True`` do we execute the print statement. If we did not indent the print statement, then there is nothing to do if the traffic light is yellow, and this is also a syntax error.

.. code-block:: python
   :linenos:

   traffic_light = 'yellow'

   # not having a block of statement below if results in an error
   if traffic_light == 'yellow':

If we did not know yet what to do if the traffic light is yellow, then we can use the ``pass`` keyword under the ``if`` statement.

.. code-block:: python
   :linenos:

   traffic_light = 'yellow'

   # using pass under if is ok, if we do not yet know what to do
   if traffic_light == 'yellow':
      pass

If we needed to do multiple things when the traffic light is yellow, we can supply multiple statements.

.. code-block:: python
   :linenos:

   traffic_light = 'yellow'

   if traffic_light == 'yellow':
      print('take foot off accelerator pedal')
      print('start pressing on brake pedal')
      print('stay focused')
      
Exercise
^^^^^^^^

We have the state of the weather, which can be rainy or sunny.

* If it is rainy, then we must advise a person to wear a rain jacket.
* If it is sunny, then we must advise a person to wear shorts.

Write simple programs to store the weather's state and a simple ``if/else`` statement to advise a person what to do.

Solution.

.. code-block:: python
   :linenos:

   weather = 'rainy'

   if weather == 'rainy':
      print('wear a rain jacket')

.. code-block:: python
   :linenos:

   weather = 'sunny'

   if weather == 'sunny':
      print('wear shorts')

if-else
-------

When we are testing a condition, we know we can provide a block of statements for the computer to do if that condition evaluates to ``True``. But what if the condition evaluates to ``False`` and we still want to provide a block of statements for the computer to do? How do we write an ``if/else`` statement for this case? 

Below, we have two integers ``a`` and ``b``, and we want to do something when ``a`` is greater than ``b`` and something else when that condition fails (evaluates to ``False``). This situation would require us to combine the ``else`` statement with the ``if``.

.. note::
   Notice how the ``else`` comes after the ``if``? Notice also how the ``else`` is followed by a ``:``? Lastly, the ``else`` does not need any boolean expression to be evaluated. The ``else`` part of the ``if-else`` statement is called the ``catch-all`` case.

.. literalinclude:: code/oneoffcoder/control/ifelse.py
   :language: python
   :linenos:
   :emphasize-lines: 4,6

In an ``if-else`` statement, when the condition in the ``if`` part evaluates to true, the code block underneath it is executed and the code block under the ``else`` is ignored. Likewise, when the condition in the ``if`` part evaluates to false, the code block underneath it is ignored and the code block under the ``else`` is executed.

Exercise
^^^^^^^^

Write a program to instruct the user to wear a rain coat and bring an umbrella if the weather is rainy, otherwise, to wear shorts and sunglasses if it's sunny.

.. code-block:: python
   :linenos:

   weather = 'rainy'

Solution.

.. code-block:: python
   :linenos:

   weather = 'rainy'

   if weather == 'rainy':
      print('wear rain jacket')
      print('bring umbrella')
   else:
      print('wear shorts')
      print('wear sunglasses')

We could of tested for sunny weather too.

.. code-block:: python
   :linenos:

   weather = 'rainy'

   if weather == 'sunny':
      print('wear shorts')
      print('wear sunglasses')
   else:
      print('wear rain jacket')
      print('bring umbrella')

if-elif-else
--------------

We can test for multiple conditions using ``if-elif-else``. The ``elif`` is Python's way of saying **else if**.

.. literalinclude:: code/oneoffcoder/control/ifelifelse.py
   :language: python
   :linenos:
   :emphasize-lines: 3,5,7

In an ``if-else`` statement, the ``if`` must always come first, the ``else`` must always come last, the ``elif`` must always be in the middle and we can have any number of ``elif``. Look at the example below.

.. code-block:: python
   :linenos:

   a = 9

   if a < 5:
      print('a < 5')
   elif a < 10:
      print('a < 10')
   elif a < 15:
      print('a < 15')
   elif a < 20:
      print('a < 20')
   else:
      print('a >= 20')

Exercise
^^^^^^^^

A percentage score on a test will be assigned a letter grade according to the following.

* [100, 90] is A
* [89, 80] is B
* [79, 70] is C
* [69, 60] is D
* [59, 0] is F

A person has a 84 on a test. Write a ``if-else`` statement to assign (or map) this score to a letter grade.

- Hint: use boolean logic

Solution.

.. code-block:: python
   :linenos:

   score = 84

   if score <= 100 and score >= 90:
      print('A')
   elif score <= 89 and score >= 80:
      print('B')
   elif score <= 79 and score >= 70:
      print('C')
   elif score <= 69 and score >= 60:
      print('D')
   else:
      print('F')

Multiple comparison in if-else
------------------------------

When evaluating conditions, you can use multiple comparisons to test for ``True`` or ``False``.

.. literalinclude:: code/oneoffcoder/control/multicompare.py
   :language: python
   :linenos:
   :emphasize-lines: 3,5

Exercise
^^^^^^^^

Modify the code below to use multiple comparison instead of boolean logic.

.. code-block:: python
   :linenos:

   score = 84

   if score <= 100 and score >= 90:
      print('A')
   elif score <= 89 and score >= 80:
      print('B')
   elif score <= 79 and score >= 70:
      print('C')
   elif score <= 69 and score >= 60:
      print('D')
   else:
      print('F')

Solution.

.. code-block:: python
   :linenos:

   score = 84

   if 90 <= score <= 100:
      print('A')
   elif 80 <= score <= 89:
      print('B')
   elif 70 <= score <= 79:
      print('C')
   elif 60 <= score <= 69:
      print('D')
   else:
      print('F')

Nested if-else
--------------

``if-else`` statements could also be nested as shown below.

.. literalinclude:: code/oneoffcoder/control/nestedifelse.py
   :language: python
   :linenos:
   :emphasize-lines: 8-11

.. warning::
   Nested ``if-else`` statements produces `cyclomatic complexity <https://en.wikipedia.org/wiki/Cyclomatic_complexity#:~:text=Cyclomatic%20complexity%20is%20a%20software,in%201976.>`_. Try to stay away from nested ``if-else`` statements when possible.

Exercise
^^^^^^^^

For some reason, John likes to do certain sports dependent on what the weather is like and what the day is. John looks at the weather in terms of sunny or rainy, and he looks at the day in terms of whether it's odd or even. 

* If it's sunny and an even numbered day, John likes play basketball.
* If it's sunny and an odd numbered day, John likes play baseball.
* If it's rainy and an even numbered day, John likes play football.
* If it's rainy and an odd numbered day, John likes play soccer.

Write a program to tell John what to do if the given weather and day is specified.

.. code-block:: python
   :linenos:

   weather = 'sunny'
   day = 2

Solution.

.. code-block:: python
   :linenos:

   weather = 'sunny'
   day = 2
   is_even = day % 2 == 0

   if weather == 'sunny' and is_even:
      print('basketball')
   elif weather == 'sunny' and not is_even:
      print('baseball')
   elif weather == 'rainy' and is_even:
      print('football')
   else:
      print('soccer')
