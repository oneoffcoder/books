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

Convert the list of quantitative temperatures below to one of qualitative values using the new function defined.

.. code-block:: python
   :linenos:

   temperatures = [30.2, 77.5, 80.2, 101.1]

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

   # use a list comprehension
   temperatures = [30.2, 77.5, 80.2, 101.1]
   conditions = [describe_weather(t) for t in temperatures]
   print(conditions)

Exercise
^^^^^^^^

Write a functions to compute compute the area and perimeter of a square e.g. ``get_area(side)`` and ``get_perimeter(side)``.

* area = side x side
* perimeter = side x 4

Compute the areas and perimeters for the following squares (represented by integers) in the list.

.. code-block:: python
   :linenos:

   squares = [10, 5, 88, 3, 4, 3]

Solution.

.. code-block:: python
   :linenos:

   def get_area(side):
      return side * side

   def get_perimeter(side):
      return side * 4

   squares = [10, 5, 88, 3, 4, 3]
   
   for side in squares:
      area = get_area(side)
      perimeter = get_perimeter(side)

      s = f'side={side} | area = {area} | perimeter = {perimeter}'
      print(s)

Exercise
^^^^^^^^

Write a functions to compute compute the area and circumference of a circle e.g. ``get_area(radius)`` and ``get_circumference(radius)``.

* area = 3.14 x radius x radius
* circumference = 2 x 3.14 x radius

Compute the areas and perimeters for the following circles (represented by integers) in the list.

.. code-block:: python
   :linenos:

   circles = [10, 5, 88, 3, 4, 3]

Solution.

.. code-block:: python
   :linenos:

   def get_area(radius):
      return 3.14 * radius ** 2

   def get_circumference(radius):
      return 2 * 3.14 * radius

   circles = [10, 5, 88, 3, 4, 3]
   
   for radius in circles:
      area = get_area(radius)
      circumference = get_circumference(radius)

      s = f'radius={radius} | area = {area} | circumference = {circumference}'
      print(s)

Function with two arguments
---------------------------

Here is a demonstration of a function with two arguments and a return value. 

.. literalinclude:: code/oneoffcoder/function/twoargs.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3

Exercise
^^^^^^^^

Create the following functions.

* ``add(a, b)`` should add ``a`` and ``b`` and return the result
* ``minus(a, b)`` should subtract ``a`` from ``b`` and return the result
* ``times(a, b)`` should multiply ``a`` and ``b`` and return the result
* ``divide(a, b)`` should divide ``b`` by ``a`` and return the result

Invoke these functions for a variety of pairs of numbers and print the results.

.. code-block:: python
   :linenos:

   pairs = [(10, 2), (13, 4), (16, 5), (88, 7)]

Solution.

.. code-block:: python
   :linenos:

   def add(a, b):
      return a + b

   def minus(a, b):
      return b - a

   def times(a, b):
      return a * b

   def divide(a, b):
      return b / a

   pairs = [(10, 2), (13, 4), (16, 5), (88, 7)]

   for a, b in pairs:
      s = """
      {a} + {b} = {add(a, b)}
      {a} - {b} = {minus(a, b)}
      {a} * {b} = {times(a, b)}
      {a} / {b} = {divide(a, b)}
      """.strip()

      print(s)
      print('')

Exercise
^^^^^^^^

Write a functions to compute compute the area and perimeter of a rectangle e.g. ``get_area(width, length)`` and ``get_perimeter(width, length)``.

* area = width x length
* perimeter = 2 x width + 2 x length

Compute the areas and perimeters for the following rectangles (represented by tuples) in the list.

.. code-block:: python
   :linenos:

   rectangles = [(10, 5), (88, 3), (4, 3)]

Solution.

.. code-block:: python
   :linenos:

   def get_area(width, length):
      return width * length

   def get_perimeter(width, length):
      return 2 * width + 2 * length

   rectangles = [(10, 5), (88, 3), (4, 3)]

   for width, length in rectangles:
      area = get_area(width, length)
      perimeter = get_perimeter(width, length)

      s = f'width={width}, length={length} | area = {area} | perimeter = {perimeter}'
      print(s)

Exercise
^^^^^^^^

Write a functions to compute compute the area of a triangle e.g. ``get_area(base, height)``.

* area = 0.5 x base x height

Compute the areas for the following triangles (represented by tuples) in the list.

.. code-block:: python
   :linenos:

   triangles = [(10, 5), (88, 3), (4, 3)]

Solution.

.. code-block:: python
   :linenos:

   def get_area(base, height):
      return 0.5 * base * height

   triangles = [(10, 5), (88, 3), (4, 3)]

   for base, height in triangles:
      area = get_area(base, height)

      s = f'base={base}, height={height} | area = {area}'
      print(s)
   

Function with three arguments
-----------------------------

Here is an example of a function with 3 arguments as inputs, and the output is the product of the inputs.

.. literalinclude:: code/oneoffcoder/function/threeargs.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3

Exercise
^^^^^^^^

Write a function that takes in 3 integer arguments ``compute(x, y, z)``. The function return the result of ``x + y * z``.

Solution.

.. code-block:: python
   :linenos:

   def compute(x, y, z):
      return x + y * z

   print(compute(10, 5, 8))

Function with a list argument
-----------------------------

A function can accept anything as input, including other other functions! Here, ``concat()`` accepts a list of strings as input and returns the concatenation of the strings in the list using the ``join()`` function.

.. literalinclude:: code/oneoffcoder/function/listarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3

Exercise
^^^^^^^^

Python has many ``built-in`` functions for math operations. The ``sum()`` function takes in a collection of numbers and returns the sum across all the values. The ``len()`` function takes in a collection of numbers and returns the number of elements in that collection. Write a function ``get_average(numbers)`` that returns the expected value of a list of numbers. Remember, the expected value is the sum of the numbers divided by the total number of elements. 

.. code-block:: python
   :linenos:

   numbers = [5, 18, 29, 787, 2, 3, 88]

Solution.

.. code-block:: python
   :linenos:

   def get_average(numbers):
      total = sum(numbers)
      n = len(numbers)
      average = total / n
      return average

   numbers = [5, 18, 29, 787, 2, 3, 88]
   average = get_average(numbers)
   print(f'The average is {average:.5f}')

Exercise
^^^^^^^^

Write a function to compute the sample variance of a list of numbers. 

* the variance :math:`\sigma^2` is defined as :math:`\sigma^2 = \frac{\sum (x_i - \bar x)^2}{n - 1}`

.. code-block:: python
   :linenos:

   numbers = [5, 18, 29, 787, 2, 3, 88]

Solution.

.. code-block:: python
   :linenos:

   def get_average(numbers):
      total = sum(numbers)
      n = len(numbers)
      average = total / n
      return average

   def get_variance(numbers):
      avg = get_average(numbers)
      n = len(numbers)
      variance = sum([(n - avg)**2 for n in numbers]) / (n - 1)
      return variance

   numbers = [5, 18, 29, 787, 2, 3, 88]
   variance = get_variance(numbers)
   print(f'The variance is {variance:.5f}')

Function with default value argument
------------------------------------

The inputs required by a function can be set to default values. Note that if an input has a default value, it must always come last! Below, we pass in a list of strings and want to join them. The default delimiter is a comma, but the user can choose to override that delimiter when they invoke the function.

.. literalinclude:: code/oneoffcoder/function/defaultvalarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2,3,11

Exercise
^^^^^^^^

Write a function that takes in two integer ``a`` and ``b`` as well as a math operation (``+``, ``-``, ``*``, ``/``). The math operation should be set to ``+`` by default. Depending on the math operation, apply such operation to ``a`` and ``b`` and return the result.

.. code-block:: python
   :linenos:

   a = 14
   b = 8

Solution.

.. code-block:: python
   :linenos:

   def do_operation(a, b, op='+'):
      if '+' == op:
         return a + b
      elif '-' == op:
         return a - b
      elif '*' == op:
         return a * b
      else:
         return a / b

   a = 14
   b = 8

   ops = ['+', '-', '*', '/']
   
   for op in ops:
      result = do_operation(a, b)
      s = f'{a} {op} {b} = {result}'
      print(s)

Non-keyworded, variable-length argument
---------------------------------------

If you require any number of inputs to a function, but do not know what these inputs will look like or how many of them there will be, you can define the inputs as a ``non-keyworded, variable-length`` argument. Such argument is conventionally defined as ``*args`` and must always come after all keyworded arguments are defined.

.. literalinclude:: code/oneoffcoder/function/nonkeywordedarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2-4,7-9

.. note::
   You can pretty much achieve the same effect of a non-keyworded, variable-length argument with an argument that is a list. What do you think is the difference between a function defined as :code:`do_it(*args)` vs :code:`do_it(args=[])`?

Exercise
^^^^^^^^

Write a function to calculate the price of a pizza based on the toppings added to the pizza. The pizza itself cost $10.50. The topping costs are as follows.

* mushroom: $3.50
* suasage: $4.40
* olives: $1.25
* pepperoni: $2.00
* cheese: $1.25
* anchovy: $3.25

The function should specify a non-keyworded, variable-length argument to represent the toppings. 

Solution.

.. code-block:: python
   :linenos:

   def compute_cost(*toppings):
      prices = {
         'mushroom': 3.50,
         'suasage': 4.40,
         'olives': 1.25,
         'pepperoni': 2.00,
         'cheese': 1.25,
         'anchovy': 3.25
      }
      cost = sum([prices[topping] for topping in toppings if topping in prices])
      cost += 10.50
      return cost

   print(compute_cost(*['mushroom', 'suasage']))
   print(compute_cost(*['olives', 'pepperoni']))
   print(compute_cost(*['cheese', 'pepperoni']))
   print(compute_cost(*['mushroom', 'suasage', 'olives', 'pepperoni', 'cheese', 'anchovy']))

Keyworded, variable-length argument
-----------------------------------

In the case when you require any number of inputs to a function, but want the caller of the function to supply keywords associated with each of the inputs, you can define the inputs as a ``keyworded, variable-length`` argument. Such argument is conventionally defined as ``**kwargs`` and must come as the very last argument when defining a function.

.. literalinclude:: code/oneoffcoder/function/keywordedarg.py
   :language: python
   :linenos:
   :emphasize-lines: 2-4,7-9

.. note::
   You can also pretty much achieve the same effect of a keyworded, variable-length argument with an argument that is a dictionary. What do you think is the difference between a function defined as :code:`do_it(**kwargs)` vs :code:`do_it(kwargs=dict())`?

Exercise
^^^^^^^^

We have students who are left- or right-handed as shown below. Write a function to get the average age of the left- and right-handed individuals. Return the results. Make sure you use a keyworded, variable-length argument function.

.. code-block:: python
   :linenos:

   students = {
      'john': {'hand': 'left', 'age': 17},
      'jack': {'hand': 'right', 'age': 18},
      'jane': {'hand': 'left', 'age': 14},
      'mary': {'hand': 'right', 'age': 13},
      'joe': {'hand': 'left', 'age': 17},
      'james': {'hand': 'right', 'age': 14},
      'nancy': {'hand': 'left', 'age': 12},
      'norah': {'hand': 'right', 'age': 19},
   }

Solution.

.. code-block:: python
   :linenos:

   def get_average_ages(**persons):
      left_hand_ages = [data['age'] for _, data in persons.items() if data['hand'] == 'left']
      right_hand_ages = [data['age'] for _, data in persons.items() if data['hand'] == 'right']

      left_avg_age = sum(left_hand_ages) / len(left_hand_ages)
      right_avg_age = sum(right_hand_ages) / len(right_hand_ages)

      return {
         'left': left_avg_age,
         'right': right_avg_age
      }
   
   students = {
      'john': {'hand': 'left', 'age': 17},
      'jack': {'hand': 'right', 'age': 18},
      'jane': {'hand': 'left', 'age': 14},
      'mary': {'hand': 'right', 'age': 13},
      'joe': {'hand': 'left', 'age': 17},
      'james': {'hand': 'right', 'age': 14},
      'nancy': {'hand': 'left', 'age': 12},
      'norah': {'hand': 'right', 'age': 19},
   }

   results = get_average_ages(**students)
   print(results)

Mixed arguments
---------------

Here's an example of a function with mixed argument/input types.

.. literalinclude:: code/oneoffcoder/function/mixedargs.py
   :language: python
   :linenos:
   :emphasize-lines: 2-9

Unpacking tuple return type
---------------------------

We have already seen how to unpack tuples, here, we show how we can unpack a tuple returned from a function.

.. literalinclude:: code/oneoffcoder/function/unpackingtuple.py
   :language: python
   :linenos:
   :emphasize-lines: 1,2,12

Lambda
------

A ``lambda`` is a function, however, lambda functions are strictly defined as one line logic or ``one-liners``. Take the ``say_hello()`` function below. This function can have multiple lines of statement, although, in this case, it only has one statement which is to print **hello**.

.. code-block:: python
   :linenos:

   def say_hello():
      print('hello')

   # call the function
   say_hello()

Now, look at this function re-defined as a lambda.

.. code-block:: python
   :linenos:

   say_hello = lambda: print('hello')

   # call the lambda
   say_hello()

It seems lambdas are suited for very simple logic (one-liners), and if you have complicated logic, you are better off using a function. Lambdas can also take in parameters/arguments.

.. code-block:: python
   :linenos:

   # lambda with 1 argument
   say_hello = lambda name: print(f'hello, {name}')
   
   # call lambda
   say_hello('John')
   say_hello('Mary')

   # lambda with 2 arguments
   say_bye = lambda fname, lname: print(f'bye, {fname} {lname}')

   # call lambda
   say_hello('John', 'Doe')
   say_hello('Mary', 'Smith')

Lambdas can return values.

.. code-block:: python
   :linenos:

   # define lambdas
   add_one = lambda x: x + 1
   minus_one = lambda x: x - 1
   times_two = lambda x: x * 2
   divide_half = lambda x: x / 2

   # call lambdas one at a time
   print(add_one(1)) # should print 2
   print(minus_one(1)) # should print 0
   print(times_two(1)) # should print 2
   print(divide_half(1)) # should print 0.5

   # compose operations using lambdas
   # should print 50
   # 50 / 2 = 25
   # 25 * 2 = 50
   # 50 - 1 = 49
   # 49 + 1 = 50
   print(add_one(minus_one(times_two(divide_half(50)))))

Functions and lambdas can be passed as arguments themselves. Below, we have a generic math lambda called ``do_math()`` which takes in two numbers ``a`` and ``b`` as well as a function/lambda as ``op``. 

.. code-block:: python
   :linenos:

   # define lambdas
   add = lambda a, b: a + b
   subtract = lambda a, b: a - b
   multiply = lambda a, b: a * b
   divide = lambda a, b: a / b

   # this lambda takes in 3 arguments
   # a and b are integers
   # op is a function or lambda and will be applied to a and b
   do_math = lambda a, b, op: op(a, b)

   # call do_math and change the op
   a, b = 12, 7
   print(do_math(a, b, add))
   print(do_math(a, b, subtract))
   print(do_math(a, b, multiply))
   print(do_math(a, b, divide))

   # note here, we inline a lambda
   print(do_math(a, b, lambda a, b: a ** b))

Exercise
^^^^^^^^

If we have the following list of first and last names of people, transform that list to a new one where each element in the new list is the initials of the corresponding person. Try using lambdas to solve this problem.

.. code-block:: python
   :linenos:

   names = [('John', 'Doe'), ('Jane', 'Smith')]

Solution.

.. code-block:: python
   :linenos:

   get_initial = lambda name: f'{name.capitalize()[0]}'
   get_initials = lambda fname, lname: f'{get_initial(fname)}.{get_initial(lname)}.'

   names = [('John', 'Doe'), ('Jane', 'Smith')]
   initials = [get_initials(fname, lname) for fname, lname in names]

   print(initials)

Exercise
^^^^^^^^

If you have the list of numbers below, create a new list from this one by including only 

* those numbers that start with a 1 and 
* have at least 3 digits 

and transform those numbers by dividing by 2 and then raising the result to the power of 2.

.. code-block:: python
   :linenos:

   numbers = [101, 100, 1003, 10002, 202, 13, 1234]

Solution.

.. code-block:: python
   :linenos:

   transform = lambda x: (x / 2.0) ** 2.0
   has_three_or_more_digits = lambda x: True if len(str(x)) >= 3 else False
   starts_with_one = lambda x: str(x).startswith('1')
   is_valid = lambda x: has_three_or_more_digits(x) and starts_with_one(x)

   numbers = [101, 100, 1003, 10002, 202, 13, 1234]
   nums = [transform(n) for n in numbers if is_valid(n)]

   print(nums)