Classes
=======

Classes are the way to model your code after real-world objects. The act of coding to model real-world objects is called ``Object Oriented Programming`` or ``OOP``. Classes define two things about objects: their properties and actions. Properties are simply traits, characteristics or attributes of an object. Actions are what the object can do. **As such, properties are variables attached to a class and actions are functions attached to a class.** When you start defining an object with a class (or start writing a class definition), always keep in mind the properties and actions that are important to that object and make a sketch or outline. Let's do some examples.

If you are trying to model a person, what are some properties of a person and what can a person do? A person has a first and last name, as well as an age. A person can also eat, sleep or talk.

* Person
   - properties
      * first name
      * last name
      * age
   - actions
      * eat
      * sleep
      * talk

If you are trying to model a square, what are some properties and actions of a square? A square has a side and can compute its own area and perimeter.

* Triangle
   - properties
      * side
   - actions
      * compute area
      * compute perimeter

What about modeling a car? A car has a make, model, year, doors and gas efficiency rating. A car can start up, speed up, slow down or stop. 

* Car
   - properties
      * make
      * model
      * year
      * number of doors
      * miles per gallon
   - actions
      * start up
      * speed 
      * slow
      * stop

.. highlight:: python

Basic
-----

The best way to understand how to define an object is by looking at the **simplest** examples possible. Below, we are starting to define classes for a Person, Triangle and Car. Since we just want to view the simplest possible way to define classes without providing actual logic, we use the ``pass`` statement as a placeholder for future code.

.. code-block:: python
   :linenos:

   class Person(object):
      pass

   class Triangle(object):
      pass

   class Car(object):
      pass

.. note::
   In Python 2, classes could be defined as follows.

   .. code:: python

      class Person:
         pass
   
   This way of declaring a class is called ``old-style`` class definition. The ``new-style`` class definition is to make all class inherit from ``object`` explicitly as follows.

   .. code:: python

      class Person(object):
         pass

   In Python 3, there are only ``new-style`` classes, and whether you explicitly inherit from ``object`` or not, all classes in Python 3 are ``new-style``. We encourage coders to explicitly inherit from ``object`` regardless of using Python 2 or 3. In Python 2, if you use ``old-style`` class definition, then the class (by way of the ``.__class__`` property) and type (by way of calling ``type()``) are `not aligned <https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python#:~:text=New%2Dstyle%20classes%20are%20created,addition%20to%20what%20type%20returns.>`_. There are many `benefits <https://stackoverflow.com/questions/4015417/python-class-inherits-object>`_ of using ``new-style`` classes.


Constructor
-----------

Let's just focus on the class definition of ``Car``. Below, only the properties of a car are defined (make, model and year), and no actions are being modeled and defined, yet. However, there is one action (or method) that we have defined with the ``def`` keyword called ``__init__()``. The function ``__init__()`` is called the ``constructor`` of the class; when we create an instance of a ``Car``, this constructor method is called to create the instance and its state. The ``constructor`` dictates the essential properties that we must supply when we create an instance of a class. Notice that we have ``self`` as a part of the arguments to the constructor? What is ``self``? What is ``self`` doing there in the signature of the constructor? ``self`` refers to the instance of ``Car`` that we are trying to create, which is passed along with the properties. 

.. code-block:: python
   :linenos:

   class Car(object):
      def __init__(self, make, model, year):
         pass

.. note::
   Sometimes, the constructor is referred to as the ``ctor``.

How do we use ``self``? We use ``self`` to associate the instance with the properties. Note how we use dot ``.`` notation to say the instance's make ``self.make`` is assigned to the ``make`` passed into the constructor, and the same for model and year as well.

.. code-block:: python
   :linenos:

   class Car(object):
      def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

.. note::
   The constructor ``__init__()`` has two underscores ``_`` before and after the name ``init``. Why? By convention, Python has specified that ``magic methods`` have double underscores before and after the method name. These magic methods are sometimes called ``dunders`` for ``double underscores``. Dunders are magic methods in the sense that if they are defined, then they may be used with functions and operators with the intended, natural result. For example, another dunder is ``__repr__()`` which should return a string representation of an instance of a class. When issuing ``print()`` on an instance of a class, ``__repr__()`` will be called to get the string representation.

Instantiation
-------------

Now that we have class definition for ``Car``, how do we create an instance of ``Car``? Remember, according to the constructor, we need to always pass in the make, model and year. When create an instance, we simply refer to the name of the class with parentheses, and inside the parentheses, supply the required properties. Note that ``self`` is not supplied, Python will do that part. 

.. code-block:: python
   :linenos:

   class Car(object):
      def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

   # instantiation: create a Car instance
   car = Car('Honda', 'Accord', 2019)

After we have an instance of ``Car``, we can access the properties (and methods) using dot ``.`` notation.

.. code-block:: python
   :linenos:

   class Car(object):
      def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

   # instantiation: create a Car instance
   car = Car('Honda', 'Accord', 2019)

   # access the properties
   print(car.make)
   print(car.model)
   print(car.year)
   print(f'{car.make} {car.model} {car.year}')

Class methods
-------------

As stated before, classes has properties and actions. Actions defined for a class is no different than the general way of defining a function. However, the ``self`` argument is always supplied to class functions or methods. 

.. code-block:: python
   :linenos:

   class Car(object):
      def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

      def start_up(self):
         print('starting up')
      
      def speed(self):
         print('increasing speed')

      def slow_down(self):
         print('slowing down')

      def stop(self):
         print('stopping')

   # instantiation: create a Car instance
   car = Car('Honda', 'Accord', 2019)

   # access, call or invoke the methods of an instance of Car
   car.start_up()
   car.speed()
   car.slow_down()
   car.stop()

Getters and setters
^^^^^^^^^^^^^^^^^^^

If you come from other languages like Java or C#, it is typical to prevent direct read and write acces to properties. You may generate ``getters`` and ``setters`` to read and write to properties, correspondingly. 

.. literalinclude:: code/oneoffcoder/clazz/gettersetter.py
   :language: python
   :linenos:
   :emphasize-lines: 7-23

.. note::
   In general, ``getters`` are called ``accessors`` and ``setters`` are called ``mutators``. Typically, in Python, it is not common to see getters and setters being defined for classes. It seems to be that Pythonistas want code to be concise. 

Private method
^^^^^^^^^^^^^^

Unlike many other languages, such as Java or C#, Python does not have a way to specify access levels (e.g. private, protected or public). However, by convention, class methods that are determined to be private should start with a double underscore. Below, we have defined ``__check_year()`` to be private, and users should not invoke this method directly. The ``set_year()`` method calls ``__check_year()`` internally when the year is being mutated.

.. literalinclude:: code/oneoffcoder/clazz/privatemethod.py
   :language: python
   :linenos:
   :emphasize-lines: 7-8, 26

Static method
^^^^^^^^^^^^^

You can define functions at the class level, as opposed to the instance level, by annotating a function with ``@staticmethod``. Such function is said to be a ``static method`` and is defined **without** using ``self`` as an argument since the function is not associated with an instance, but, rather, with the class. You do not need an instance of a class to call static methods, you can access a static method through the class name using dot ``.`` notation.


.. literalinclude:: code/oneoffcoder/clazz/staticmethod.py
   :language: python
   :linenos:
   :emphasize-lines: 7-8, 27

Method overriding dunders
^^^^^^^^^^^^^^^^^^^^^^^^^

Overriding a method means to redefine it (assumes that a method has been previously defined). When defining a class, two dunder functions that should be overridden are ``__str__()`` and ``__repr__()``. Both methods return a string representation of the instance (of a class), however,

* ``__str__()`` returns an informal representation, and
* ``__repr__()`` returns a formal representation.

By convention, the string returned by ``__repr__()`` should be able to be used to reconstruct the instance. Many times, ``__str__()`` can just call ``__repr()__`` (or vice-versa).

.. literalinclude:: code/oneoffcoder/clazz/methodoverriding.py
   :language: python
   :linenos:
   :emphasize-lines: 7-11

Inheritance
-----------
One of the core tenets of coding is to reuse existing code. Why? Writing code is hard and testing code to assure quality and correctness is resource intensive. When you can, reuse code. This core tenent is so highly valued, we create languages like Python with features like OOP to encourage and enable code reuse. Specifically, ``inheritance`` is the feature of OOP that maximizes code-reuse. If we define a base class, there may be many sub-classes that share the same properties and actions, but with slight caveats. Inheritance enables the sub-classes to acquire the properties and actions of the base or parent class, and we can extend or modify the parent class' features by adding or overriding its features. 

Let's understand inheritance a bit better with an example dealing with shapes. In particular, we want to model a rectangle as follows. A rectangle has a width and length (properties). A rectangle should be able to compute its own area and perimeter (actions).

* Rectangle
   - properties
      * width
      * length
   - actions
      * computes area
      * computes perimeter

A ``Rectangle`` class definition could look like the following.

.. code-block:: python
   :linenos:

   class Rectangle(object):
      def __init__(self, width, length):
         self.name = type(self).__name__
         self.width = width
         self.length = length

      def get_area(self):
         return self.width * self.length

      def get_perimeter(self):
         return self.width * 2 + self.length * 2

      def __str__(self):
         return self.__repr__()

      def __repr__(self):
         return f'{self.name}[width={self.width}, length={self.length}]'

   r = Rectangle(10, 5)
   print(r)
   print(r.get_area())
   print(r.get_perimeter())

Now we want to create a class definition for a square. We know that a square **is a** rectangle with all sides equaled to one another. We do not want to recreate all the logic of that goes into computing the area and perimeter of a square since we have that logic defined in the ``Rectangle`` class. We should use inheritance to achieve the goal of logical relationship and code reuse. In the ``Square`` class definition, the constructor is different by requiring only the value of one side (all sides are equal, or width is the same as length). Also, we use ``super()`` to call the ctor of ``Rectangle``; ``Rectangle`` is called the base, parent or super class of ``Square``. Lastly, notice how ``Square`` does not have to define ``get_area()``, ``get_perimeter()``, ``__str__()`` or ``__repr__()``? ``Square`` has inherited such methods from ``Rectangle``.

.. code-block:: python
   :linenos:

   class Square(Rectangle):
      def __init__(self, side):
         super().__init__(side, side)

Here is the all-in-one example of class inheritance.

.. code-block:: python
   :linenos:

   class Rectangle(object):
      def __init__(self, width, length):
         self.name = type(self).__name__
         self.width = width
         self.length = length

      def get_area(self):
         return self.width * self.length

      def get_perimeter(self):
         return self.width * 2 + self.length * 2

      def __str__(self):
         return self.__repr__()

      def __repr__(self):
         return f'{self.name}[width={self.width}, length={self.length}]'

   class Square(Rectangle):
      def __init__(self, side):
         super().__init__(side, side)

   r = Rectangle(10, 5)
   print(r)
   print(r.get_area())
   print(r.get_perimeter())

   s = Square(5)
   print(s)
   print(s.get_area())
   print(s.get_perimeter())

Abstract Classes
----------------

Here, we have a base class ``Animal``. Noticed how the Animal class itself inherits from ``ABC`` (Abstract Base Class)?
We annotate the ``make_noise`` method ``@abstractmethod`` decorator. A class that inherits from ``ABC`` cannot be 
instantiated directly. We create two subclasses, ``Dog`` and ``Cat``, from Animal. These derived classes can be
instantiated, however, they must implement all methods annotated with ``@abstractmethod`` or a ``TypeError`` will be thrown.
The Animal class is also called a ``formal interface``.

.. literalinclude:: code/oneoffcoder/clazz/inheritance.py
   :language: python
   :linenos:

Informal Interface
------------------

An informal interface is defined like a class but has no internal state and method implementations are not provided.
Below, we have a circle calculator which computes the area and circumference of a circle given
the radius. We also show how to implement the informal interface. 

.. literalinclude:: code/oneoffcoder/clazz/informalinterface.py
   :language: python
   :linenos:

Mixin
-----

A mixin is like an abstract base class, but does not have state. It sits somewhere between an informal
interface and abstract base class. Philosophically, a mixin avoids problems with single and multiple
inheritance. Single inheritance can be taken to an extreme where long chains of inheritance can obfuscate
the intentions of methods and properties (fragmentation). Multiple inheritance is problematic when 
`diamond dependencies <https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem>`_ are created.

Below, we have an example class ``DivisionSolver`` that solves a division problem; the dividend (numerator)
and divisor (denominator) must be given. The ``DivFloatMixin`` returns the solution as a float. 
The ``DivQRMixin`` returns the solution with the quotient and remainder.

.. literalinclude:: code/oneoffcoder/clazz/mixin.py
   :language: python
   :linenos:

Python has a lot of mixins. Below, we use the ``Mapping`` mixin to model a person's mailing label.
Notice that the ``MailingLabel`` class behaves like a dictionary?

.. literalinclude:: code/oneoffcoder/clazz/mixinmapping.py
   :language: python
   :linenos: