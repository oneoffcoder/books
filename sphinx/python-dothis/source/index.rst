.. meta::
   :description: Python: Do This, Not That!
   :keywords: python
   :robots: index, follow
   :abstract: A book showing how to write beautiful, idiomatic Python code.
   :author: One-Off Coder
   :contact: info@oneoffcoder.com
   :copyright: One-Off Coder
   :content: global
   :generator: Sphinx
   :language: English
   :rating: general
   :reply-to: info@oneoffcoder.com
   :web_author: One-Off Coder
   :revisit-after: 1 days

.. Python: Do This, Not That! documentation master file, created by
   sphinx-quickstart on Wed Oct 16 19:28:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python: Do This, Not That!
==========================

Preface
=======

This book is a compact guide to writing clear, idiomatic Python. Each chapter uses a small example to contrast a clumsy approach with a cleaner one, with an emphasis on readability first and performance second.

The intended audience is Python developers who already know the language basics and want sharper instincts for everyday code review decisions. The examples are deliberately short, but the underlying goal is practical: write code that is easier to read, easier to change, and less error-prone.

Under each major section, you will see two sub-sections: ``Don't Do This`` and ``Do This``. Treat them as rules of thumb, not absolute laws. Python is full of tradeoffs, and the "better" choice depends on context. In this edition, the examples target modern Python 3 and favor current best practices over historical Python 2 compatibility.

Ideas and code examples are adapted from :cite:`RaHe19b,JeKn19,YaKh19` and from the wider Python community.

To follow along, you only need a recent Python 3 installation and a way to run short scripts or a REPL. A virtual environment is recommended.

.. code-block:: bash

   python3 -m venv .venv
   source .venv/bin/activate

You can then paste the snippets into ``python`` or save them to small files as you work through the chapters.

.. |JeffKnupp_Link| raw:: html

   <a href="https://jeffknupp.com/writing-idiomatic-python-ebook/" target="_blank">Jeff Knupp</a>


The chapters are grouped into core patterns first, followed by patterns that depend on newer Python versions.

Core Patterns
-------------

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Basics

   collection-initialization
   basic-chained-comparison
   basic-falsy-truthy
   basic-ternary-operator
   basic-any-all
   basic-none-comparison
   basic-walrus-operator

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Loops and Iteration

   looping-range-numbers
   looping-backward
   looping-collection
   looping-collection-indices
   looping-two-collections
   looping-enumerate-start
   iter-next-default
   collection-deque-queue
   iter-heapq-topn
   iter-combination
   iter-cycling
   iter-product

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Lists and Comprehensions

   list-generator
   list-filtering
   list-count-if
   list-counting
   dictionary-comprehension
   set-comprehension

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Tuples and Strings

   tuple-unpacking
   tuple-ignoring
   tuple-namedtuple
   string-concatenation
   string-interpolation
   string-debug
   string-dry
   string-reversal
   string-remove-prefix-suffix

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Functions and Context

   function-clarification
   function-lambda
   function-generator
   context-suppress
   context-nullcontext

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Dictionaries and Data

   dictionary-defaultdict
   dictionary-get
   dictionary-updating
   dictionary-merging
   dictionary-counting
   data-map-filter-reduce
   data-flattening
   data-caching

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Files, Paths, and Exceptions

   file-reading
   file-delete
   file-filtering
   file-serde-shelve
   pathlib-over-os-path
   exception-reraise

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Classes and Misc

   class-dunder
   class-enumeration
   class-dataclass-default-factory
   misc-simultaneous-state-updates
   misc-pandas

Version-Specific Patterns
-------------------------

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: General Modern Python

   class-new-vs-old
   misc-locals-explicit

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Python 3.9+

   data-functools-cache

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Python 3.10+

   looping-zip-strict
   class-dataclass-slots
   basic-pattern-matching

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Python 3.11+

   class-strenum
   typing-self
   file-tomllib
   asyncio-taskgroup
   exception-add-note
   exception-except-star

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Python 3.12+

   pathlib-walk
   pathlib-glob-case-sensitive
   typing-type-statement
   typing-override
   iter-batched

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Python 3.13+

   data-copy-replace
   queue-shutdown

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Python 3.14+

   concurrent-interpreterpoolexecutor
   concurrent-interpreters
   file-zstd
   string-template-literals

About
=====

.. image:: _static/images/logo.png
   :alt: One-Off Coder logo.

One-Off Coder is an educational, service and product company. Please visit us online to discover how we may help you achieve life-long success in your personal coding career or with your company's business goals and objectives.

- |Website_Link|
- |Facebook_Link|
- |Twitter_Link|
- |Instagram_Link|
- |YouTube_Link|
- |LinkedIn_Link|

.. |Website_Link| raw:: html

   <a href="https://www.oneoffcoder.com" target="_blank">Website</a>

.. |Facebook_Link| raw:: html

   <a href="https://www.facebook.com/One-Off-Coder-309817926496801/" target="_blank">Facebook</a>

.. |Twitter_Link| raw:: html

   <a href="https://twitter.com/oneoffcoder" target="_blank">Twitter</a>

.. |Instagram_Link| raw:: html

   <a href="https://www.instagram.com/oneoffcoder/" target="_blank">Instagram</a>

.. |YouTube_Link| raw:: html

   <a href="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ" target="_blank">YouTube</a>

.. |LinkedIn_Link| raw:: html

   <a href="https://www.linkedin.com/company/one-off-coder/" target="_blank">LinkedIn</a>

Copyright
=========

.. raw:: html

    <embed>
    This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a> by <a href="https://www.oneoffcoder.com" target="_blank">One-Off Coder</a>.
    <br />
    <br />
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
        <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
    </a>
    <br />
    <br />
    The full source code is available on <a href="https://github.com/oneoffcoder/books" target="_blank">GitHub</a>.
    <br />
    <br />
    </embed>

Cite this book as follows.::

    @misc{oneoffcoder_python_dothis_2019, 
    title={Python: Do This, Not That!}, 
    url={https://python.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Oct}}

Bibliography
============

.. bibliography:: references.bib
   :style: alpha

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>
