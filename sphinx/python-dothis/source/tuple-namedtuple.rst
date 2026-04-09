Avoid accessing tuple elements by index
---------------------------------------

.. highlight:: python
   :linenothreshold: 1

Avoid accessing tuple elements by index when the positions have semantic meaning. Use ``namedtuple`` so the fields can be accessed by name.

Once positions start carrying domain meaning, named access is easier to remember and far harder to misuse than numeric indexes. It also makes later code reviews faster because field names explain themselves.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    scores = [80, 90, 95, 88, 99, 93]

    students = [(name, score) for name, score in zip(names, scores)]

    for student in students:
        print('{} {}'.format(student[0], student[1]))

Do this
^^^^^^^

.. code:: python

    from collections import namedtuple

    names = ['john', 'jane', 'jeremy', 'janice', 'joyce', 'jonathan']
    scores = [80, 90, 95, 88, 99, 93]
    
    Student = namedtuple('Student', 'name score')
    students = [Student(name, score) for name, score in zip(names, scores)]

    for student in students:
        print('{} {}'.format(student.name, student.score))
