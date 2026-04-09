Use @override for overridden methods
------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.12 and later, use ``@override`` to mark methods that are intended to override a base-class method.

.. note::

   Python 3.12+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    class BaseFormatter:
        def format(self, value):
            return str(value)

    class JsonFormatter(BaseFormatter):
        # overrides BaseFormatter.format
        def format(self, value):
            return f'"{value}"'

Do this
^^^^^^^

.. code:: python

    from typing import override

    class BaseFormatter:
        def format(self, value):
            return str(value)

    class JsonFormatter(BaseFormatter):
        @override
        def format(self, value):
            return f'"{value}"'
