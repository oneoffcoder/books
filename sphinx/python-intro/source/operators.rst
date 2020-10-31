Operators
=========

.. highlight:: python

Basic arithmetic operators 
--------------------------

When dealing with integers and floats, you can apply the following basic math operators.

.. literalinclude:: code/oneoffcoder/operator/mathop.py
   :language: python
   :linenos:

Pay attention to the multiplication and division operators, as they are ``*`` (asterisk) and ``/`` (forward slash), correspondingly. Also, there are 3 ways to divide using ``/``, ``//`` and ``%``. 

* ``/`` gives you a real number (decimal)
* ``//`` gives you the quotient
* ``%`` gives you the remainder

Exercise
^^^^^^^^

For the following 2 variables,

* print what is a + b?
* print what is a - b?
* print what is a x b?
* print what is a ÷ b?

.. code-block:: python
   :linenos:

   a = 17
   b = 5

Solution.

.. code-block:: python
   :linenos:

   print(f'{a} + {b} = {a + b}')
   print(f'{a} - {b} = {a - b}')
   print(f'{a} * {b} = {a * b}')
   print(f'{a} / {b} = {a / b}')

Exercise
^^^^^^^^

Can you express 4 divided by 3 in terms of an improper fraction?

Solution.

.. code-block:: python
   :linenos:

   dividen = 4
   divisor = 3
   quotient = dividen // divisor
   remainder = dividen % divisor

   s = f'{dividen} / {divisor} = {quotient} and {remainder}/{divisor}'
   print(s)

Compound assignment operators 
-----------------------------

If you had an integer variable, and wanted to add a number to it and reassign the result back to itself, how would you do so? Here's a way.

.. code-block:: python
   :linenos:

   a = 15
   a = a + 2 # add 2 to a, and assign the result back to a

A shorter way of expressing this operation is through using a compound assignment operator.

.. code-block:: python
   :linenos:

   a = 15
   a += 2

Here are other types of compound assignment operators.

.. literalinclude:: code/oneoffcoder/operator/compound.py
   :language: python
   :linenos:

Exercise
^^^^^^^^

Let's say you have someone's age. 

* What is the person's age in 10 years?
* What's the person's age 2 years ago from the previous result?
* What's double the person's age from the previous result?
* What's half the person's age from the previous result?

.. code-block:: python
   :linenos:

   age = 15

Solution.

.. code-block:: python
   :linenos:

   age += 10
   print(f'age: {age}')

   age -= 2
   print(f'age: {age}')

   age *= 2
   print(f'age: {age}')

   age /= 2
   print(f'age: {age}')

Bitwise operators 
-----------------

All data is represented as a list of bits. A bit is just a space in the computer's memory that can store the value ``0`` or ``1``. As a first step to understanding bits, it makes a lot of sense to understand representations of integers through bits. In Python, integers are represented with 32 bits. Since 1 byte is equal to 8 bits, an integer is said to use 4 bytes (or 32 bits). When we declare and initialize an integer variable, Python finds contiguous spaces in memory (32 bits or 4 bytes) to store the representation of the value. For example, the number 8 is represented as: ``0000000000001000``. The number 8 is said to be in decimal form and the number ``0000000000001000`` is said to be in binary form; they are equivalent, but using different representation schemes. Bitwise operators work to manipulate these bits.

If 8 in decimal is represented as ``0000000000001000``, then the bitwise not ``~``, when applied to the decimal number, changes the bits to be ``1111111111110111``, and the resulting decimal is -9. Note that ``~`` flips all 0 bits to 1 and all 1 bits to 0. Here's a cheat sheet on the bitwise operators.

* ``~`` reverses the bit (0 is turned to 1, 1 is turned to 0)
* ``|`` if either bit is 1, then 1, else 0
* ``&`` if both bits are 1, then 1, else 0
* ``^`` if one or the other bit is 1, then 1, else 0
* ``<<`` shifts the bits to the left (padding zeros to the right)
* ``>>`` shifts the bits to the right (padding zeros to the left)

.. literalinclude:: code/oneoffcoder/operator/bitwise.py
   :language: python
   :linenos:

Exercise
^^^^^^^^

What is the result of 16

* shifted by 1 bit to the left?
* shifted by 2 bits to the left?
* shifted by 3 bits to the left?
* shifted by 1 bit to the right?
* shifted by 2 bits to the right?
* shifted by 3 bits to the right?

Solution.

.. code-block:: python
   :linenos:

   print(16 << 1) # 32
   print(16 << 2) # 64
   print(16 << 3) # 128
   print(16 >> 1) # 8
   print(16 >> 1) # 4
   print(16 >> 1) # 2

Relational operators 
--------------------

Relational operators are also called ``comparison operators``. These operators compare two things and the evaluation of the comparison must always be ``True`` or ``False``. 

.. literalinclude:: code/oneoffcoder/operator/relational.py
   :language: python
   :linenos:

Exercise
^^^^^^^^

You have the ages of Jack, John, Mary and Jane.

* Is Jack older than John?
* Is Jack younger than Mary?
* Is Jack's age equal to Jane?

.. code-block:: python
   :linenos:

   jack = 28
   john = 35
   mary = 24
   jane = 28

Solution.

.. code-block:: python
   :linenos:

   # is jack older than john?
   print(jack > john)

   # is jack younger than mary?
   print(jack < mary)

   # is jack equal to jane?
   print(jack == mary)

Boolean logical operators 
-------------------------

You can chain boolean values or comparisons to evaluate to True or False using boolean logical operators. The following are examples of such operators.

.. literalinclude:: code/oneoffcoder/operator/booleanlogical.py
   :language: python
   :linenos:

.. note::
   When you have a boolean expression with all boolean ``and``, this expression is called a ``conjunction``. When you have a boolean expression with all boolean ``or``, this expression is called a ``disjunction``. In a conjunction, all sub-expressions or evaluations must be true for the overall evaluation to be true. In a disjunction, only 1 sub-expression must be true for the overall evaluation to be true. 
   
   Here's some examples of conjunctions :code:`True and True and True` and :code:`True and True and False and True`. The first conjunction evaluates to true since all sub-expressions are true. The second conjunction evaluates to false since one of the sub-expression is false.

   Here's some examples of disjunctions :code:`True or False or True or False` and :code:`False or False`. The first disjunction evaluates to true since at least one of the sub-expression is true. The second disjunction evaluates to false since none of the sub-expressions are true.

Exercise
^^^^^^^^

You have the ages of Jack, John, Mary and Jane.

* Is Jack older than John or Mary?
* Is Jack younger than Mary and Jane?
* Is Jack's age equal to Jane and less than John?

.. code-block:: python
   :linenos:

   jack = 28
   john = 35
   mary = 24
   jane = 28

Solution.

.. code-block:: python
   :linenos:

   # is jack older than john or mary?
   print(jack > john or jack > mary)

   # is jack younger than mary and jane?
   print(jack < mary and jack < jane)

   # is jack equal to jane and less than john?
   print(jack == mary and jack < john)

Parentheses
-----------

Parentheses can be used in math operations to give priority to which operations to do first. Look at the examples below. There is a difference between :code:`4 + 2 * 2` versus :code:`(4 + 2) * 2`.

.. literalinclude:: code/oneoffcoder/operator/parentheses.py
   :language: python
   :linenos:

List unpacking
--------------

We have talked about unpacking tuples, but lists may also be unpacked.

.. literalinclude:: code/oneoffcoder/operator/listunpacking.py
   :language: python
   :linenos:
   :emphasize-lines: 6

Just as in unpacking values from tuples, when we unpack values from a list, we can use ``_`` to ignore values or ranges of values.

.. literalinclude:: code/oneoffcoder/operator/listunpackingignoring.py
   :language: python
   :linenos:
   :emphasize-lines: 5

We can also use list unpacking to merge two lists as follows.

.. literalinclude:: code/oneoffcoder/operator/mergelistviaunpacking.py
   :language: python
   :linenos:
   :emphasize-lines: 4

Note that you do not have to unpack lists to merge their elements into one list. You can simply use the ``+`` operator to merge the elements of two lists as follows.

.. code-block:: python
   :linenos:

   boys = ['John', 'Jack', 'Jeremy']
   girls = ['Mary', 'Nancy', 'Joyce']
   names = boys + girls

Merging dictionaries via unpacking
----------------------------------

If you want to merge the key-value pairs of 2 maps/dictionaries, use the ``**`` operator as follows.

.. literalinclude:: code/oneoffcoder/operator/mergedictionaryviaunpacking.py
   :language: python
   :linenos:
   :emphasize-lines: 9

Exercise
^^^^^^^^

There are four major competitions, called ``slams``, in tennis: Australian Open, French Open, Wimbledon and US Open. The results (data) below are how many times Roger Federer has won each one. Combine these individual results at the slams into one map (dictionary).

.. code-block:: python
   :linenos:

   australian_slam = {'australian': 6}
   french_slam = {'french': 1}
   wimbledon_slam = {'wimbledon': 8},
   us_slam = {'us': 5}

Solution.

.. code-block:: python
   :linenos:

   slams = {**australian_slam, **french_slam, **wimbledon_slam, **us_slam}
   print(slams)
