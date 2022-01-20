Elastic Container Service
=========================

After you have published your docker images, you can use docker to publish your technology stack. First, you must create an ``ecs`` context.



.. code:: bash

    docker context ls
    docker context create ecs myecscontext
    docker context use myecscontext

You can then define a technology stack in a ``docker-compose.yml`` file like the following to deploy.

.. literalinclude:: _static/code/ecs/full-stack/docker-compose.ecs.yml
   :language: yaml
   :linenos:

Note that you can externalize values in a file ``.env``. 

This command will bring up your techonology stack in ECS.

.. code:: bash

    docker compose up

You can check what is running as follows.

.. code:: bash

    docker compose ps


You can bring down the cluster as follows.

.. code:: bash

    docker compose down