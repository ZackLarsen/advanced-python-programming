# Input/Output

At some point, your program must perform I/O.  This project explores
some of the problems associated with low-level I/O including data
encoding, working with bytes, and the implementation of I/O protocols.

This project also explores a more fundamental design problem
concerning I/O in modern Python development--and that's the choice
between using synchronous code (i.e. threads) or the choice of using
asynchronous code (i.e., the `asyncio` module and relatives).

Go the file `protocol.py` to start the project.

## bytes and bytearrays

For low-level I/O it is common to use `bytes` and `bytearray`.  These
objects behave somewhat like a cross between a string and list of
integers.  For example:

```
>>> a = b'hello'
>>> len(a)
5
>>> a[0]
104
>>> a[1]
101
>>> ord('h')
104
>>> for c in a:
...     print(c)
104
101
108
108
111
>>> a[:4]
b'hell'
>>>
```

A `bytearray` is a mutable array of bytes and adds features similar to a list:

```
>>> a = bytearray(b'hello')
>>> a.append(33)
>>> a
bytearray(b'hello!')
>>> a.extend(b'world')
>>> a
bytearray(b'hello!world')
>>> del a[0:5]
>>> a
bytearray(b'!world')
>>>
```

A bytearray is often useful for assembling fragments of I/O into
larger messages.  For example, if you were reading data from a network
connection, you might have some code like this:

```
buffer = bytearray()
def readline(conn):
    while b'\n' not in buffer:
         buffer.extend(conn.receive(1000))
    index = buffer.find(b'\n')
    line = buffer[:index+1]
    del buffer[:index+1]
    return line
```


## asyncio

For part of this project, you need to use `asyncio`.  This is not
meant to be an `asyncio` tutorial.  The main thing you need to know is
how to run an `async` function.  For example, if you have a function
like this:

```
async def blah(x, y):
    return x + y
```

To run it, you'll need to do the following:

```
import asyncio
print(asyncio.run(blah(2, 3)))   # -> 5
```

Certain operations involving `asyncio` require the use of a special
`await` statement. For example:

```
async def countdown(n):
    while n > 0:
        print('T-minus', n)
        await asyncio.sleep(1)
        n -= 1

# Run it
asyncio.run(countdown(10))
```

## What Color is Your I/O?

One of the most fundamental problems in programming is that of
abstraction and decoupling of components. In fact, a major theme of
this entire course has focused on issues of decoupling, interactions
between parts, and other matters.  Why should I/O be any different?
If you're implementing an application, isn't the choice of I/O an
implementation detail?  Why should it matter?

Unfortunately, the choice of I/O model has created a schism in the
Python world.  Should you choose to use asynchronous code, you will
start writing so-called `async` functions like this:

```
async def greeting(name):
    print('Hello', name)
```

Asynchronous functions are different.  First, they can't be called
like a normal function.  If you try, you find that they don't do
anything:

```
greeting('Dave')         # Does nothing
```

The only way to make an `async` function run is to call it from
another `async` function using `await`.  For example:

```
async def main():
    await greeting('Dave')
```

This presents an obvious problem--who calls `main()`?  That
responsibility is left to a library such as `asyncio`.  For example,
you can do the following:

```
import asyncio
asyncio.run(main())
```

The addition of a single `async` function in your codebase has a viral
effect on almost every other function. Because such functions can only
be called from other async functions, you will find huge parts of your
code flipping to an async implementation.  None of this new code can
work with ordinary Python.  You're now firmly locked into async.

Part of this project focuses on this problem--is it possible to
implement an I/O protocol that's independent of I/O implementation.
