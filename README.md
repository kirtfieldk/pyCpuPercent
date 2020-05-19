#### CPU LOGGER

The tapestry file is home to a decorator that when applied to any function, it loggs the CPU percent
of the given task.

The decorator spawns two threads, the logging thread and the orginial function thread. The decorator than places all new information into a database.

```python
from tapestry import log_stats

@log_stats("simple func")
def simple(x):
    print(x)
```
