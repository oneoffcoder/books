Libraries
=========

.. highlight:: python

The built-in Python modules do a lot that you need, but there are many Application Programming Interfaces (APIs), libraries or modules built for Python that will solve many other types of problems that are not addressed by built-in Python modules. We will look at some of these external libraries.

Pandas
------

``Pandas`` is a library for interacting with data. Writing CSV files is easy using Pandas.

.. literalinclude:: code/oneoffcoder/library/pandaswritecsv.py
   :language: python
   :linenos:
   :emphasize-lines: 9

Reading data from a CSV using Pandas is just as easy.

.. literalinclude:: code/oneoffcoder/library/pandasreadcsv.py
   :language: python
   :linenos:
   :emphasize-lines: 3

Numpy
-----

``Numpy`` is a numerical library. ``SciPy`` builds on numpy and is a general purpose scientific computing library.

Scikit-Learn
------------

``Scikit-Learn`` is a data science library.

joblib
------

``Joblib`` is an library to make multi-core processing easier in Python.