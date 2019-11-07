Saving objects to file
----------------------

.. highlight:: python
   :linenothreshold: 1

In the example below, although pickle is a great way to save objects, shelve is an alternative to saving multiple data/objects into a central location.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import pickle

    object_1 = 'pretend some big object 1'
    object_2 = 'pretend some big object 2'
    data = {
        'object_1': object_1,
        'object_2': object_2,
    }

    # write to file
    pickle.dump(data, open('data.p', 'wb')) 

    # read from file
    data = pickle.load(open('data.p', 'rb'))

Do this
^^^^^^^

.. code:: python

    import shelve

    object_1 = 'pretend some big object 1'
    object_2 = 'pretend some big object 2'

    # write to file
    with shelve.open('data') as s:
        s['object_1'] = object_1
        s['object_2'] = object_2
        
    # read from file
    with shelve.open('data') as s:
        print(s['object_1'])
        print(s['object_2'])