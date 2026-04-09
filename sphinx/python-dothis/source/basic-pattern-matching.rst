Use structural pattern matching for structural dispatch
-------------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When branching on the shape of structured data, pattern matching can be clearer than a long ``if``/``elif`` chain.

.. note::

   Python 3.10+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    event = {'type': 'click', 'x': 10, 'y': 20}

    if event.get('type') == 'click':
        print(event['x'], event['y'])
    elif event.get('type') == 'keypress':
        print(event['key'])

Do this
^^^^^^^

.. code:: python

    event = {'type': 'click', 'x': 10, 'y': 20}

    match event:
        case {'type': 'click', 'x': x, 'y': y}:
            print(x, y)
        case {'type': 'keypress', 'key': key}:
            print(key)
