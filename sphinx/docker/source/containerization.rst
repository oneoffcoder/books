Containerizing Applications
===========================

One major use of containerization is to build shippable containers out of applications. Here, we show how to containerize an ``Angular`` application and a ``Flask`` application.

Angular
-------

Create
^^^^^^

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
   :language: docker
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

Flask
-----

