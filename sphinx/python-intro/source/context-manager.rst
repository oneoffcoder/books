Context Manager
===============

The concept of a ``context manager`` is to manage resources. Typically, these resources are limited, expensive to acquire or the references to such resources need to be released (so others may also access the resources). Examples of resources that we might want to manage include connections to databases or references to files. The context manager's main job is to manage the lifecycle of the resource, which is as follows.

* initialization (setup): this phase is for the context manager to set up the resource
* enter (reference and execution): this phase is to acquire the reference to the resource and give it back to the user for use
* exit (tear down): this phase is for the context manager to clean up (release) the resource.

If a context manager is being used, Python provides the ``with`` idiom to express the use of a resource.

.. code:: python

    with <context_manager> as <resource>:
        # do something with the resource

.. highlight:: python

A context manager is defined by creating a class and implementing at least two methods. 

* :code:`__enter__()`
* :code:`__exit__()`

.. code-block:: python
    :linenos:

    class HelloManager(object):
        def __init__(self):
            print('hello, world!')
        
        def __enter__(self):
            print('how are you doing?')
            return 7

        def __exit__(self, exc_type, exc_value, exc_traceback):
            print('bye, world!')

    with HelloManager() as hello_manager:
        print(f'what did HelloManager return? {hello_manager}')    

Note the method signature of ``__exit__(self, exc_type, exc_value, exc_traceback)`` which has several arguments/parameters. These arguments might be useful when there are exceptions. The arguments are named in a short way but more useful names could be mapped as follows.

* ``exc_type`` to ``exception_type``
* ``exc_value`` to ``exception_value``
* ``exc_traceback`` to ``traceback``

These arguments are not optional when defining ``__exit__()``; they must be part of the method signature of Python will assume that we are not implementing a cleanup for the exit phase. 

Exercise
--------

Create a context manager that generates the width and length randomly for a rectangle. Try using that context manager.

Solution.

.. code-block:: python
    :linenos:

    from random import randint

    class RandomRectManager(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
        
        def __enter__(self):
            width = randint(self.a, self.b)
            length = randint(self.a, self.b)
            return {
                'width': width,
                'length': length
            }

        def __exit__(self, etype, eval, etrace):
            pass

    with RandomRectManager(1, 10) as rect:
        print(f'what did RandomRectManager return? {rect}')

Exercise
--------

Create a context manager that generates the width and length randomly for 10 rectangle. Try using a generator function to help you. 

Solution.

.. code-block:: python
    :linenos:

    from random import randint

    class RandomRectManager(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __enter__(self):
            return self.__get_rect()

        def __exit__(self, etype, eval, etrace):
            pass

        def __get_rect(self):
            n = 0
            while n < 10:
                n += 1

                width = randint(self.a, self.b)
                length = randint(self.a, self.b)
                
                yield {
                    'width': width,
                    'length': length
                }

    with RandomRectManager(1, 10) as rects:
        for rect in rects:
            print(rect)