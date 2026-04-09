Use structural pattern matching for structural dispatch
-------------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

When branching on the shape of structured data, pattern matching can be clearer than a long ``if``/``elif`` chain.

Pattern matching becomes especially valuable when the condition depends on both the kind of input and the fields available on that input. It keeps the dispatch logic in one place and makes it easier to add new shapes without growing a fragile ladder of nested checks.

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
