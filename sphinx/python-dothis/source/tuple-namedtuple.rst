Avoid accessing tuple elements by index
---------------------------------------

.. highlight:: python
   :linenothreshold: 1

The key here is to avoid accessing tuples by indicies since those indicies are meaningless. Instead, use namedtuple and access elements of the tuple by a meaningful name.

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
