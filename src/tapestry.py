import inspect
import sys
import threading
import time
import psutil
import os
from resource import *
from function_stats import Function_Stats
from peak_stats import Peak_Stats
from database import session, Base, engine
"""
    Within each line of the main func we can parse the line and 
    call each method -- hard --

    analiyze the stats of that method call

    idea -> create a decorator that takes the stats of a method and
    its children method

    main points to take -> execution time, memory consumption, 

"""
Base.metadata.create_all(engine)
# Just to check the database #


def query_all():
    x = session.query(Function_Stats).all()
    for y in x:
        print(y)
    print("Peak Stats")
    y = session.query(Peak_Stats).all()
    for x in y:
        print(x)


def log_stats(func):
    def wrapper():
        threads = []
        threads.append(threading.Thread(
            target=print_stats, args=(func.__name__, )))
        threads.append(threading.Thread(target=func,  name="mains"))
        start_time = time.perf_counter()
        [x.start() for x in threads]
        [x.join() for x in threads]
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        Peak_Stats.populate_table(func.__name__, run_time)
    return wrapper()


def print_stats(name):
    while True:
        # print(getrusage(RUSAGE_SELF))
        process = psutil.Process(os.getpid())
        mem = process.memory_info().rss / 1000000
        cpu = psutil.cpu_percent(interval=1)
        Function_Stats(name, cpu, 12.0, mem).save_to_db()
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
    rando()
    randos()


if __name__ == "__main__":
    query_all()
