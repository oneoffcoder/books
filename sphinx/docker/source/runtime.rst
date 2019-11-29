Runtime Behavior
================

When deploying containers, it is typical to modify and/or configure their states and behavior at runtime. For example, we may run a Flask application on port ``5000`` during development, but on production, we want to run it on a different port. Or, we may be using a development API key for a remote service during development, but would want to substitute for a production API key on the production cluster. 

How do we modify the states and behavior of our containers and the applications within them? The answer is typically through passing environment variables to the containers. The applications inside the containers may then reconfigure based on the environment settings. However, this approach is only available for server-side applications like Flask. What about client-side applications like Angular? An Angular application is ``transpiled`` to static content (HTML, CSS, JavaScript) and are served back to the user, and these static content resources typically do not exist in a runtime container that would enable them access to the environment. Let's investigate a couple of ways we may handle these situations.

Flask
-----

The Flask application ``app.py`` can acquire environment variables through the ``os`` package. We can supply the key and a default value when attempting to acquire an environment variable ``os.getenv(KEY, DEFAULT_VALUE)``. In this application, we get database connection parameters from the environment, and if we fail, we fallback to the application configuration. When specifying on which port the Flask application will run, we do not use the application configuration, rather, we set a default value of ``5000`` in the case that the environment variable corresponding to this value does not exists.

.. literalinclude:: _static/code/runtime/flask/rest-app/app.py
   :language: python
   :linenos:
   :emphasize-lines: 27-35, 42-43, 47

The Flask application configuration ``config.py``.

.. literalinclude:: _static/code/runtime/flask/rest-app/config.py
   :language: python
   :linenos:

The Flask ``Dockerfile`` has 5 ``ENV`` instructions corresponding to the database connection parameters. Note the values of the environment variables are the same as the values in the application configuration ``config.py``, however, they are suffixed with two underscores ``__``.

.. literalinclude:: _static/code/runtime/flask/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 3-7

Now let's build this container.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t rest-app:local .

We run the container as follows.

.. code-block:: bash
    :linenos:

    docker run -it --rm -p 5000:5000 rest-app:local

When we access the url `http://localhost:5000/v1/db <http://localhost:5000/v1/db>`_, we will see the following output. These values are the ones coming from the ``ENV`` instruction in the ``Dockerfile``.

.. code-block:: json
    :linenos:

    {
        "DB_USER":"oneoffcoder__",
        "DB_PW":"isthebest__",
        "DB_INSTANCE":"school__",
        "DB_HOST":"localhost__",
        "DB_PORT":"3333",
        "timestamp":1574985251133
    }

Let's try to override them at runtime. We use the flag ``-e`` to pass in these environment key-value pairs. Essentially, at runtime, we override what's set in ``Dockerfile`` and ``config.py``.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 3-7

    docker run -it --rm \
        -p 5000:5000 \
        -e DB_USER="alan" \
        -e DB_PW="turing" \
        -e DB_INSTANCE="ai" \
        -e DB_HOST="enigma" \
        -e DB_PORT=1729 \
        rest-app:local

Now we get the following output from `http://localhost:5000/v1/db <http://localhost:5000/v1/db>`_. Note that the numeric value ``1729`` is a string instead of a number? You will have to add logic to convert that in the Python application code.

.. code-block:: json
    :linenos:
    :emphasize-lines: 2-7

    {
        "DB_USER":"alan",
        "DB_PW":"turing",
        "DB_INSTANCE":"ai",
        "DB_HOST":"enigma",
        "DB_PORT":"1729",
        "timestamp":1574985447823
    }

How about the Flask port? How do we override that value? There was no ``FLASK_PORT`` variable set in ``Dockerfile`` or ``config.py``. We override by using ``-e`` again. Note that we will map the local port ``5000`` to the container port ``5001`` through the flag ``-p 5000:5001``.

.. code-block:: bash
    :linenos:
    :emphasize-lines: 2, 8

    docker run -it --rm \
        -p 5000:5001 \
        -e DB_USER="alan" \
        -e DB_PW="turing" \
        -e DB_INSTANCE="ai" \
        -e DB_HOST="enigma" \
        -e DB_PORT=1729 \
        -e FLASK_PORT=5001 \
        rest-app:local


Flask downloads
^^^^^^^^^^^^^^^

* :download:`app.py <_static/code/runtime/flask/rest-app/app.py>`
* :download:`config.py <_static/code/runtime/flask/rest-app/config.py>`
* :download:`Dockerfile <_static/code/runtime/flask/Dockerfile>`

Angular
-------