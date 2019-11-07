Filtering files
---------------

.. highlight:: python
   :linenothreshold: 1

We are able to filter strings more concisely with fnmatch. Notice the second example uses a method, two for loops and an if statement?

Don't do this
^^^^^^^^^^^^^

.. code:: python

    files = ['one.txt', 'two.py', 'three.txt', 'four.py', 'five.scala', 'six.java', 'seven.py']

    py_files = filter(lambda f: f.endswith('.py'), files)

.. code:: python

    import os

    def traverse(path):
        for basepath, directories, files in os.walk(path):
            for f in files:
                if f.endswith('.ipynb'):
                    yield os.path.join(basepath, f)

    ipynb_files = traverse('./')

Do this
^^^^^^^

.. code:: python

    import fnmatch

    files = ['one.txt', 'two.py', 'three.txt', 'four.py', 'five.scala', 'six.java', 'seven.py']

    fnmatch.filter(files, '*.py')

.. code:: python

    import os

    ipynb_files = fnmatch.filter(
        (f for basepath, directories, files in os.walk('./') for f in files),
        '*.ipynb')

.. code:: python

    import pathlib

    ipynb_files = pathlib.Path('./').glob('**/*.ipynb')