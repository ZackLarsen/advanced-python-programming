# Composition of Functions

Up to this point, a lot of our discussion has focused on objects and
the way in which objects can be put together (inheritance,
composition, etc.).  However, a similar focus on "composition" can
also be applied to functions.  For example, functions can be passed
around and interact with other functions in unusual ways.  Studying
this interaction is often at the foundation of a lot of "functional
programming" but it's also useful to think about when creating
APIs.

This project explores some subtle aspects involving the evaluation
of functions and the interplay between functions.  It also starts
to introduce some ideas involving concurrency and threads.

Look at the file `returns.py` to start and then proceed through
`ex1.py` - `ex7.py`. 

## Overview of Functions

One of the most common things we do as programmers is write functions.
For example:

```
def square(x):
    return x * x

print(square(10))
```

A function takes inputs and returns a result. It all seems simple
enough. Well, until it's not.

## Higher Order Functions

Functions can be passed around as data, just like numbers or strings.
So, a function can be passed as an argument to another function.  For
example:

```
def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print('Hello world!')

after(10, greeting)
```

Functions can also be returned as results.  For example:

```
def make_adder(delta):
    def add(x):
        return x + delta
    return add

g = make_adder(10)
g(3)    # -> 13
g(30)   # -> 40
```

When returning a function, it remembers values from the definition
environment.  So the `g()` function above remembers the value of
`delta` that was provided to `make_adder()`.  This is sometimes known
as a "closure."

## Composition of Functions

Suppose that you have two functions like this:

```
def square(x):
    return x * x

def tenx(x):
    return x * 10
```

These functions can be composed together by defining a new function like this:

```
# Compute 10 times the square of x
def f(x):
    return tenx(square(x))
```

This is effectively defining a chain of computation.  The input `x` is
first fed to `square(x)`. The result of that is then fed to the
function `tenx()`.  This is not always a common technique in Python,
but sometimes you see it with string processing.  For example:

```
t = s.lower().replace('.', ' . ').replace(',', ' , ').split()
```

## Exceptions

Python uses exceptions to signal errors.  For example:

```
>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>>
```

Exceptions can be caught using `try-except`.  For example:

```
try:
    y = sqrt(x)
except ValueError as err:
    print("It didn't work. Reason:", err)
```

## Chained Exceptions

Python functions signal errors via exceptions.  It is possible for
exceptions to be nested and to be chained together.  Try this example
and see what happens:

```
def fail():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError("It failed") from e

fail()
```

Here, the result will be a "chained exception".  You should get a
traceback that includes information about both of the exceptions that
occurred.  If you want to unwind the exception, you can access the
`__cause__` attribute.  For example:

```
try:
    fail()
except RuntimeError as err:
    print("It failed. The reason why was", err.__cause__)
```

## Threads

Later parts of the project involve threads.  This is not meant to be a
full-fledged tutorial on thread programming.  But here are a few basic
concepts.

To launch a thread, you create a `Thread` object using the `threading`
library.  For example:

```
import threading
import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        time.sleep(5)
        n -= 1

t = threading.Thread(target=countdown, args=[10])
t.start()
```

Once started, a thread runs in the background on its own.  You're now
free to do other things in your program.  If you want to wait for a
thread to finish, use `t.join()`.

If you want a thread to pause or wait until you signal it, use an
`Event`.  For example:

```
import threading
import time

def countdown(n, evt):
    print("Waiting to start")
    evt.wait()
    while n > 0:
        print('T-minus', n)
        time.sleep(5)
        n -= 1

evt = threading.Event()
t = threading.Thread(target=countdown, args=[10, evt])
t.start()

print("Yawn")
time.sleep(30)

# Does not start counting until this step occurs
print("Ok begin")
evt.set()
```

If you want to pass data between threads, it is common to use a
`Queue` from the `queue` module. For example:

```
import threading
import time
import queue

def counter(n, q):
    while n > 0:
        q.put(n)
        time.sleep(5)
        n -= 1
    q.put(None)

def printer(q):
    while True:
        n = q.get()
        if n is None:
            break
        print('T-minus', n)
    print('Blastoff!)

q = queue.Queue()
t1 = threading.Thread(target=counter, args=[10, q])
t2 = threading.Thread(target=printer, args=[q])
t1.start()
t2.start()
```

