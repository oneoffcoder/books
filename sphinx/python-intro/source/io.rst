Input/Output (IO)
=================

IO operations are those dealing with interacting with files; either we are reading (input) or writing (output). Most of the IO operations are done with context managers to manage the lifecycle of acquiring and releasing access to the files.

.. highlight:: python

File write and read
-------------------

Here's how to write to a file. Note that ``open()`` is a context manager for the file. Since we need to access the file in write mode, we pass in ``w``.

.. literalinclude:: code/oneoffcoder/io/writingfile.py
   :language: python
   :linenos:
   :emphasize-lines: 1

Here's how to read from a file. Since we need to access the file in read mode, we pass in ``r``.

.. literalinclude:: code/oneoffcoder/io/readingfile.py
   :language: python
   :linenos:
   :emphasize-lines: 1

JSON file write and read
------------------------

Creating and reading JSON file is pretty easy with the help of the ``json`` module. Note that we use the ``open()`` context manager as before, however, we leverage the ``dumps()`` method to dump dictionary data. The values stored in the dictionary should be primitive types (string, integer, float and boolean) or collections (list and dictionary) and the keys should be strings.

.. literalinclude:: code/oneoffcoder/io/wrjson.py
   :language: python
   :linenos:
   :emphasize-lines: 6,10,14

Pickle/unpickle data
--------------------

We have shown how to write and read from text-based files. Here, we show how to save data in binary format using the ``pickle`` module. Note that since the data being written and read is binary, we specify ``wb`` and ``rb``, respectively.

.. literalinclude:: code/oneoffcoder/io/pickledata.py
   :language: python
   :linenos:
   :emphasize-lines: 7,11

Shelving/unshelfing data
------------------------

We can use the ``shelve`` module to save data as well. If you have logical sets of data and you do not want to create one pickle file per data, then you can shelve the datasets into one file.

.. literalinclude:: code/oneoffcoder/io/shelvingdata.py
   :language: python
   :linenos:
   :emphasize-lines: 6-7,10-11

Creating temporary file and directory
-------------------------------------

If we need to create temporary files, we can use the ``tempfile`` module.

.. literalinclude:: code/oneoffcoder/io/tempio.py
   :language: python
   :linenos:
   :emphasize-lines: 4,9,13