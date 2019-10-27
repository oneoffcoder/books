Threading
=========

Different ways to create threads
--------------------------------

Implementing Runnable
^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithImplementingRunnable.java
   :language: java
   :linenos:
   :lines: 5-20
   :dedent: 2
   :emphasize-lines: 1

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithImplementingRunnable.java
   :language: java
   :linenos:
   :lines: 23-24
   :dedent: 4

Extending Thread
^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithExtendingThread.java
   :language: java
   :linenos:
   :lines: 5-21
   :dedent: 2
   :emphasize-lines: 1

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithExtendingThread.java
   :language: java
   :linenos:
   :lines: 25-26
   :dedent: 4

Anonymous subclass
^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithAnonymousSubclass.java
   :language: java
   :linenos:
   :lines: 6-24
   :dedent: 4
   :emphasize-lines: 1-17

Lambda runnable
^^^^^^^^^^^^^^^

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithLambda.java
   :language: java
   :linenos:
   :lines: 6-21
   :dedent: 4
   :emphasize-lines: 1-14

Multiple threads
----------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/MultipleThreads.java
   :language: java
   :linenos:
   :lines: 6-29
   :dedent: 4
   :emphasize-lines: 1,19,23

Timer and TimerTask
-------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithTimer.java
   :language: java
   :linenos:
   :lines: 9-31
   :dedent: 4
   :emphasize-lines: 1,3,10,23

Executor
--------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithExecutor.java
   :language: java
   :linenos:
   :lines: 3-5

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithExecutor.java
   :language: java
   :linenos:
   :lines: 9-33
   :dedent: 2

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithExecutor.java
   :language: java
   :linenos:
   :lines: 36-64
   :dedent: 4
   :emphasize-lines: 11,14,16,21,27

Callable
--------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithCallable.java
   :language: java
   :linenos:
   :lines: 3-9

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithCallable.java
   :language: java
   :linenos:
   :lines: 13-45
   :dedent: 2
   :emphasize-lines: 16

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithCallable.java
   :language: java
   :linenos:
   :lines: 48-70
   :dedent: 4
   :emphasize-lines: 7,14,18

Sharing a variable across threads
---------------------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithAtomicInteger.java
   :language: java
   :linenos:
   :lines: 3-10

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithAtomicInteger.java
   :language: java
   :linenos:
   :lines: 14-37
   :dedent: 2
   :emphasize-lines: 4

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithAtomicInteger.java
   :language: java
   :linenos:
   :lines: 40-61
   :dedent: 4
   :emphasize-lines: 1

Fork/Join and Recursive Task
----------------------------

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithForkJoinRecursiveTask.java
   :language: java
   :linenos:
   :lines: 3-12

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithForkJoinRecursiveTask.java
   :language: java
   :linenos:
   :lines: 16-83
   :dedent: 2
   :emphasize-lines: 1,41-52

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithForkJoinRecursiveTask.java
   :language: java
   :linenos:
   :lines: 97-102
   :dedent: 2

.. literalinclude:: code/src/main/java/com/oneoffcoder/java/threading/WithForkJoinRecursiveTask.java
   :language: java
   :linenos:
   :lines: 86-94
   :dedent: 4
   :emphasize-lines: 4