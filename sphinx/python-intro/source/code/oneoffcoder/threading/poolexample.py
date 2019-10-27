from multiprocessing import Pool
import random


def squared(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as pool:
        results = pool.map(squared, [random.randint(0, 100) for _ in range(1000)])
        print(results)
