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

Angular applications manage configuration as a first class citizen through `envrionment files <https://angular.io/guide/build>`_. If you use the `Angular CLI <https://cli.angular.io/>`_ or ``ng-cli`` to initialize, scaffold and build your Angular application, there will be two files ``environment.ts`` and ``environment.prod.ts`` where you may declare the development and production settings for using with ``ng build``. After you build your application (e.g. with either ``ng build`` or ``ng build --prod``), a distribution will be created. In this example, we set ``environment.ts`` and ``environment.prod.ts`` to be as follows.

.. literalinclude:: _static/code/runtime/ng/ui-app/src/environments/environment.ts
   :language: typescript
   :linenos:

The code to acquire these environment variables are stored in ``app.component.ts``.

.. literalinclude:: _static/code/runtime/ng/ui-app/src/app/app.component.ts
   :language: typescript
   :linenos:

The HTML rendering/presentation code is in ``app.component.html``.

.. literalinclude:: _static/code/runtime/ng/ui-app/src/app/app.component.html
   :language: html
   :linenos:

Here is what the files for ``ng build`` will generate.

::

    ui-app/
    ├── favicon.ico
    ├── index.html
    ├── main-es2015.js
    ├── main-es2015.js.map
    ├── main-es5.js
    ├── main-es5.js.map
    ├── polyfills-es2015.js
    ├── polyfills-es2015.js.map
    ├── polyfills-es5.js
    ├── polyfills-es5.js.map
    ├── runtime-es2015.js
    ├── runtime-es2015.js.map
    ├── runtime-es5.js
    ├── runtime-es5.js.map
    ├── styles-es2015.js
    ├── styles-es2015.js.map
    ├── styles-es5.js
    ├── styles-es5.js.map
    ├── vendor-es2015.js
    ├── vendor-es2015.js.map
    ├── vendor-es5.js
    └── vendor-es5.js.map

Here is what the files for ``ng build --prod`` will generate.

::

    ui-app/
    ├── 3rdpartylicenses.txt
    ├── favicon.ico
    ├── index.html
    ├── main-es2015.c2c754009562ee4be6a8.js
    ├── main-es5.c2c754009562ee4be6a8.js
    ├── polyfills-es2015.2987770fde9daa1d8a2e.js
    ├── polyfills-es5.6696c533341b95a3d617.js
    ├── runtime-es2015.edb2fcf2778e7bf1d426.js
    ├── runtime-es5.edb2fcf2778e7bf1d426.js
    └── styles.3ff695c00d717f2d2a11.css

The key is in the ``main-es*.js`` files. If you reference the environment settings from within your application, they will be exported as literals in the ``main-es*.js`` files (if you do not, then ``ng build --prod`` will shake these unnecessary literals off). 

Here is a snippet from of the code in ``main-es2015.js``.

.. code-block:: javascript
    :linenos:

    var environment = {
        production: false,
        serviceUrl: 'ENV_SERVICE_URL',
        apiKey: 'ENV_API_KEY'
    };

Here is a snippet from of the code in ``main-es2015.c2c754009562ee4be6a8.js``.

.. code-block:: javascript
    :linenos:

    Ra={production:!0,serviceUrl:"ENV_SERVICE_URL",apiKey:"ENV_API_KEY"}

When the Angular static contents are placed in a webserver like ``nginx``, they have no runtime environment that will allow the code to sense the environment. The code is strictly meant to be sent back to the user's browser and then then browser interprets them, at which point, the code is away from the webserver environment, and cannot (and should not) access the environment from which they came. So then, how do we replace these files at runtime? The key is with the string literals, environment variables passed into the Docker container ``-e``, and string substitution. Let's see how we may use these elements to modify the string literals at runtime.

This ``override.py`` file will acquire environment variables and substitute the string literals in ``.js`` and ``.map`` files.

.. literalinclude:: _static/code/runtime/ng/override.py
   :language: python
   :linenos:

This ``override.ini`` file specifies the ``override`` service for ``supervisor``.

.. literalinclude:: _static/code/runtime/ng/override.ini
   :language: ini
   :linenos:

This ``nginx.ini`` file specifies the ``nginx`` service for ``supervisor``.

.. literalinclude:: _static/code/runtime/ng/nginx.ini
   :language: ini
   :linenos:

This is the ``Dockerfile``. In the container, we copy over the ``*.ini`` and ``*.py`` files. Additionaly, install the ``supervisor`` service to help us do multiple things; namely, perform the string substitution with Python and then run ``nginx``.

.. literalinclude:: _static/code/runtime/ng/Dockerfile
   :language: docker
   :linenos:

Build the container.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t ui-app:local .

Run the container without any environment specification.

.. code-block:: bash
    :linenos:

    docker run -it --rm -p 80:80 ui-app:local

Run the container with environment specification.

.. code-block: bash
    :linenos:

    docker run -it --rm \
        -p 80:80 \
        -e ENV_SERVICE_URL="http://dummy.org" \
        -e ENV_API_KEY="adsf234kdjlfsjdkfj234" \
        ui-app:local

You may now go to `http://localhost <http://localhost>`_ and observe the runtime string substitution.

nginx
-----

``nginx`` typically runs on port ``80``. What if we want nginx to run on a different port? Again, we can use string substitution. Whereas in the Angular application we used Python, in this example, we use a simple ``bash`` script.

The ``nginx-default.conf.template`` file is the template that we want to modify and place into ``/etc/nginx/conf.d/default.conf``.

.. literalinclude:: _static/code/runtime/nginx/nginx-default.conf.template
   :language: docker
   :linenos:

The ``docker-entrypoint.sh`` script does the actual string substitution with the environment variable value.

.. literalinclude:: _static/code/runtime/nginx/docker-entrypoint.sh
   :language: docker
   :linenos:

The ``Dockerfile``. Notice how we modify ``ENTRYPOINT`` and ``CMD`` and specify a default port with ``ENV``.

.. literalinclude:: _static/code/runtime/nginx/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 3, 7-8

Build the container.

.. code-block:: bash
    :linenos:

    docker build --no-cache -t web-app:local .

Run the container on different ports.

.. code-block:: bash
    :linenos:

    docker run -p 81:81 -e PORT=81 --rm web-app:local
    docker run -p 82:82 -e PORT=82 --rm web-app:local
    docker run -p 83:83 -e PORT=83 --rm web-app:local

Depending on how you specified the port through ``-e PORT=<port>``, you may access the site as follow.

* `http://localhost:81 <http://localhost:81>`_
* `http://localhost:82 <http://localhost:82>`_
* `http://localhost:83 <http://localhost:83>`_