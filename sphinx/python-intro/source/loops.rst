Loops
=====

.. highlight:: python

Loops are used to recycle logic over and over over any number of data or inputs. Without loops, for as many times as you need to apply the same logic to your data, you will have to code (or copy and paste) your logic that many times. Loops are frequently used to ``iterate`` over collections such as lists, sets, tuples and maps. There are two basic loops, the ``while`` and ``for-each`` loops. Let's investigate them further below.

while
-----

The while loop has the following syntax.

.. code-block:: python
   :linenos:

   while <some-condition-is-true>:
      # perform some logic

Below, we loop until the variable ``n`` is equal to or greater than 10. At the end of the block of code under the while loop, we increment ``n`` by one. If we did not increment ``n`` then the termination condition will never be ``False`` and we would loop forever.

.. literalinclude:: code/oneoffcoder/loop/whileloop.py
   :language: python
   :linenos:
   :emphasize-lines: 3-5

You can also loop endless and ``break`` out of a ``while`` loop manually. In the example below, we loop forever since we set :code:`while True:`. However, inside the loop, we check if ``n`` is a multiple of 10, and if so, we issue a ``break`` (a manual termination) of the ``while`` loop.

.. code-block:: python
   :linenos:

   n = 0
   while True:
      print(n)
      n += 1
      if n % 10 == 0:
         break

Exercise
^^^^^^^^

Create a program to keep asking for the user to input something (anything) 5 times. Use a ``while`` loop to help you in this exercise. Inside the loop, simply print back out what the user entered.

Solution.

.. code-block:: python
   :linenos:

   n = 0
   while n < 5:
      user_input = input('enter in anything: ')
      print(f'{user_input}')

Exercise
^^^^^^^^

Create a program using a ``while`` loop to keep asking for the user to input something endlessly. Inside the loop, if the user enters in ``n``, then ``break``. If the user did not enter ``n`` as the input, then echo the user's input back to the terminal.

Solution.

.. code-block:: python
   :linenos:

   while True:
      user_input = input('enter in anything: ')
      
      if user_input == 'n':
         break

      print(f'{user_input}')

for-each
--------

The ``for-each`` loop is best understood when looping over the elements of a collections. To appreciate the power of the ``for-each`` loop, let's see what it would take to print a list of 10 numbers without a ``for-each`` loop.

.. code-block:: python
   :linenos:

   numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

   print(numbers[0])
   print(numbers[1])
   print(numbers[2])
   print(numbers[3])
   print(numbers[4])
   print(numbers[5])
   print(numbers[6])
   print(numbers[7])
   print(numbers[8])
   print(numbers[9])

This approach to printing each number from a list is not scalable if there are a million numbers to print. We need to use the ``for-each`` loop. The syntax of the ``for-each`` loop is as follows.

.. code-block:: python
   :linenos:

   for <element> in <collection>:
      # perform some logic over the element

Basic for-each
^^^^^^^^^^^^^^

Here are some examples of using a ``for-each`` loop against different types of collections.

.. literalinclude:: code/oneoffcoder/loop/foreach.py
   :language: python
   :linenos:
   :emphasize-lines: 4-5,10-11,16-17,26-27


Exercise
^^^^^^^^

Loop through each number in the list below and print the number and what the number times 2 would be.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Solution.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   for number in numbers:
      n = number * 2
      print(f'{number} x 2 = {n}')

Exercise
^^^^^^^^

Loop through each number in the list below and print the number and what the number times 2 would be only if the number is even.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Solution.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   for number in numbers:
      if number % 2 == 0:
         n = number * 2
         print(f'{number} x 2 = {n}')

Exercise
^^^^^^^^

Loop through each number in the list below and print the number and what the number times 3 would be only if the number times 3 is odd.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Solution.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   for number in numbers:
      n = number * 3
      if n % 2 != 0:
         print(f'{number} x 3 = {n}')

Exercise
^^^^^^^^

Loop through each key-value pair in the following dictionary. Since the values are tuples, loop through each element in the tuple and print them.

.. code-block:: python
   :linenos:

   data = {
      'fred': (28, 150.5, 5.5),
      'john': (32, 180.2, 6.2)
   }

Solution.

.. code-block:: python
   :linenos:

   data = {
      'fred': (28, 150.5, 5.5),
      'john': (32, 180.2, 6.2)
   }

   for key, tup in data.items():
      for item in tup:
         print(item)

for-each with break
^^^^^^^^^^^^^^^^^^^

Breaking is also possible inside a for-each loop.

.. literalinclude:: code/oneoffcoder/loop/foreachbreak.py
   :language: python
   :linenos:
   :emphasize-lines: 3-6

Exercise
^^^^^^^^

Loop through the following list and break after the third odd number is encountered.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Solution.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   total_odds = 0

   for number in numbers:
      if number % 2 != 0:
         total_odds += 1
      if total_odds == 3:
         break

for-each with continue
^^^^^^^^^^^^^^^^^^^^^^

When used inside a ``for-each`` or ``while`` loop, the ``continue`` command forces the logic back to the start of the code block inside the loop; all code below the ``continue`` are skipped. The code below iterates through each integer a list and skips printing the integer if it is odd.

.. literalinclude:: code/oneoffcoder/loop/foreachcontinue.py
   :language: python
   :linenos:
   :emphasize-lines: 5

Exercise
^^^^^^^^

Loop through the following list of names and skip printing names that do not start with a ``j``. Use the ``continue`` command to achieve this request.

.. code-block:: python
   :linenos:

   names = ['jane', 'mary', 'josephine', 'nancy']

Solution.

.. code-block:: python
   :linenos:

   names = ['jane', 'mary', 'josephine', 'nancy']

   for name in names:
      if not name.startswith('j'):
         continue
      print(name)

for-each with enumeration
^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes, we want to access the corresponding index of an element as we are iterating through a collection. To get the index and element, we can pass the collection to the ``enumerate()`` function.

.. literalinclude:: code/oneoffcoder/loop/foreachenum.py
   :language: python
   :linenos:
   :emphasize-lines: 3

Note that ``enumerate()`` will return a tuple, and so we can loop over the elements as follows.

.. code-block:: python
   :linenos:

   numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   for tup in enumerate(numbers):
      print(tup[0], tup[1])

Or, we can unpack the tuple inside the ``for-each`` loop.

.. code-block:: python
   :linenos:

   numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   for tup in enumerate(numbers):
      i, number = tup
      print(i, number)

Typically, we prefer to unpack the tuple with the ``for-each`` loop as :code:`for i, numbers in enumerate(numbers):`.

If we did not want to start the index at 0, then we can specify a starting index as follows.

.. code-block:: python
   :linenos:

   numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   for i, number in enumerate(numbers, 10):
      print(i, number)

   # the code above will print
   # 10 0
   # 11 1
   # 12 2
   # and so on ...

Exercise
^^^^^^^^

Loop through the following list of names and print the name only if the name starts with a ``j`` and the associated index is odd.

.. code-block:: python
   :linenos:

   names = ['jane', 'mary', 'josephine', 'jack', 'nancy']

Solution.

.. code-block:: python
   :linenos:

   names = ['jane', 'mary', 'josephine', 'jack', 'nancy']

   for i, name in enumerate(names):
      if name.startswith('j') and i % 2 != 0:
         print(name)

Looping over two lists
^^^^^^^^^^^^^^^^^^^^^^

What if we want to iterate over 2 collections at the same time? We can use the ``zip()`` function. ``zip()`` aligns the elements from 2 or more lists and creates a tuple for each aligned elements. We can create a list from zipping two lists as follows.

.. code-block:: python
   :linenos:

   names = ['Jack', 'John', 'Joe']
   ages = [18, 19, 20]

   persons = list(zip(names, ages))
   print(persons)

   # should print [('Jack', 18), ('John', 19), ('Joe', 20)]

The example below show the use of using a ``for-each`` loop with ``zip()``. Note how we unpack the tuple elements generated by ``zip()``.

.. literalinclude:: code/oneoffcoder/loop/foreachzip.py
   :language: python
   :linenos:
   :emphasize-lines: 4

Exercise
^^^^^^^^

Loop over the two lists below simultaneously using ``zip()`` and print the name and age only if the age is even.

.. code-block:: python
   :linenos:

   names = ['Jack', 'John', 'Joe']
   ages = [18, 19, 20]

Solution.

.. code-block:: python
   :linenos:

   names = ['Jack', 'John', 'Joe']
   ages = [18, 19, 20]

   for name, age in zip(names, ages):
      if age % 2 == 0:
         print(f'{name}, {age}')

Looping with enumerate and zip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can combine ``enumerate()`` with ``zip()`` as follows.

.. code-block:: python
   :linenos:

   names = ['Jack', 'John', 'Joe']
   ages = [18, 19, 20]
   persons = list(enumerate(zip(names, ages)))
   print(persons)

   # the above should print [(0, ('Jack', 18)), (1, ('John', 19)), (2, ('Joe', 20))]
   # note the result is a list of tuples, where each tuple has the index in the first
   # position and a tuple in the second position

Here is how we can use ``enumerate()`` with ``zip()`` with a ``for-each`` loop.

.. literalinclude:: code/oneoffcoder/loop/foreachenumzip.py
   :language: python
   :linenos:
   :emphasize-lines: 4

Exercise
^^^^^^^^

Loop through both lists below. Only print the name and age if the name starts with a ``J``, the index is odd and the age is odd.

.. code-block:: python
   :linenos:

   names = ['Mary', 'Jack', 'John', 'Nancy', 'Sam', 'Jeremy', 'Mark']
   ages = [18, 19, 21, 24, 26, 27, 32]

.. code-block:: python
   :linenos:

   names = ['Mary', 'Jack', 'John', 'Nancy', 'Sam', 'Jeremy', 'Mark']
   ages = [18, 19, 21, 24, 26, 27, 32]

   for i, (name, age) in enumerate(zip(names, ages)):
      if i % 2 != 0 and age % 2 != 0 and name.startswith('J'):
         print(f'{i}, {name}, {age}')

Comprehension
-------------

Comprehensions are a way to transform an existing collection into a new one using the ``for-each`` loop. There are comprehensions to generate lists, sets and dictionaries.

List comprehension
^^^^^^^^^^^^^^^^^^

The ``list comprehension`` has the following syntax: :code:`[<expression> for <element> in <collection> <filter:optional>]`. The ``<expression>`` is required and the ``<filter:optional>`` is optional. The ``<expression>`` is typically a transformation of the ``<element>``. Let's say we have a list :code:`numbers = [1, 2, 3, 4]` and we want to transform this list into a new one where each element is multiplied by two. We can use a regular ``for-each`` loop or a list comprehension. 

.. literalinclude:: code/oneoffcoder/loop/listcomprehension.py
   :language: python
   :linenos:
   :emphasize-lines: 9

An example of using a filter is as follows. In this example, we transform each integer to a new number by multiplying it by 3 and we filter for for only odd-indexed numbers.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   nums = [number * 3 for i, number in numbers if i % 2 != 0]

Exercise
^^^^^^^^
Transform the list below into a new one with all boolean values, where each element in the new list indicates if the corresponding element in the existing list is even ``True`` or odd ``False``.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   nums = [True if number % 2 == 0 else False for number in numbers]


Nested list comprehension
^^^^^^^^^^^^^^^^^^^^^^^^^

List comprehensions can also be nested as in the example below. Note that we have a list of lists, which represents a two-dimensional matrix. So we have to iterate over the rows and then the columns in that row. The result is that we end up with a ``flattened`` list (the new list is not like the first list, which is a list of lists).

.. literalinclude:: code/oneoffcoder/loop/nestedlistcomprehension.py
   :language: python
   :linenos:
   :emphasize-lines: 3

Exercise
^^^^^^^^

Flatten the matrix below using a nested list comprehension, but, only include those elements whose row and column indices are equal.

.. code-block:: python
   :linenos:

   matrix = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

Solution.

.. code-block:: python
   :linenos:

   matrix = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
   diagonal = [col for i, row in enumerate(matrix) for j, col in enumerate(row) if i == j]

Set comprehension
^^^^^^^^^^^^^^^^^

``Set comprehensions`` are just like list comprensions, except, instead of using ``[]`` to setup the comprehension, we use ``{}``. The ``set comprehension`` has the following syntax: :code:`{<expression> for <element> in <collection> <filter:optional>}`.

.. literalinclude:: code/oneoffcoder/loop/setcomprehension.py
   :language: python
   :linenos:
   :emphasize-lines: 9

Exercise
^^^^^^^^

Find all the unique odd numbers in the following list of numbers.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 2, 3, 5, 1, 1]

Solution.

.. code-block:: python
   :linenos:

   numbers = [1, 2, 3, 4, 5, 2, 3, 5, 1, 1]
   nums = {number for number in numbers if number % 2 != 0}

Dictionary comprehension
^^^^^^^^^^^^^^^^^^^^^^^^

A ``dictionary comprehension`` is used to generate a new dictionary. The ``dictionary comprehension`` has the following syntax: :code:`{<key>: <expression> for <element> in <collection> <filter:optional>}`.

.. literalinclude:: code/oneoffcoder/loop/dictionarycomprehension.py
   :language: python
   :linenos:
   :emphasize-lines: 12

Exercise
^^^^^^^^

Below is a list of names. Note that the elements are tuples, where the first element in the tuple is the first name and the second element is the last name. Transform the list into a dictionary where they key is the initials of each name and the corresponding value is the full name.

.. code-block:: python
   :linenos:

   names = [('Jack', 'Washington'), ('John', 'Doe'), ('Joe', 'Black'), ('Mary', 'Swanson')]

Solution.

.. code-block:: python
   :linenos:

   names = [('Jack', 'Washington'), ('John', 'Doe'), ('Joe', 'Black'), ('Mary', 'Swanson')]
   persons = {f'{fname[0]}.{lname[0]}.': f'{fname} {lname}' for fname, lname in names}
   print(persons)

   # should print {'J.W.': 'Jack Washington', 'J.D.': 'John Doe', 'J.B.': 'Joe Black', 'M.S.': 'Mary Swanson'}

Generator comprehension
^^^^^^^^^^^^^^^^^^^^^^^

With list, set and dictionary comprehensions, the resulting data is evaluated and created immediately. The ``generator comprehension``, however, only evaluates the expression as needed. The former comprehensions are ``eagerly`` evaluated and the latter comprehension is ``lazily`` evaluated. If we need to generate a new collection that does not need to be stored, use a generator comprehension as intermediary results will not be stored. The syntax for a generator comprehension is nearly identical to the list comprehension, except that we use ``()`` instead of ``[]``: :code:`(<expression> for <element> in <collection> <filter:optional>)`

.. literalinclude:: code/oneoffcoder/loop/generatorcomprehension.py
   :language: python
   :linenos:
   :emphasize-lines: 7

Exercise
^^^^^^^^

Write a program to ask the user to input a number over and over (until the user requests to quit by entering ``q`` to quit). Each time a user enters a number, whatever that number is, compute the list of numbers that results when multiplying it by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. 

Solution.

.. code-block:: python
   :linenos:

   # we use a tuple for the collection
   # why? because we do not want this collection to ever be modified
   # we define this collection of numbers outside the while loop
   # why? because we only need to define it once, not over and over inside the loop
   multipliers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

   while True:
      user_input = input('enter a number or "q" to quit: ')

      if user_input == 'q':
         break
      
      num = int(user_input)
      numbers = [n * num for n in multipliers]
      print(numbers)
