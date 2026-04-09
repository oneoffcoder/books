Use compression.zstd for standard-library Zstandard
---------------------------------------------------

.. highlight:: python
   :linenothreshold: 1

In Python 3.14 and later, prefer ``compression.zstd`` for basic Zstandard support instead of reaching for a third-party dependency immediately.

.. note::

   Python 3.14+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import zstandard

    data = zstandard.ZstdCompressor().compress(b'hello world')

Do this
^^^^^^^

.. code:: python

    from compression import zstd

    data = zstd.compress(b'hello world')
