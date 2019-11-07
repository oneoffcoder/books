Merging dictionaries
--------------------

.. highlight:: python
   :linenothreshold: 1

Avoid explicit iterations when merging two dictionaries.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    name = {
        'first_name': 'john', 
        'last_name': 'doe'
    }
    address = {
        'street': '123 main street', 
        'city': 'washington', 
        'state': 'dc', 
        'zip': 20500
    }

    person = {}
    for k, v in name.items():
        person[k] = v
    for k, v in address.items():
        person[k] = v
    
Do this
^^^^^^^

.. code:: python

    name = {
        'first_name': 'john', 
        'last_name': 'doe'
    }
    address = {
        'street': '123 main street', 
        'city': 'washington', 
        'state': 'dc', 
        'zip': 20500
    }

    person = {**name, **address}