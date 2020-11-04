Threading
=========

.. highlight:: python

Process
-------

The ``Process`` object will create a new process to invoke the method associated with it. The two important arguments to ``Process`` is the **target**, which is typically a function, and **args** which is a tuple of the arguments that we want to pass to the function. The ``start()`` function of a ``Process`` object will commence the computation and the ``join()`` function will wait until the processing is finished. Below, we generate a list of 1,000 random numbers in the range [0, 100]. What we want to do with each number is to square it. Note the function ``squared()`` does not return anything; it simply computes the result of the integer passed to it squared. Also, inside ``squared()``, we get the parent and process IDs associated with running the method to show that these are indeed different processes that are being created. 

.. note::
   If you look at the code below, you will see that we use the ``main guard`` which is :code:`if __name__ == '__main__':`. We perform multiprocessing inside the main guard to prevent problems associated with the ways processes are created (endless loops of process generations). `Python <https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming>`_ recommends that multiprocessing code be placed inside the main guard.

.. code-block:: python
   :linenos:
   :emphasize-lines: 1,19,26,30

   from multiprocessing import Process
   import random
   import os
   from random import randint


   def squared(x):
      module_name = __name__
      parent_id = os.getppid()
      process_id = os.getpid()

      result = x * x

      print(f'module={module_name} : parent={parent_id} : process={process_id} : result={result}')


   if __name__ == '__main__':
      # generate 1,000 random numbers in the range [0, 100]
      numbers = [random.randint(0, 100) for _ in range(1000)]

      # create a list of Process
      processes = [Process(target=squared, args=(num,)) for num in numbers]

      # start each Process
      for process in processes:
         process.start()

      # join each Process
      for process in processes:
         process.join()

Pool
----

.. literalinclude:: code/oneoffcoder/threading/poolexample.py
   :language: python
   :linenos:
   :emphasize-lines: 1,10,11

Multiprocessing
---------------

.. literalinclude:: code/oneoffcoder/threading/multiprocessingexample.py
   :language: python
   :linenos:
   :emphasize-lines: 18,19,21,29-30

Synchronization
---------------

.. literalinclude:: code/oneoffcoder/threading/lockingexample.py
   :language: python
   :linenos:
   :emphasize-lines: 13,17,21,32,37
