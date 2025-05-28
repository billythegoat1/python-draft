#Manual Caching
import random
import timeit


def sum_digits(numbers):
    if numbers not in sum_digits.my_cache:
        sum_digits.my_cache[numbers] = sum(int(digit) for number in numbers for digit in str(number))
    return sum_digits.my_cache[numbers]
    

sum_digits.my_cache = {}

numbers = tuple(random.randint(1, 1000) for _ in range(1_000_000))

print(numbers)
#Time when run for the first time
print(timeit.timeit(
    "sum_digits(numbers)",
    globals=globals(),
    number=1
))

#Time when run for the second time
print(timeit.timeit(
    "sum_digits(numbers)",
    globals=globals(),
    number=1
))