Quickstart
==========

Dockerfile
----------

All ``docker`` containers are defined through a ``Dockerfile``. A ``Dockerfile`` has a set of predefined ``instructions`` or ``directives`` that declares how the container should be built, its state, as well as its runtime behavior. The `official Dockerfile reference <https://docs.docker.com/engine/reference/builder/>`_ is avaible. The most important instruction is ``FROM``, which defines which ``base image container`` your container will be based. Below, we the base image is ``busybox``. The ``LABEL`` instruction specifies ``metadata`` in a ``key-value`` pair way for the container.

.. literalinclude:: _static/code/quickstart/Dockerfile
   :language: docker
   :linenos:

The file may be :download:`downloaded <_static/code/quickstart/Dockerfile>`.

Docker CLI
----------

To build this container, we will use the ``docker`` commandline interface ``CLI``. The `docker CLI <https://docs.docker.com/engine/reference/commandline/cli/>`_ has many ``subcommands`` that you should be familiar with. Here are a few docker CLI subcommands commonly used.

* ``build`` builds a docker image
* ``run`` runs a docker image
* ``ps`` is like the linux ps (``process status``) command and shows the container statuses
* ``exec`` executes a command against a running container
* ``stop`` stops a running container
* ``rm`` removes a container
* ``pull`` retrieves a docker image 
* ``push`` publishes a docker image
* ``images`` lists all the images downloaded
* ``login`` log into the `Docker Hub <https://hub.docker.com/>`_ repository.
* ``search`` searches for docker images.

Build
-----

Let's build the docker container and type in the following. Note the options.

* ``--no-cache`` specifies to not use the cache (always build)
* ``-t`` specifies the tag, which is ``donothing:local``
* ``.`` specifies the root directory to start building from (the current)

.. code:: bash

    docker build --no-cache -t donothing:local .

You should see an output like the following.

::

    Sending build context to Docker daemon  2.048kB
    Step 1/4 : FROM busybox
    ---> 020584afccce
    Step 2/4 : LABEL "author"="One-Off Coder"
    ---> Running in af8fdeea4744
    Removing intermediate container af8fdeea4744
    ---> 8424b50d2202
    Step 3/4 : LABEL "version"="0.0.1"
    ---> Running in 81f29ec03010
    Removing intermediate container 81f29ec03010
    ---> d57b4186fb56
    Step 4/4 : LABEL "description"="A do nothing container."
    ---> Running in 4208567a8939
    Removing intermediate container 4208567a8939
    ---> a8f8fc8d975c
    Successfully built a8f8fc8d975c
    Successfully tagged donothing:local

Run
---

To run this container, type in the following.

.. code:: bash

    docker run donothing:local

Since this container does nothing, after running the command above, the container simply exits. You should check that the container indeed did run and exited.

.. code:: bash

    docker ps -a

Your output should resemble the following.

::

    CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                          PORTS               NAMES
    42dcc9fe23b5        donothing:local     "sh"                     About a minute ago   Exited (0) About a minute ago

If we wanted to start this container and go into its shell, we may type in the following. Note the flags we pass into the ``run`` subcommand.

* ``-i`` runs the container in interactive mode
* ``-t`` creates a tty terminal
* ``--rm`` automatically removes the container when it exits

.. code:: bash

    docker run -i -t --rm donothing:local /bin/sh


If we wanted to use this container to do something like ``echo`` or ``ping`` we may type in the following.

.. code:: bash

    docker run --rm donothing:local echo "hello, world!"

.. code:: bash

    docker run --rm donothing:local ping 8.8.8.8

Tagging
-------

After you define and build a docker container, you may want to tag it for publication to a docker registry. To tag the container, type in the following.

.. code:: bash

    docker tag donothing:local oneoffcoder/donothing:0.0.1
    docker tag donothing:local oneoffcoder/donothing:latest

Note that we simply tag the already tagged image ``donothing:local`` to two new tags.

* ``oneoffcoder/donothing:0.0.1``
* ``oneoffcoder/donothing:latest``

Note the namespace ``oneoffcoder`` followed by a forward slash ``/``. This tagging convention is to avoid tag collisions. Also, note that we specify two tag versions ``0.0.1`` and ``latest``. The ``0.0.1`` follows `semantic versioning <https://semver.org/>`_, or ``semver``, and the ``latest`` is to signal the latest version as well as ``default`` image that will be used when referenced without specifying a version (e.g. when pulling the image from a docker repository).

You may check to see if your tagging was successful by issuing the following command.

.. code:: bash

    docker images

Your output should look like the following.

::

    REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
    donothing               local               a8f8fc8d975c        36 minutes ago      1.22MB
    oneoffcoder/donothing   0.0.1               a8f8fc8d975c        36 minutes ago      1.22MB
    oneoffcoder/donothing   latest              a8f8fc8d975c        36 minutes ago      1.22MB
    busybox                 latest              020584afccce        3 weeks ago         1.22MB
    alpine                  <none>              f80194ae2e0c        10 months ago       4MB

Publishing
----------

Now we are ready to publish to a docker repository. We will use `Docker Hub <https://hub.docker.com/>`_ as the repository, although you may create private ones on Amazon Web Services (``AWS``) or ``Azure``. The docker repository service for these cloud service providers (``CSPs``) are shown below.

.. csv-table:: CSP Docker Repository Service
    :header: CSP, Service

    AWS, `Elastic Container Registry <https://aws.amazon.com/ecr/>`_ ``ECR``
    Azure, `Azure Container Registry <https://azure.microsoft.com/en-us/services/container-registry/>`_ ``ACR``


Before you may publish to Docker Hub, you need to create an account. After you create an account, you need to log into Docker Hub using the ``docker`` CLI.

.. code:: bash

    docker login

Now you may publish by typing in the following.

.. code:: bash

    docker push oneoffcoder/donothing:0.0.1
    docker push oneoffcoder/donothing:latest

Docker Hub 
----------

Just as in software engineering where the principle of ``code reuse`` is emphasized, in creating docker containers, it is also beneficial to reuse containers and/or build upon existing ones. Docker Hub has a plethora of published containers by major commercial vendors and products. You may use the ``search`` subcommand to search for existing images. In the example below, we search for containers related to ``Java``.

.. code:: bash

    docker search java

You should get an output like the following.

::

    NAME                                     DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
    node                                     Node.js is a JavaScript-based platform for s…   8130                [OK]                
    tomcat                                   Apache Tomcat is an open source implementati…   2564                [OK]                
    openjdk                                  OpenJDK is an open-source implementation of …   1998                [OK]                
    java                                     Java is a concurrent, class-based, and objec…   1976                [OK]                
    ghost                                    Ghost is a free and open source blogging pla…   1062                [OK]                
    jetty                                    Jetty provides a Web server and javax.servle…   319                 [OK]                
    groovy                                   Apache Groovy is a multi-faceted language fo…   80                  [OK]                
    lwieske/java-8                           Oracle Java 8 Container - Full + Slim - Base…   45                                      [OK]
    nimmis/java-centos                       This is docker images of CentOS 7 with diffe…   42                                      [OK]
    fabric8/java-jboss-openjdk8-jdk          Fabric8 Java Base Image (JBoss, OpenJDK 8)      28                                      [OK]
    frekele/java                             docker run --rm --name java frekele/java        12                                      [OK]
    blacklabelops/java                       Java Base Images.                               8                                       [OK]
    bitnami/java                             Bitnami Java Docker Image                       5                                       [OK]
    cloudbees/java-with-docker-client        Java image with Docker client installed, use…   4                                       [OK]
    rightctrl/java                           Oracle Java                                     3                                       [OK]
    zoran/java10-sjre                        Slim Docker image based on AlpineLinux with …   2                                       [OK]
    cfje/java-resource                       Java Concourse Resource                         1                                       
    cfje/java-buildpack                      Java Buildpack CI Image                         1                                       
    cfje/java-test-applications              Java Test Applications CI Image                 1                                       
    buildo/java8-wkhtmltopdf                 Java 8 + wkhtmltopdf                            1                                       [OK]
    dwolla/java                              Dwolla’s custom Java image                      1                                       [OK]
    jelastic/javaengine                      An image of the Java Engine server maintaine…   0                                       
    cfje/java-buildpack-dependency-builder   Java Buildpack Dependencies Builder Image       0                                       
    cfje/java-buildpack-memory-calculator    Java Buildpack Memory Calculator CI Image       0                                       
    thingswise/java-docker                   Java + dcd                                      0                                       [OK]

In nearly every case, it is encouraged to reuse existing container images.