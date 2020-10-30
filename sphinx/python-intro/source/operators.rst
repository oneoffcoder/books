Operators
=========

.. highlight:: python

Basic arithmetic operators 
--------------------------

When dealing with integers and floats, you can apply the following basic math operators.

.. literalinclude:: code/oneoffcoder/operator/mathop.py
   :language: python
   :linenos:

Exercise
^^^^^^^^

For the following 2 variables,

* print what is a + b?
* print what is a - b?
* print what is a x b?
* print what is a ÷ b?

.. code:: python

   a = 17
   b = 5

Solution.

.. code:: python

   print(f'{a} + {b} = {a + b}')
   print(f'{a} - {b} = {a - b}')
   print(f'{a} * {b} = {a * b}')
   print(f'{a} / {b} = {a / b}')

Compound assignment operators 
-----------------------------

If you had an integer variable, and wanted to add a number to it and reassign the result back to itself, how would you do so? Here's a way.

.. code:: python

   a = 15
   a = a + 2 # add 2 to a, and assign the result back to a

A shorter way of expressing this operation is through using a compound assignment operator.

.. code:: python

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

.. code:: python

   age = 15

Solution.

.. code:: python

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

.. code:: python

   print(16 << 1) # 32
   print(16 << 2) # 64
   print(16 << 3) # 128
   print(16 >> 1) # 8
   print(16 >> 1) # 4
   print(16 >> 1) # 2

Relational operators 
--------------------

.. literalinclude:: code/oneoffcoder/operator/relational.py
   :language: python
   :linenos:

Boolean logical operators 
-------------------------

.. literalinclude:: code/oneoffcoder/operator/booleanlogical.py
   :language: python
   :linenos:

Parentheses
-----------

.. literalinclude:: code/oneoffcoder/operator/parentheses.py
   :language: python
   :linenos:

List unpacking
--------------

.. literalinclude:: code/oneoffcoder/operator/listunpacking.py
   :language: python
   :linenos:
   :emphasize-lines: 6

List unpacking ignoring some values
-----------------------------------

.. literalinclude:: code/oneoffcoder/operator/listunpackingignoring.py
   :language: python
   :linenos:
   :emphasize-lines: 5

Merging lists via unpacking
---------------------------

.. literalinclude:: code/oneoffcoder/operator/mergelistviaunpacking.py
   :language: python
   :linenos:
   :emphasize-lines: 4

Merging dictionaries via unpacking
----------------------------------

.. literalinclude:: code/oneoffcoder/operator/mergedictionaryviaunpacking.py
   :language: python
   :linenos:
   :emphasize-lines: 9