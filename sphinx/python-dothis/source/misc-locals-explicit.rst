Use explicit namespaces with exec and eval
------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Do not rely on mutating ``locals()``. Pass explicit namespaces to ``exec()`` or ``eval()`` instead.

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
