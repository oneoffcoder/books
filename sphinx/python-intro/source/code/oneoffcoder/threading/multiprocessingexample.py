import multiprocessing as mp
import os
import random


def squared(x, queue):
    module_name = __name__
    parent_id = os.getppid()
    process_id = os.getpid()

    result = x * x

    print(f'module={module_name} : parent={parent_id} : process={process_id} : result={result}')
    queue.put(result)


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    queue = ctx.Queue()

    processes = [ctx.Process(target=squared, args=(random.randint(0, 100), queue,)) for _ in range(10)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    while queue.qsize() != 0:
        print(queue.get())
