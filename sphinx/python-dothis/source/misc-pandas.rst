Pandas apply and numpy vectorization
------------------------------------

.. highlight:: python
   :linenothreshold: 1

When operating over Pandas dataframes, avoid using for loops and favor the apply function and Numpy vectorization.

Don't do this
^^^^^^^^^^^^^

.. code:: python

    import numpy as np
    import pandas as pd

    np.random.seed(37)

    def get_df():
        N = 10000
        M = 50
        
        get_x = lambda x: np.random.normal(x, 1, N).reshape(-1, 1)
        get_y = lambda x: np.full(N, -1).reshape(-1, 1)
        

        X = np.hstack([get_x(x) if x < M - 1 else get_y(x) for x in range(M)])
        columns=[f'X{i}' if i < M - 1 else 'y' for i in range(M)]
        
        return pd.DataFrame(X, columns=columns)

    df = get_df()

    # standard for loop
    for row in range(len(df)):
        total = np.sum(df.iloc[row][0:df.shape[1] - 1])
        y = 1 if total > 1175 else 0
        df['y'].iloc[row] = y

.. code:: python

    import numpy as np
    import pandas as pd

    np.random.seed(37)

    def get_df():
        N = 10000
        M = 50
        
        get_x = lambda x: np.random.normal(x, 1, N).reshape(-1, 1)
        get_y = lambda x: np.full(N, -1).reshape(-1, 1)
        

        X = np.hstack([get_x(x) if x < M - 1 else get_y(x) for x in range(M)])
        columns=[f'X{i}' if i < M - 1 else 'y' for i in range(M)]
        
        return pd.DataFrame(X, columns=columns)

    df = get_df()

    # pandas iterrows
    for i, r in df.iterrows():
        total = np.sum(r[0:df.shape[1] - 1])
        y = 1 if total > 1175 else 0
        df['y'].iloc[row] = y

Do this
^^^^^^^

.. code:: python

    import numpy as np
    import pandas as pd

    np.random.seed(37)

    def get_df():
        N = 10000
        M = 50
        
        get_x = lambda x: np.random.normal(x, 1, N).reshape(-1, 1)
        get_y = lambda x: np.full(N, -1).reshape(-1, 1)
        

        X = np.hstack([get_x(x) if x < M - 1 else get_y(x) for x in range(M)])
        columns=[f'X{i}' if i < M - 1 else 'y' for i in range(M)]
        
        return pd.DataFrame(X, columns=columns)

    df = get_df()

    # pandas apply
    df['y'] = df.apply(lambda r: 1 if np.sum(r[0:df.shape[1] - 1]) > 1175 else 0, axis=1)

.. code:: python

    import numpy as np
    import pandas as pd

    np.random.seed(37)

    def get_df():
        N = 10000
        M = 50
        
        get_x = lambda x: np.random.normal(x, 1, N).reshape(-1, 1)
        get_y = lambda x: np.full(N, -1).reshape(-1, 1)
        

        X = np.hstack([get_x(x) if x < M - 1 else get_y(x) for x in range(M)])
        columns=[f'X{i}' if i < M - 1 else 'y' for i in range(M)]
        
        return pd.DataFrame(X, columns=columns)

    df = get_df()

    # numpy vectorization
    f = lambda s: 1 if s > 1175 else 0
    s = df[[c for c in df.columns if c != 'y']].values.sum(axis=1)
    df['y'] = [f(val) for val in s]
