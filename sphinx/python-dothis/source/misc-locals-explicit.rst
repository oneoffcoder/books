Use explicit namespaces with exec and eval
------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Do not rely on mutating ``locals()``. Pass explicit namespaces to ``exec()`` or ``eval()`` instead.

Relying on implicit local-scope mutation is hard to reason about and varies by execution context. Explicit mappings make the data flow visible and make dynamic execution code much easier to debug.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    x = 1
    exec('x = 2', globals(), locals())
    print(x)

Do this
^^^^^^^

.. code:: python

    scope = {'x': 1}
    exec('x = 2', {}, scope)
    print(scope['x'])
