# member
`member` is a python library that introduces instance-stored memoized functions
## Example: Fibonacci numbers
```python
from member import member


class FibonacciSeries:
    def __init__(self, starters=(0, 1)):
        self.n = len(starters)
        for i, v in enumerate(starters):
            self.__call__[i] = v

    @member
    def __call__(self, index):
        return sum(self(index - i) for i in range(1, self.n + 1))


f = FibonacciSeries()
assert f(10) == 55
```
## What's wrong with `lru_cache`?
`functools.lru_cache` is a very powerful tool to memoize functions, and it can even work on class methods! Its weak point is that it stores the instance (`self`) as part of the the cache key, and the cache is stored in the class namespace. Meaning that unless the user calls `lru_cache.cache_clear()`, then any instance of the class that calls the memoized methods will never be deleted.
