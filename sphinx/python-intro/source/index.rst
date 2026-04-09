.. meta::
   :description: Python, No Tears
   :keywords: python
   :robots: index, follow
   :abstract: A Python tutorial book.
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

.. Python, No Tears documentation master file, created by
   sphinx-quickstart on Tue Oct 22 17:49:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python, No Tears
================

This edition is updated for Python 3.13.

Preface
=======

This book is an introduction to programming in ``Python``. The examples and recommendations in this edition target Python 3.13. You can follow along with a local Python 3.13 installation, but a Docker image is also available if you want a preconfigured environment with JupyterLab already set up. The diagram below is the book roadmap, showing that the material starts with core syntax, then adds control flow and reusable code, and only after that moves into objects, the standard library, and practice-heavy chapters.

.. uml::

   @startuml
   left to right direction
   skinparam shadowing false
   rectangle "Basics\nintro, types,\noperators" as basics
   rectangle "Flow\ncontrol, matching,\nloops" as flow
   rectangle "Functions\nfunctions, docs,\ndecorators" as functions
   rectangle "Objects\nclasses, dataclasses,\nenum, typing" as objects
   rectangle "Stdlib\npathlib, datetime,\nexceptions, threads,\nio" as stdlib
   rectangle "Practice\nbuilt-ins, collections,\nfunctional, turtle,\nprojects" as practice
   basics --> flow
   flow --> functions
   functions --> objects
   objects --> stdlib
   stdlib --> practice
   @enduml

Use that roadmap when jumping around the book: chapters later in the chain assume more vocabulary and more comfort with Python's built-in tools. To run the Docker image, use the following command.

.. code-block:: bash

   docker run -it \
    -p 8888:8888 \
    oneoffcoder/book-python-intro

The Docker container starts `JupyterLab <https://jupyter.org/>`_ on port ``8888``. When the container is running, you can open it at `http://localhost:8888 <http://localhost:8888>`_.

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Contents
   
   intro
   types
   operators
   control
   pattern-matching
   user-input
   loops
   function
   documentation
   builtin-function
   collections
   functional
   decorators
   clazz
   dataclasses
   enum
   typing
   libraries
   json
   csv
   pathlib
   random
   datetime-zoneinfo
   tomllib
   argparse
   subprocess
   logging
   exceptions
   context-manager
   threads
   io
   testing
   turtle
   mini-projects
   more-practice
   python-3-13-notes

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Nifty Libraries
   
   extralib

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

    @misc{oneoffcoder_python_intro_2019, 
    title={Python, No Tears}, 
    url={https://learn-python.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Oct}}

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>
