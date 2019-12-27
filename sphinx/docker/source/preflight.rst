Pre-Flight Checks
=================

Docker
------

Let's check to make sure ``docker`` and other components are installed and working correctly. First, check to make sure docker is installed.

.. code-block:: bash
    :linenos:

    docker --version
    
You should see an output that looks like the following.

::

    Docker version 19.03.2, build 6a30dfca03

Now, let's make sure we are able to run the ``busybox`` container.

.. code-block:: bash
    :linenos:

    docker run busybox echo "hello, world!"

The command above simply echos ``hello, world!`` back to the console.

Swarm
-----

Initialization
^^^^^^^^^^^^^^

Initialize ``swarm``.

.. code-block:: bash
    :linenos:

    docker swarm init

You should see an output as follows.

::

    Swarm initialized: current node (muo6bizx5z19kny0gswqm8jq4) is now a manager.

    To add a worker to this swarm, run the following command:

        docker swarm join --token SWMTKN-1-3qo8eradxo3oy2tjzc0odurhumk4nlpt9eoeg2gq5dwl2sh88o-bc6fpa8qeh5bsn3l0kdfip2qf 10.0.2.15:2377

    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

Service creation
^^^^^^^^^^^^^^^^

Now let's create a toy service. This service uses the ``apline:3.5`` container to ping the Google domain name servier ``8.8.8.8``.

.. code-block:: bash
    :linenos:

    docker service create --name demo alpine:3.5 ping 8.8.8.8

The output should look like the following.

::

    av2o3juacixl7zwr36wd10zzg
    overall progress: 1 out of 1 tasks 
    1/1: running   
    verify: Service converged

To see which services are running.

.. code-block:: bash
    :linenos:

    docker service ps demo

To see the logs of a service.

.. code-block:: bash
    :linenos:

    docker service logs demo


To stop the service.


.. code-block:: bash
    :linenos:

    docker service rm demo