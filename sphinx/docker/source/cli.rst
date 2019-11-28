Commandline Tool
================

A lot of uses for Docker containers is to containerize enterprise applications. However, commandline tools may also be built using containers. Imagine that we have learned data science models that may predict

* credit card fraud,
* when an employee will leave a company or
* if there is a network security threat.

How could we ship the model? In this example here, we mock a data science model that predicts how much a person is expected to earn per year based on the years of education they have after high-school. Let's see how shipping data science models may be done. **NOTE** This model is ``fictitious``.

Why would we want to containerize the models? 

* Ease of use: we may invoke the model easily through the Docker commandline.
* Dependencies: we may avoid setting up complicated environments and dependencies required by our predictive models.
* Portability: we may ship our model around (and sell them?).

Prediction model
----------------

The prediction program ``income-model.py`` is a Python application hosting our predictive model. It computes the expected yearly income earning as follows.

.. math::

    y = 25000 + 20000 \times e

If a person has no education after high-school, they are expected to make $25,000. The per unit increase in earning is $20,000 (per year after high-school).

.. literalinclude:: _static/code/cli/income-model.py
   :language: python
   :linenos:
   :emphasize-lines: 19

Docker container
----------------

The ``Dockerfile`` below has 2 instructions ``ENTRYPOINT`` and ``CMD``. Together, these instructions allow users to pass in the required arguments to the prediction model (which is years of education after high-school). In the Dockerfile below, ``ENTRYPOINT`` points to the executable program, and the ``CMD`` serves to pass in the arguments to the program.

.. literalinclude:: _static/code/cli/Dockerfile
   :language: docker
   :linenos:
   :emphasize-lines: 6, 7

Build the container as follows.

.. code:: bash

    docker build --no-cache -t income-model:local .

You may then run the container. Note the flag ``-e`` is required by the Python program. We could also substitute ``--education`` for ``-e`` as well. The flags after the container name and tag will be passed to the Python program and override what was originally in the ``CMD`` instruction (in the Dockerfile).

.. code:: bash

    docker run -it income-model:local -e 10

Downloads
---------

* :download:`income-model.py <_static/code/cli/income-model.py>`
* :download:`Dockerfile <_static/code/cli/Dockerfile>`