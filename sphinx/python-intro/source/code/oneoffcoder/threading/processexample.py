from multiprocessing import Process
import random
import os


def squared(x):
    module_name = __name__
    parent_id = os.getppid()
    process_id = os.getpid()

    result = x * x

    print(f'module={module_name} : parent={parent_id} : process={process_id} : result={result}')


if __name__ == '__main__':
    processes = [Process(target=squared, args=(random.randint(0, 100),)) for _ in range(1000)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
