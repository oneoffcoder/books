Swarm
=====

Enable Swarm
------------

To start ``Swarm``, type in the following.

.. code-block:: bash
    :linenos:

    docker swarm init

You should see a similar output as follows.

::

    Swarm initialized: current node (891q5gj0y69y2s1kzk01xdjzy) is now a manager.

    To add a worker to this swarm, run the following command:

        docker swarm join --token SWMTKN-1-3mwknlzd6h75b0l8e9324l3tlhi1hhn1k9cc0vklwsf937v1dq-3ri0hmvm2390rho4irbwby0ru 192.168.0.73:2377

    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

To list the nodes in the swarm.

.. code-block:: bash
    :linenos:

    docker node ls

Output.

::

    ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
    16ui13y7ijoaqw6u8h05u2a2b *   ryzen               Ready               Active              Leader              19.03.3


Set up a Docker registry
------------------------

To set up a local Docker registry, type in the following.

.. code-block:: bash
    :linenos:

    docker service create --name registry --publish published=5000,target=5000 registry:2

::

    mq4lk2beo4yz1hj8aqe2po3up
    overall progress: 1 out of 1 tasks 
    1/1: running   [==================================================>] 
    verify: Service converged

Check the status as follows.

.. code-block:: bash
    :linenos:

    docker service ls

::

    ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
    mq4lk2beo4yz        registry            replicated          1/1                 registry:2          *:5000->5000/tcp

Check that it's working.

.. code-block:: bash
    :linenos:

    curl http://localhost:5000/v2/

Publish stack
-------------

Create ``docker-compose.yml`` as follows.

.. literalinclude:: _static/code/swarm/docker-compose.yml
   :language: yaml
   :linenos:

Build.

.. code-block:: bash
    :linenos:

    docker-compose up

Publish.

.. code-block:: bash
    :linenos:

    docker-compose push

Deploy to Swarm
---------------

Now deploy the stack to the swarm.

.. code-block:: bash
    :linenos:

    docker stack deploy -c docker-compose.yml student

Output.

::

    Creating network student_default
    Creating service student_flask
    Creating service student_ng
    Creating service student_db

List services
^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    docker service ls

Output.

::

    ID                  NAME                MODE                REPLICAS            IMAGE                        PORTS
    mq4lk2beo4yz        registry            replicated          1/1                 registry:2                   *:5000->5000/tcp
    v898krzykppw        student_db          replicated          1/1                 127.0.0.1:5000/db:latest     *:3306->3306/tcp
    bgkeb2k2skpt        student_flask       replicated          1/1                 127.0.0.1:5000/rest:latest   *:5001->5000/tcp
    ypnuugzylzp7        student_ng          replicated          1/1                 127.0.0.1:5000/ui:latest     *:80->80/tcp

Inspect services
^^^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    docker service inspect --pretty student_db
    docker service inspect --pretty student_flask
    docker service inspect --pretty student_ng

Scale services
^^^^^^^^^^^^^^

.. code-block:: bash
    :linenos:

    docker service scale student_ng=5
    docker service ps student_ng

Stop services
-------------

.. code-block:: bash
    :linenos:

    docker stack rm student
    docker service rm registry

Output.

::

    Removing service student_db
    Removing service student_flask
    Removing service student_ng
    Removing network student_default

Leave swarm
-----------

To leave swarm.

.. code-block:: bash
    :linenos:

    docker swarm leave --force