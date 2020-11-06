from multiprocessing import Pool
import random


def squared(x):
    return x * x


if __name__ == '__main__':
    numbers = [random.randint(0, 100) for _ in range(1000)]
    with Pool(5) as pool:
        results = pool.map(squared, numbers)
        print(results)
