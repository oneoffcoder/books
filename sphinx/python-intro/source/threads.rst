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

So, ``squared()`` did not return anything, but, what we wanted to get the results? How do we get any output from ``squared()``? The idea here is to use a ``Queue``. The pattern of multiprocessing with ``Process`` is now, create, start, get and join.

.. code-block:: python
   :linenos:
   :emphasize-lines: 1,7,16,24,35-38,45

   from multiprocessing import Process, Queue
   import random
   import os
   from random import randint


   def squared(x, queue):
      module_name = __name__
      parent_id = os.getppid()
      process_id = os.getpid()

      result = x * x

      print(f'module={module_name} : parent={parent_id} : process={process_id} : result={result}')

      queue.put(result)


   if __name__ == '__main__':
      # generate 1,000 random numbers in the range [0, 100]
      numbers = [random.randint(0, 100) for _ in range(1000)]

      # set up a queue to store results
      queue = Queue()

      # create a list of Process
      processes = [Process(target=squared, args=(num, queue)) for num in numbers]

      # start each Process
      for process in processes:
         process.start()

      # get items from the queue to prevent the queue from filling up 
      # if the queue fills up, it will block
      results = []
      for process in processes:
         result = queue.get()
         results.append(result)

      # join each Process
      for process in processes:
         process.join()

      # print results
      print(results)

Exercise
^^^^^^^^
Write a multiprocessing program to simulate the rolling of dice. There should be a function to simulate rolling 2 dice, and that function should store the result (add the numbers together). At the very end, collect your results from the simulation and count the number of unique values that came up.

Solution.

.. code-block:: python
   :linenos:

   from multiprocessing import Process, Queue
   from random import randint
   from itertools import groupby


   def roll(queue):
      die1 = randint(1, 6)
      die2 = randint(1, 6)
      total = die1 + die2

      queue.put(total)


   if __name__ == '__main__':
      # set up a queue to store results
      queue = Queue()

      # create a list of Process
      processes = [Process(target=roll, args=(queue, )) for _ in range(100)]

      # start each Process
      for process in processes:
         process.start()

      # get items from the queue to prevent the queue from filling up 
      # if the queue fills up, it will block
      results = []
      for process in processes:
         result = queue.get()
         results.append(result)

      # join each Process
      for process in processes:
         process.join()

      # print results
      get_key = lambda x: x
      counts = {k: len(list(v)) for k, v in groupby(sorted(results, key=get_key), key=get_key)}
      print(counts)

Pool
----

``Pool`` enables you to use a much simpler idiom for multiprocessing. If the function that you are invoking in the parallelized operations return something, you do not need another structure like ``Queue`` to be passed in to store the results.

.. literalinclude:: code/oneoffcoder/threading/poolexample.py
   :language: python
   :linenos:
   :emphasize-lines: 1,11,12

What if the function you are calling requires multiple parameters? Use ``starmap()`` instead of ``map()``.

.. code-block:: python
   :linenos:
   :emphasize-lines: 11

   from multiprocessing import Pool
   from random import randint

   def times(x, y, z):
      return x * y * z

   if __name__ == '__main__':
      rand = lambda: (randint(0, 10), randint(0, 10), randint(0, 10))
      triplets = [rand() for _ in range(1000)]
      with Pool(5) as pool:
         results = pool.starmap(times, triplets)
         print(results)

Multiprocessing
---------------

Here's another way of using the multiprocessing module to perform parallel processing.

.. literalinclude:: code/oneoffcoder/threading/multiprocessingexample.py
   :language: python
   :linenos:
   :emphasize-lines: 18,19,21,29-30

Synchronization
---------------

We can use ``Lock`` to synchronize between different processes. The function ``acquire()`` will place a hold on the parallel processes, and ``release()`` will allow the parallel processes to continue.

.. literalinclude:: code/oneoffcoder/threading/lockingexample.py
   :language: python
   :linenos:
   :emphasize-lines: 13,17,21,32,37
