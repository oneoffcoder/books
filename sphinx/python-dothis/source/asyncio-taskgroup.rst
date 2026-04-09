Use asyncio.TaskGroup for related tasks
---------------------------------------

.. highlight:: python
   :linenothreshold: 1

Use ``asyncio.TaskGroup`` instead of managing related tasks manually.

Task groups make the lifetime of related concurrent work explicit and give failures structured semantics instead of leaving cancellation and cleanup spread across the call site. That usually makes async code easier to reason about because the tasks that belong together are created, awaited, and torn down in one block.

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
