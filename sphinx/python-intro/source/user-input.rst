User Input
==========

Getting input from a user is accomplished through the ``input()`` function. When we use ``input()``, we can supply a prompt to give the user a hint about what to type. The program below asks the user to type in something and then simply echoes that input back. You can think of ``input()`` as the opposite of ``print()``: ``input()`` reads from the terminal and ``print()`` writes to it.

.. uml::

   @startuml
   start
   :Prompt user with input();
   :Read text from terminal;
   :Convert text if needed;
   :Use value in program;
   :Print result;
   stop
   @enduml

.. code-block:: python
    :linenos:

    user_input = input('Type in something: ')
    print(user_input)

Everything you get back from ``input()`` is a string. Let's write a program to ask the user to give us two numbers, add them, and return the result back.


.. code-block:: python
    :linenos:

    num_1 = input('num 1: ')
    num_2 = input('num 2: ')
    result = num_1 + num_2

    print(f'{num_1} + {num_2} = {result}')

If the user enters 1 and then 1 again for ``num_1`` and ``num_2``, the mathematical answer should be 2. Instead, the program prints 11. Why? Because ``input()`` always returns strings, so :code:`num_1 + num_2` performs string concatenation rather than numeric addition. To get arithmetic addition, we need to convert the inputs to integers first.

.. code-block:: python
    :linenos:
    :emphasize-lines: 4, 5

    num_1 = input('num 1: ')
    num_2 = input('num 2: ')

    num_1 = int(num_1)
    num_2 = int(num_2)
    result = num_1 + num_2

    print(f'{num_1} + {num_2} = {result}')

Exercise, Math Calculators
^^^^^^^^^^^^^^^^^^^^^^^^^^
Let's create some math calculator programs. 

* Write a program that asks the user for 2 numbers, print the subtraction result of those 2 numbers.
* Write a program that asks the user for 2 numbers, print the multiplication result of those 2 numbers.
* Write a program that asks the user for 2 numbers, then print the division result of those 2 numbers.

Solution.

Subtraction

.. code-block:: python
    :linenos:

    num_1 = int(input('num 1: '))
    num_2 = int(input('num 2: '))
    result = num_1 - num_2

    print(f'{num_1} - {num_2} = {result}')

Multiplication

.. code-block:: python
    :linenos:

    num_1 = int(input('num 1: '))
    num_2 = int(input('num 2: '))
    result = num_1 * num_2

    print(f'{num_1} x {num_2} = {result}')

Division

.. code-block:: python
    :linenos:

    num_1 = int(input('num 1: '))
    num_2 = int(input('num 2: '))
    result = num_1 / num_2

    print(f'{num_1} / {num_2} = {result}')

Exercise, Shape Calculators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's create some shape calculator programs.

* Write a program to ask the user for the side of square. Use the side the compute the perimeter and area of the square. Print the results to the user.
* Write a program to ask the user for the width and length of a rectangle. Use the width and length to compute the perimeter and area of the rectangle. Print the results to the user.
* Write a program to ask the user for the radius of a circle. Use the radius to compute the circumference and area of the circle. Print the results to the user.


Solution.

Square

.. code-block:: python
    :linenos:

    side = int(input('side: '))

    perimeter = 4 * side
    area = side * side

    print(f'perimeter = {perimeter}, area = {area}')

Rectangle

.. code-block:: python
    :linenos:

    width = int(input('width: '))
    length = int(input('length: '))

    perimeter = 2 * width + 2 * length
    area = width * length

    print(f'perimeter = {perimeter}, area = {area}')

Circle

.. code-block:: python
    :linenos:

    radius = int(input('radius: '))

    circumference = 2 * 3.1415 * radius
    area = 3.1415 * radius * radius

    print(f'circumference = {circumference}, area = {area}')
