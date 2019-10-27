from multiprocessing import Process, Lock, Queue
import os


def squared(x, lock, queue):
    module_name = __name__
    parent_id = os.getppid()
    process_id = os.getpid()

    result = x * x
    queue.put(result)

    lock.acquire()
    try:
        print(f'module={module_name} : parent={parent_id} : process={process_id} : result={result}')
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    queue = Queue(maxsize=-1)

    processes = [Process(target=squared, args=(num, lock, queue, )) for num in range(10)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    lock.acquire()
    try:
        while queue.qsize() != 0:
            print(queue.get())
    finally:
        lock.release()
