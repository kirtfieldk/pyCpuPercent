import inspect
import sys
import threading
import time
import psutil
import os
from resource import *
"""
    Within each line of the main func we can parse the line and 
    call each method -- hard --

    analiyze the stats of that method call

    idea -> create a decorator that takes the stats of a method and
    its children method

    main points to take -> execution time, memory consumption, 

"""


def do_work():
    print_hello()


def print_hello():
    print("Hello world")


def log_stats(func):
    def wrapper():
        threads = []
        threads.append(threading.Thread(target=print_stats))
        threads.append(threading.Thread(target=func,  name="mains"))
        start_time = time.perf_counter()
        [x.start() for x in threads]
        [x.join() for x in threads]
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.6f} secs")
    return wrapper()


def print_stats():
    while True:
        print(getrusage(RUSAGE_SELF))
        process = psutil.Process(os.getpid())
        print(f"{process.memory_info().rss / 1000000} megabytes")  # in bytes
        print(f'{psutil.cpu_percent(interval=1)}%')
        if end_logger_when_main_finish():
            break


def end_logger_when_main_finish():
    """Two threads the main thread and the thread this proccess is running on"""
    if len(threading.enumerate()) == 2 and threading.enumerate()[0].name == "MainThread":
        return True
    # return False


def rando():
    for i in range(0, 10000000):
        i += i
        i += 23
    return i


def randos():
    for i in range(1, 1000000):
        i += i
        i += 23
    return i


@log_stats
def main():
    do_work()
    rando()
    randos()


if __name__ == "__main__":
    th = threading.Thread(target=main)
    th.start()
    th.join()
