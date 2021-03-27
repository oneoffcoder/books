Libraries
=========

.. highlight:: python

The built-in Python modules do a lot that you need, but there are many external Application Programming Interfaces (APIs), libraries or modules. We will look at some of these external libraries.

pip
---

One popular way to install external libraries is through ``pip``. ``pip`` is a commandline tool that allows you to install Python libraries from the `Python Package Index <https://pypi.org/>`_ ``PyPi``. In order to install a Python library from PyPi, all you need to know is the package name, e.g. ``pandas``, and then you can issue the installation as follows.

.. code-block:: bash

   pip install <package_name>

You can also install multiple packages in one line.

.. code-block:: bash

   pip install <package_name_1> <package_name_2>


.. note::
   ``pip`` will work its hardest to resolve ``transitive`` dependencies and bring those in. Transitive dependencies are those that a package you are trying to install depends on to work. 

Pandas
------

.. code-block:: bash

   pip install pandas

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

.. code-block:: bash

   pip install numpy scipy

``Numpy`` is a numerical library. ``SciPy`` builds on numpy and is a general purpose scientific computing library. If we wanted to draw samples from a normal distribution centered on 0 with a scale of 1, :math:`\mathcal{N}(0, 1)`, we can use the ``normal()`` function.

.. code-block:: python

   from numpy.random import normal

   values = normal(0, 1, 100)
   print(values)

Scikit-Learn
------------

.. code-block:: bash

   pip install scikit-learn

``Scikit-Learn`` is a data science library. We can use this library to learn predictive models, generate data, transform data and so on.

.. code-block:: python

   from sklearn.datasets import make_regression

   X, y = make_regression(**{
      'n_samples': 1000,
      'n_features': 50,
      'n_informative': 10,
      'n_targets': 1,
      'bias': 5.3,
      'random_state': 37
   })

   print(f'X shape = {X.shape}, y shape {y.shape}')

joblib
------

.. code-block:: bash

   pip install joblib

``Joblib`` is an library to make multi-core processing easier in Python.

.. code-block:: python

   from math import sqrt
   from joblib import Parallel, delayed

   results = Parallel(n_jobs=2)(delayed(sqrt) (i ** 2) for i in range(10))
   print(results)