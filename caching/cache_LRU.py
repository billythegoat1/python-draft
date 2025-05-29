import functools
import timeit
import random

@functools.lru_cache
def sum_digits(numbers):
    return sum(
        int(digit) for number in numbers for digit in str(number)
    )


numbers = tuple(random.randint(1, 1000) for _ in range(1_000_000))

print(timeit.timeit(
    "sum_digits(numbers)",
    globals=globals(),
    number=1
))

print(timeit.timeit(
    "sum_digits(numbers)",
    globals=globals(),
    number=1
))

"""
The cache decorator has a minimum size of 128 values calculated.

We can set the size on the decorator like this: @functools.lru_cache(maxsize=5) or 

maxsize = None to not set a size at all.
"""