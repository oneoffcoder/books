Swarm
=====

Enable Swarm
------------

To start ``Swarm``, type in the following.

.. code:: bash

    docker swarm init

To list the nodes in the swarm.

.. code:: bash

    docker node ls

Output.

::

    ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
    16ui13y7ijoaqw6u8h05u2a2b *   ryzen               Ready               Active              Leader              19.03.3

To leave swarm.

.. code:: bash

    docker swarm leave --force


Create Swarm yaml
-----------------

The ``stack file`` is a ``YAML`` file for Swarm that is nearly identical to the syntax of ``compose file`` for ``Docker Compose``.

.. literalinclude:: _static/code/swarm/student.yml
   :language: yaml
   :linenos:

Deploy to Swarm
---------------

.. code:: bash

    docker stack deploy -c student.yml student

Output.

::

    Creating network student_default
    Creating service student_flask
    Creating service student_ng
    Creating service student_db

List services
^^^^^^^^^^^^^

.. code:: bash

    docker service ls

Output.

::

    ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
    4kkjzq525ye4        student_db          replicated          0/1                 db-app:local        *:3306->3306/tcp
    kxqhlgn38dxb        student_flask       replicated          0/1                 rest-app:local      *:5000->5000/tcp
    g2alvr797i76        student_ng          replicated          0/1                 ui-app:local        *:80->80/tcp

Stop services
^^^^^^^^^^^^^

.. code:: bash

    docker stack rm student

Output.

::

    Removing service student_db
    Removing service student_flask
    Removing service student_ng
    Removing network student_default