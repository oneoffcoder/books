JMESPath
========

We work with JSON data a lot in the real world. Would it not be nice to be able to extract and query for values in our JSON data? `JMESPath` (james path) enables the extraction of elements from a JSON document. To use JMESPath, you will have to install the `jmespath <https://pypi.org/project/jmespath/>`_ module. 

.. literalinclude:: code/oneoffcoder/extralib/jmespathdemo.py
   :language: python
   :linenos:

For more information on JMESPath, check out the following links.

- `JMESPath <https://jmespath.org/>`_
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