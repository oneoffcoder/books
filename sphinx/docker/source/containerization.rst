Containerizing Applications
===========================

One major use of containerization is to build shippable containers out of applications. Here, we show how to containerize the following applications.

* Front-end application with ``Angular`` 
* Backend application with ``Flask``
* Database with ``MySQL``

Angular
-------

The ``Angular`` application is created using `Angular CLI <https://cli.angular.io/>`_. To create the application we simply type in the following command.

.. code:: bash

    ng new ui-app

Note that all the default options are used in the interactive creation of this Angular application, as the intention is not to show how to create an Angular application, but, rather, ship one out into a container. The structure of your Angular project should look like the following.

::

    ui-app
    ├── angular.json
    ├── browserslist
    ├── e2e
    ├── karma.conf.js
    ├── node_modules
    ├── package.json
    ├── package-lock.json
    ├── README.md
    ├── src
    ├── tsconfig.app.json
    ├── tsconfig.json
    ├── tsconfig.spec.json
    └── tslint.json

The next thing to do is create a ``Dockerfile`` that will containerize this Angular application. A couple of things to note here. Notice that we have two ``FROM`` instructions. What is happening here is that we are using docker's `multi-stage build <https://docs.docker.com/develop/develop-images/multistage-build/>`_ capabilities. The first ``FROM`` builds the Angular application using the ``node:lts`` docker image, and the second ``FROM`` uses the ``nginx:alpine`` docker image to run the built application (from the first stage). The first ``FROM`` aliases the first stage as ``NodeBuilder`` so that downstream stages may reference it.

.. literalinclude:: _static/code/containerization/ng/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 1, 8

Also, note the following instructions.

* ``WORKDIR`` sets the working directory inside the container; this will be the current working path and every command inside the container will be relative to this path until changed
* ``COPY`` copies files and/or folders locally to the container; here we copy the Angular directory ``my-app`` to the container's directory ``/tmp/my-app``
* ``RUN`` executes the specified shell command inside the container; here, we install the Angular CLI, install the node libraries and then build the application (three ``RUN`` commands)

In using multi-stage build, we copy the output of the ``NodeBuilder`` stage into the ``/usr/share/nginx/html`` path of the last one.

We will also create a ``.dockerignore`` file to ignore copying files and folders that we do not want to be copied into the container. Namely, the ``dist`` and ``node_modules`` directories of the Angular applications are folders that we do not want to be copied over because they are derived and should be pulled in fresh from ``npm`` to reinforce the idea of reproducible builds, respectively. Additionally, the ``node_modules`` directory is typically very large, and if we ignore it, the ``tar`` file that is created and shipped to the local Docker server will have a reduced ``build context``. 

.. literalinclude:: _static/code/containerization/ng/.dockerignore
   :language: text
   :linenos:

We place the ``Dockerfile`` and ``.dockerignore`` files one directory up from the ``my-app`` directory. Your project should look structurally as follows.

::

    ng
    ├── Dockerfile
    ├── .dockerignore
    └── ui-app

We are now ready to build the Angular container.

.. code:: bash

    docker build -t ui-app:local .

We may now run the container as follows. Note the port mapping ``-p 80:80`` which maps the local port ``80`` to the container's port ``80``.

.. code:: bash

    docker run --rm -p 80:80 ui-app:local

Angular Download
^^^^^^^^^^^^^^^^

* :download:`Dockerfile <_static/code/containerization/ng/Dockerfile>`
* :download:`.dockerignore <_static/code/containerization/ng/.dockerignore>`

Flask
-----

Before we create, build and deploy a ``Flask`` application, we need to install some ``Python`` dependencies. Since we prefer using ``conda`` to manage our environments and dependencies for Python, we issue the following command to make sure the packages/libraries we need are available.

.. code:: bash

    conda install -y flask flask-cors

The Flask application is very simple and has only 2 files; ``config.py`` for configuration and ``app.py`` as an application entrypoint. Here's the code for ``config.py``.

.. literalinclude:: _static/code/containerization/flask/rest-app/config.py
   :language: python
   :linenos:

Here's the code for ``app.py``. As can be seen, there is only one real route ``/v1/test`` and a catch-all route.

.. literalinclude:: _static/code/containerization/flask/rest-app/app.py
   :language: python
   :linenos:

For local testing, we could run this Flask application as follows. However, we will containerize it and run it as a container.

.. code:: bash

    python app.py

The ``Dockerfile`` is defined as follows.

.. literalinclude:: _static/code/containerization/flask/Dockerfile
   :language: docker
   :linenos:

We do not do anything special in the ``Dockerfile``; we simply use the ``python:3`` container image as the base image, copy over the ``rest-app`` folder and install the dependencies using ``pip``. There is a new instruction ``CMD`` that we specify, however, and it provides us a way to specify which executable should run when the container is brought to a running state.

The ``.dockerignore`` file is defined as follows. We ignore the ``__pycache__`` directory.

.. literalinclude:: _static/code/containerization/flask/.dockerignore
   :language: text
   :linenos:


In all, the structure of the folders and files should look like the following.

::

    flask/
    ├── Dockerfile
    ├── .dockerignore
    └── rest-app
        ├── app.py
        └── config.py

To build the Flask application.

.. code:: bash

    docker build -t rest-app:local .

We may now run the container as follows. Note the port mapping ``-p 5000:5000`` which maps the local port ``5000`` to the container's port ``5000``.

.. code:: bash

    docker run --rm -p 5000:5000 rest-app:local

Flask Download
^^^^^^^^^^^^^^

* :download:`Dockerfile <_static/code/containerization/flask/Dockerfile>`
* :download:`.dockerignore <_static/code/containerization/flask/.dockerignore>`
* :download:`config.py <_static/code/containerization/flask/rest-app/config.py>`
* :download:`app.py <_static/code/containerization/flask/rest-app/app.py>`

MySQL
-----

The ``MySQL`` container is the simplest container to define. It as simple as the following. However, what may look sophisticated is how we run our new container based off of the MySQL one.

.. literalinclude:: _static/code/containerization/mysql/Dockerfile
   :language: docker
   :linenos:

To build our new database container.

.. code:: bash

    docker build -t db-app:local .

To run the container.

.. code:: bash

    docker run \
        --rm \
        -e MYSQL_ROOT_PASSWORD=oneoffcoder \
        -v `pwd`/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
        db-app:local

When running the container the you will notice the flag ``-v`` which specifies a mount. In the command above, when we run our database container, we mount the local directory ``docker-entrypoint-initdb.d`` to the container's directory ``/docker-entrypoint-initdb.d``. According to the `documentation <https://hub.docker.com/_/mysql>`_, when the database container starts, any ``SQL`` script found in ``/docker-entrypoint-initdb.d`` will be executed in alphabetical order. In our case, we have a simple ``setup.sql`` script that creates one database, one table in that database and one user for the database.

.. literalinclude:: _static/code/containerization/mysql/docker-entrypoint-initdb.d/setup.sql
   :language: sql
   :linenos:

You will also notice the flag ``-e``, which specifies a value for an environment variable. In this case, the environment variable is the root password for the ``MySQL`` database, called ``MYSQL_ROOT_PASSWORD``, and the value is ``oneoffcoder``.

When you run the database container, it will lock the terminal. Open a new terminal and you may open a shell session with the running container. First, see what is the ``Container ID`` of the running database container.

.. code:: bash

    docker ps

You should see an output like the following.

::

    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                 NAMES
    45bee317b0d0        db-app:local        "docker-entrypoint.s…"   9 minutes ago       Up 9 minutes        3306/tcp, 33060/tcp   confident_bartik

Then run the ``exec`` subcommand. Below, we use the full container ID, however, you may use only the first few characters if they uniquely identify the running container. For example, instead of using ``45bee317b0d0`` completely, you may use ``45``, ``45b``, ``45be``, and so on. If there is another container whose ID starts with ``45``, the equivocality will be stated and you must continue to use as many characters as required to distinguish which container ID you are targeting.

.. code:: bash

    docker exec -it 45bee317b0d0 /bin/bash

A shell in the container will be created. You may then use the ``mysql`` CLI to go into the database to tinker around.

.. code:: bash

    mysql -u root -poneoffcoder
    mysql -u oneoffcoder -pisthebest

The structure of the files and folders is as follows.

::

    mysql/
    ├── docker-entrypoint-initdb.d
    │   └── setup.sql
    └── Dockerfile

MySQL Download
^^^^^^^^^^^^^^

* :download:`Dockerfile <_static/code/containerization/mysql/Dockerfile>`
* :download:`setup.sql <_static/code/containerization/mysql/docker-entrypoint-initdb.d/setup.sql>`