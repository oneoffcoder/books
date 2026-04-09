Use add_note for extra exception context
----------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``add_note()`` to attach extra debugging context instead of overloading the exception message itself.

.. note::

   Python 3.11+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    try:
        process_invoice(invoice_id)
    except ValueError as exc:
        raise ValueError(f'invoice failed: {invoice_id}') from exc

Do this
^^^^^^^

.. code:: python

    try:
        process_invoice(invoice_id)
    except ValueError as exc:
        exc.add_note(f'invoice_id={invoice_id}')
        raise
