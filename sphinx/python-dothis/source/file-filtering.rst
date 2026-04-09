Filtering files
---------------

.. highlight:: python
   :linenothreshold: 1

``fnmatch`` can express simple filename filtering more concisely. Notice how the second example uses a helper function, nested loops, and an ``if`` statement.

Filename matching is usually simpler than the loops used to discover it. Using a purpose-built helper keeps the filtering rule front and center instead of burying it inside traversal code.

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
