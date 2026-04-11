Exercises and Mini-Projects
===========================

Practice turns the short examples in this book into working habits. Start with
small changes, then combine several chapters into one program.

Syntax practice
---------------

1. Change the ``HelloWorld`` program so it prints your name and the current
   year.
2. Create variables for a product name, price, quantity, and total cost.
3. Write an ``if`` statement that prints a letter grade from a numeric score.
4. Rewrite the grade logic with ``switch`` when the input is already a letter.
5. Use a ``for`` loop to print the first ten square numbers.

Object practice
---------------

1. Create a ``Student`` class with ``firstName``, ``lastName``, and ``grade``
   fields.
2. Add getters, setters, and a ``getFullName()`` method.
3. Override ``toString()`` so a student prints clearly.
4. Create an interface named ``Reportable`` with one method named ``report``.
5. Make ``Student`` implement ``Reportable``.

Collection practice
-------------------

1. Store five students in a ``List``.
2. Find all students with grades greater than or equal to ``90``.
3. Store unique course names in a ``Set``.
4. Store student IDs and students in a ``Map``.
5. Sort students by last name, then first name.

Streams practice
----------------

1. Convert a loop that sums numbers into a stream pipeline.
2. Use ``filter`` to keep only passing grades.
3. Use ``map`` to convert students into full names.
4. Use ``collect`` to place filtered results into a new list.
5. Use ``groupingBy`` to group students by letter grade.

Mini-project: gradebook
-----------------------

Build a command-line gradebook.

Requirements:

1. Read students from a CSV file with columns for ID, first name, last name, and
   numeric grade.
2. Convert each row into a ``Student`` object.
3. Store students in a ``Map`` keyed by ID.
4. Print the class average, highest grade, and lowest grade.
5. Print students grouped by letter grade.
6. Write a summary report to a text file.
7. Add tests for the grade conversion logic.

This project uses classes, collections, streams, exceptions, file IO, and tests
in one small program.

Mini-project: contact manager
-----------------------------

Build a contact manager that stores names, email addresses, and phone numbers.

Requirements:

1. Add a contact.
2. Search contacts by last name.
3. Remove a contact by ID.
4. Save contacts to a CSV file.
5. Load contacts from a CSV file.
6. Validate that an email address is present before saving.
7. Add tests for searching and validation.

Use this project to practice object modeling. A ``Contact`` class or record is
clearer than passing several unrelated strings through the program.
