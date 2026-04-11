JDK 26 Preview Notes
====================

JDK 26 is the latest feature release of Java. This book uses JDK 25 LTS as the
main baseline, so JDK 26-only features belong in a clearly marked preview
section.

Use preview features deliberately. They require explicit compiler and launcher
flags, and their syntax or API can still change before finalization.

.. code-block:: bash

   javac --release 26 --enable-preview Example.java
   java --enable-preview Example

Primitive patterns
------------------

JDK 26 previews primitive types in patterns, ``instanceof``, and ``switch``.
This makes pattern matching more uniform across reference and primitive values.

.. code-block:: java

   String statusMessage(int status) {
     return switch (status) {
       case 0 -> "okay";
       case 1 -> "warning";
       case 2 -> "error";
       case int code when code > 2 -> "unknown status: " + code;
     };
   }

Because this is preview syntax, do not use it in the core examples. The standard
JDK 25 way to write the same beginner-friendly code is still a normal
``default`` branch.

HTTP/3
------

JDK 26 adds HTTP/3 support to the HTTP Client API. Most beginner code still
starts with ``HttpClient``, ``HttpRequest``, and ``HttpResponse``; the new
protocol support mainly matters when an application talks to HTTP/3 servers.

Structured concurrency
----------------------

Structured concurrency is preview in JDK 26. It is important for the future of
Java concurrency, but this book should teach stable virtual threads first.
Preview structured-concurrency examples can be added later when the API is
final.

Migration notes
---------------

When moving code from JDK 25 to JDK 26, watch for these areas:

1. Preview code must be rechecked against the exact JDK 26 syntax.
2. HTTP Client behavior changed in a few edge cases.
3. The Applet API was removed.
4. Deep reflection that mutates ``final`` fields now emits warnings to prepare
   for future restrictions.
