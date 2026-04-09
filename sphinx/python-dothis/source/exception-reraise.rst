Re-raise exceptions deliberately
--------------------------------

.. highlight:: python
   :linenothreshold: 1

Catch specific exceptions and re-raise with context. Avoid swallowing errors or using a bare ``except``.

Re-raising deliberately keeps the failure visible while adding just enough local context to explain what the code was trying to do. That usually produces better debugging information than either swallowing the error or replacing it with a vague new one.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    try:
        config = load_config('settings.json')
    except:
        raise RuntimeError('configuration failed')

Do this
^^^^^^^

.. code:: python

    try:
        config = load_config('settings.json')
    except FileNotFoundError as exc:
        raise RuntimeError('settings.json was not found') from exc
