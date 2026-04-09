JMESPath
========

We work with JSON data a lot in the real world. `JMESPath`_ ("james path") makes it easy to extract and query values from a JSON document. To use it, install the `jmespath package <https://pypi.org/project/jmespath/>`_.

.. graphviz::

   digraph extralibs {
     rankdir=LR;
     node [shape=box, style="rounded"];
     libs [label="useful third-party libraries"];
     jmespath [label="JMESPath\nquery JSON"];
     dateutil [label="python-dateutil\nparse and adjust dates"];
     termtables [label="termtables / tabulate\npretty-print tables"];
     libs -> jmespath;
     libs -> dateutil;
     libs -> termtables;
   }

.. _JMESPath: https://jmespath.org/

.. literalinclude:: code/oneoffcoder/extralib/jmespathdemo.py
   :language: python
   :linenos:

For more information on JMESPath, check out the following links.

- `JMESPath home page <https://jmespath.org/>`_
- `JMESPath examples <https://jmespath.org/examples.html>`_
- `JMESPath tutorial <https://jmespath.org/tutorial.html>`_

python-dateutil
===============

Date and time information is everywhere. It is not easy to parse, clean and format date and time information. The `python-dateutil <https://dateutil.readthedocs.io/en/stable/>`_ package can help ease the pain of dealing with date and time data.

.. literalinclude:: code/oneoffcoder/extralib/pythondateutildemo.py
   :language: python
   :linenos:

termtables
==========

If you have tabular data, you will find yourself wanting to pretty print the content from time to time if the data is not so big. There are many libraries to help you do so.

- `termtable <https://github.com/nschloe/termtables>`_
- `texttable <https://pypi.org/project/texttable/>`_
- `prettytable <https://pypi.org/project/prettytable/>`_
- `tabulate <https://pypi.org/project/tabulate/>`_

.. literalinclude:: code/oneoffcoder/extralib/termtablesdemo.py
   :language: python
   :linenos:
