import pandas as pd
import random

data = [[random.randint(0, 101) for _ in range(10)] for _ in range(10)]

df = pd.DataFrame(data, columns=[f'x{i}' for i in range(10)])
print(df.shape)

df.to_csv('test.csv', header=True, index=False)
