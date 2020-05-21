import inspect
import sys
import threading
import time
import psutil
import os
import functools
from resource import *
from function_stats import Function_Stats
from peak_stats import Peak_Stats
from database import make_tables, get_session
"""
    Within each line of the main func we can parse the line and 
    call each method -- hard --

    analiyze the stats of that method call

    idea -> create a decorator that takes the stats of a method and
    its children method

    main points to take -> execution time, memory consumption, 

"""
make_tables()


def query_all():
    session = get_session()
    x = session.query(Function_Stats).all()
    for y in x:
        print(y)
    print("Peak Stats: ")
    y = session.query(Peak_Stats).all()
    for x in y:
        print(x)


def log_stats(desc):
    def inner(func):
        def wrapper(*args, **kwargs):
            file_name = func.__code__.co_filename
            threads = []
            threads.append(threading.Thread(
                target=print_stats, args=(func, desc, file_name, )))
            threads.append(threading.Thread(target=func, args=(
                *args, ), kwargs={**kwargs}, name=func.__name__))
            start_time = time.perf_counter()
            [x.start() for x in threads]
            [x.join() for x in threads]
            end_time = time.perf_counter()      # 2
            run_time = end_time - start_time    # 3
            Peak_Stats.populate_table(func.__name__, desc, file_name, run_time)
        return wrapper
    return inner


def print_stats(func, desc, filename):
    while True:
        # print(getrusage(RUSAGE_SELF))
        process = psutil.Process(os.getpid())
        mem = process.memory_info().rss / 1000000
        cpu = psutil.cpu_percent(interval=1)
        Function_Stats(func.__name__, cpu, mem, desc, filename).save_to_db()
        if end_logger_when_main_finish(func.__name__):
            return


def end_logger_when_main_finish(name):
    """Checks when the main func is done"""
    thr = [x.name for x in threading.enumerate()]
    return name not in thr


    # return False
"""
    Need to implement functions in another file 
"""
if __name__ == "__main__":
    query_all()
