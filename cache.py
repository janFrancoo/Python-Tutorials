from time import time
from functools import lru_cache

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache()
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n - 1) + fibonacci(n - 2)


def calc_time(func, n):
    start_time = time()
    func(n)
    finish_time = time()
    return finish_time - start_time


max_n = 40
cached = []
not_cached = []
for i in range(max_n):
    not_cached.append(calc_time(fibonacci, i))
    cached.append(calc_time(fibonacci_cache, i))

df = pd.DataFrame([cached, not_cached]).T
df.columns = ['cached', 'not cached']
print(df.tail())

sns.set()
sns.lineplot(data=df)
plt.show()
