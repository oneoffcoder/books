.. SQLite documentation master file, created by
   sphinx-quickstart on Thu Jun  3 16:11:30 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SQLite's documentation!
==================================

This book is currently small, but the diagram below still captures the core SQLite workflow the material is meant to support: connect to a database, define tables, query data, and inspect results.

.. uml::

   @startuml
   left to right direction
   skinparam shadowing false
   rectangle "Connect" as connect
   rectangle "Define Schema" as schema
   rectangle "Insert and\nUpdate Data" as mutate
   rectangle "Query" as query
   rectangle "Inspect\nResults" as inspect
   connect --> schema --> mutate --> query --> inspect
   @enduml

Even before more chapters are added, that diagram gives readers the practical lifecycle they should expect when working through SQLite examples.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
