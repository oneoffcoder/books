Types
=====

.. highlight:: python

Variable
--------
There is the fundmental concept of a ``variable`` in programming languages. Mathematically, a variable is a symbol denoting an unknown value. A most popular symbol denoting an unknown value in math is ``x``. In computer programming, however, one useful mental model of a variable is to think of it as a ``box``. In life, what can you do with a box?

* you can put something into a box
* you can take something out of a box
* you can label a box meaningfully

A variable is simply a storage container. Let's not get too technical in understanding what is a variable, as going to such level is not necessary to knowing how to effectively create and use variables when programming.

Last thing before moving on, each variable as a ``type`` associated with it. The variable type is determined by what it is storing. If a variable (a box) is storing an integer number, then the variable is said to be an integer variable. If a variable is storing a car, then the variable is siad to be a car variable. Whatever the box is storing determines the type of the box.

Basic types
-----------

There are four basic or ``primitive`` types in Python. They are ``float``, ``integer``, ``boolean`` and ``string``. You can remember these four types with the acronym, ``FIBS`` (float, integer, boolean, string). What are these types actually?

* an integer is a whole number value
* a float is a decimal number value
* a string is a text value
* a boolean is either true or false

A lesser known Python type is a ``complex number`` value. Below, we declare and initialize 5 variables, each storing one of the 5 basic variable types. Note the symbol ``=``, which is called the ``assignment operator``. To the left of the assignment operator is the variable name, and to the right is a literal value (e.g. string literal, integer literal, float literal, boolean literal and complex number literal). If you read the line :code:`i = 32` naturally, you should read it as *i is assigned to 32* and **not** *i is equal to 32*.

.. literalinclude:: code/oneoffcoder/type/basictype.py
   :language: python
   :linenos:

.. note::
   In Python, boolean values are either ``True`` or ``False``. Notice that these boolean literal values have the first letter capitalized? This convention is atypical, as other languages specify boolean values completely in lower case (e.g. ``true`` and ``false``).

After you declare a variable and assign a value to it, you may print it to the terminal.

.. code:: python

   age = 32
   print(age)

The value ``32`` will be printed to the terminal, and not the variable name ``age``. Remember we said to think of a variable as a box? You can put stuff in, take stuff out and label it meaningfully? Putting something into a box is accomplished through the assignment operator. Labelling the variable meaningfully is accomplished by giving a name that hints at the context. Taking something out of the box is accomplished through functions such as print; somehow, the print function is able to reach into the box and take what we have stored in it to be printed to the terminal. 

.. note::
   Said by Phil Karlton, "There are only two hard things in computer science: cache invalidation and naming things." Do not underestimate how difficult it is to give meaningful names to variables. A variable name such as ``x``, ``y`` or ``z`` does not indicate or hint at any context. 

Question
^^^^^^^^

In the code below, 

* what type is the variable ``s``?
* what type is the variable ``b``?
* what type is the variable ``i``?
* what type is the variable ``f``?
* what type is the variable ``c``?

.. code:: python

   s = 'test'
   b = False
   i = 3
   f = 3.14
   c = 17 + 29j

Solution.

* ``s`` is a string variable
* ``b`` is a boolean variable
* ``i`` is an integer variable
* ``f`` is a float variable
* ``c`` is a complex number variable

Question
^^^^^^^^

Create variables to store your name, age, height and whether you like pizza. Print the variables.

Solution.

.. code:: python

   name = 'John'
   age = 32
   height = 5.5
   pizza = True

   print(name)
   print(age)
   print(height)
   print(pizza)

Specifying a variable's type
----------------------------

In Python, the variable type is inferred from what it is storing; we do not have to explicitly declare the variable type with the variable name. Python is said to be a ``dynamically typed`` language, as compared with other languages that are ``statically typed`` where when you declare the variable name, you must also declare the variable type. However, in later versions of Python, you may declare the variable type associated with the variable name as follows. (As programmers from other statically typed languages have begun to adopt Python, you will see more Python code that specify type information with variables.)

.. literalinclude:: code/oneoffcoder/type/typedeclaration.py
   :language: python
   :linenos:

.. note::
   There is a difference between dynamically- versus statically-typed languages and weakly- versus strongly-typed languages. Dynamically- and statically-typed languages refer to what types of values a variable can store after they are declared. For example, in Python, we can declare a variable and assign anything to it later without problem.

   .. code:: python

      a = 'test'
      a = 3
      a = 3.4

   In Java, once we declare a variable and its type, we cannot assign values to that variables that are not of the same type.

   .. code:: java

      int a = 32;
      a = 42; // legal, since 42 is an int
      a = "test"; // illegal, cannot be done in Java

   Weakly- versus strongly-typed languages refers to the ability to force values into unrelated types. Weakly-typed languages can force values into unrelated types (e.g. an integer to a string), while strongly-typed languages cannot. Python is a strongly-typed language and JavaScript is a weakly-typed language. For example, in Python, we cannot add or concatenate a string with an integer.

   .. code:: python

      a = 1
      b = '1'
      c = a + b # illegal in python, error will be thrown
      d = str(a) + b # legal in python now, since a is forced into being a string

   In JavaScript, we can add or concantentate a string with an integer.

   .. code:: javascript

      const a = 1;
      const b = '1';
      const c = a + b; // legal in JavaScript, c is '11' as a is forced into being a string

   Python is said to be a dynamically- and strongly-typed language. Java is said to be a statically- and strongly-typed language. JavaScript is said to be a dynamically- and weakly-typed language. 

String
------

Let's dive a bit deeper with strings.

.. highlight:: python

String creation
^^^^^^^^^^^^^^^

Creating strings may be done with single, double or triple-quotes. Single and double quotes are the most common way to create strings in Python. Triple-quote strings are a bit special in that they enable you to define multi-line text.

.. literalinclude:: code/oneoffcoder/type/string.py
   :language: python
   :linenos:

If you are using single quotes to create a string and your text has a single quote, you must escape the single quote with a backslash ``\``. For example, :code:`'I\'m feeling happy and awesome today'`. Likewise, if you are using double quotes to create a string and your text has a double quote, you must escape the double quote with a backslash. For example, :code:`"She said, \"I love to code in Python.\""`.

Anything enclosed with single (or double) quotes is considered a string. All the variables below are string variables since they are storing string literals. One might jump to the conclusion that ``b`` should be considered an integer variable, however, ``b`` is assigned to a string :code:`b = '32'`; if we did :code:`b = 32` (no single quotes), then ``b`` would be an integer variable.

.. code:: python

   a = 'car'
   b = '32'
   c = '3.14'
   d = 'True'

String concatenation and interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/oneoffcoder/type/stringconcat.py
   :language: python
   :linenos:

String manipulation
^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/oneoffcoder/type/stringmanip.py
   :language: python
   :linenos:

List
----

.. literalinclude:: code/oneoffcoder/type/listtype.py
   :language: python
   :linenos:

Set
---

.. literalinclude:: code/oneoffcoder/type/settype.py
   :language: python
   :linenos:

Map
---

.. literalinclude:: code/oneoffcoder/type/maptype.py
   :language: python
   :linenos:

Tuple
-----

.. literalinclude:: code/oneoffcoder/type/tupletype.py
   :language: python
   :linenos: