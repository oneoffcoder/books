Running Commands with subprocess
================================

.. highlight:: python

The ``subprocess`` module lets Python run external commands. This is useful when you want to automate shell tools, capture output, or check whether a command succeeded.

.. uml::

   @startuml
   skinparam shadowing false
   rectangle "Python program" as py
   rectangle "subprocess.run()" as run
   rectangle "external command" as cmd
   rectangle "stdout / stderr / exit code" as result

   py --> run
   run --> cmd
   cmd --> result
   @enduml

Running a command
-----------------

The simplest pattern is ``subprocess.run()`` with a list of arguments.

.. literalinclude:: code/oneoffcoder/subprocess/run_command.py
   :language: python
   :linenos:

Capturing output
----------------

If you need the command output inside Python, capture it explicitly.

.. literalinclude:: code/oneoffcoder/subprocess/capture_output.py
   :language: python
   :linenos:

Checking failures
-----------------

Use ``check=True`` if a non-zero exit status should raise an exception.

.. literalinclude:: code/oneoffcoder/subprocess/check_status.py
   :language: python
   :linenos:

Exercise
--------

Write a script that runs two external commands: one that succeeds and one that fails. Capture the output of the successful command and catch the exception from the failing one.

.. uml::

   @startuml
   skinparam shadowing false
   start
   :Run successful command;
   :Capture stdout;
   :Run failing command with check=True;
   :Handle CalledProcessError;
   stop
   @enduml

Solution
^^^^^^^^

.. code-block:: python
   :linenos:

   import subprocess

   ok = subprocess.run(['python3', '-c', "print('hello')"], capture_output=True, text=True, check=True)
   print(ok.stdout.strip())

   try:
       subprocess.run(['python3', '-c', 'import sys; sys.exit(1)'], check=True)
   except subprocess.CalledProcessError as exc:
       print(f'command failed: {exc.returncode}')
