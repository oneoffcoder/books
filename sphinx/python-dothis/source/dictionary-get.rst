Accessing a dictionary value with a default value
-------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``dict.get`` when the missing-key case should fall back to a default value.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    d = {
        'username': 'jdoe'
    }

    is_authorized = False
    if 'auth_token' in d:
        is_authorized = True

.. code:: python

    d = {
        'username': 'jdoe'
    }

    is_authorized = True if 'auth_token' in d else False

Do this
^^^^^^^

.. code:: python

    d = {
        'username': 'jdoe',
        'theme': 'dark',
    }

    theme = d.get('theme', 'light')
