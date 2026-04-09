Dates, Times, and Time Zones
============================

.. highlight:: python

Working with dates and times is a common task in real programs. Python's ``datetime`` module handles dates and times, and ``zoneinfo`` adds standard-library time zone support.

Creating dates and times
------------------------

You can create ``date`` and ``datetime`` objects directly.

.. literalinclude:: code/oneoffcoder/datetimezoneinfo/create.py
   :language: python
   :linenos:

Current time
------------

Use ``datetime.now()`` to get the current local date and time.

.. literalinclude:: code/oneoffcoder/datetimezoneinfo/now.py
   :language: python
   :linenos:

Formatting and parsing
----------------------

``strftime()`` formats a date or time as text, and ``strptime()`` parses text into a ``datetime``.

.. literalinclude:: code/oneoffcoder/datetimezoneinfo/formatparse.py
   :language: python
   :linenos:

Time zones with zoneinfo
------------------------

Use ``zoneinfo.ZoneInfo`` when you need an aware datetime tied to a real time zone.

.. literalinclude:: code/oneoffcoder/datetimezoneinfo/zoneinfo_demo.py
   :language: python
   :linenos:

Why this matters
----------------

Dates and times often become tricky because formatting, parsing, and time zones all matter at once. It is worth learning the standard-library tools early so you do not end up treating times as plain strings everywhere in your code.
