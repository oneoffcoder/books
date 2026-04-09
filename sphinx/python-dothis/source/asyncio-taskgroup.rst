Use asyncio.TaskGroup for related tasks
---------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``asyncio.TaskGroup`` instead of managing related tasks manually.

.. note::

   Python 3.11+

Don't do this
^^^^^^^^^^^^^

.. code:: python

    tasks = [
        asyncio.create_task(fetch_user()),
        asyncio.create_task(fetch_orders()),
    ]
    user, orders = await asyncio.gather(*tasks)

Do this
^^^^^^^

.. code:: python

    async with asyncio.TaskGroup() as tg:
        user_task = tg.create_task(fetch_user())
        orders_task = tg.create_task(fetch_orders())

    user = user_task.result()
    orders = orders_task.result()
