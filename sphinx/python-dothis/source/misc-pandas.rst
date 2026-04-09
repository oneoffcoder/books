Pandas apply and numpy vectorization
------------------------------------

.. highlight:: python
   :linenothreshold: 1

When operating over Pandas dataframes, avoid row-by-row Python loops. Prefer vectorized Pandas or NumPy operations. ``apply`` can be useful, but it is usually not the fastest option.

In dataframe code, the highest-leverage improvement is usually moving work from Python-level row iteration into array-oriented operations. That shift tends to improve both performance and clarity because the code starts describing whole-column transformations.

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
        df['y'].iloc[i] = y

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

    feature_columns = [c for c in df.columns if c != 'y']
    totals = df[feature_columns].sum(axis=1)
    df['y'] = np.where(totals > 1175, 1, 0)
