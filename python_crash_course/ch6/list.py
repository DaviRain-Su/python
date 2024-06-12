from collections.abc import Iterable
from functools import reduce
from typing import List
import functools

print("isinstance([], Iterable):",isinstance([], Iterable))
l = [x * x for x in range(1,10)]
print(l)
print("\n")
print([x * x for x in range(1,10) if x % 2 == 0])
print("\n")
print([m + n for m in "ABC" for n in "XYZ"])
d = {"x":"A", "y":"B", "z":"C"}
print([k + "=" + v for k, v in d.items()])
l = ["Hello", "World", "IBM", "Apple"]
print([s.lower() for s in l])
print([x if x % 2 == 0 else -x for x in range(1, 11)])

# Generator expression
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

for n in g:
    print(n)

def square(n):
    return n * n

# map() function
l = list(map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

def add(x, y):
    return x + y

# reduce() function
l = reduce(add, [1, 3, 5, 7, 9])
print(l)

# filter() function
def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

# sorted() function
# sorted() function can take a key function to determine the sorting criteria
l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)

def calc_sum(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
print(lazy_sum)
f = lazy_sum(1, 3, 5, 7, 9)
print(f())

def build(x, y):
    return lambda: x * x + y * y

f = build(3, 4)
print(f())

l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

# decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" %(text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute")
def now():
    print("2021-09-25")

now()
