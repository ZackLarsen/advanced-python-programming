# The Cycle of Life

Objects are created, used, and destroyed.   This project continues our
exploration of programming with objects, but focuses on issues related
to object creation, destruction, and related topics.   Many of the 
problems faced here are nuanced and subtle.  Expect to have a lot of
conversation surrounding the solutions we come up with.

Go to the file `message.py` to start the project.  The rest of
this document provides some background on Python.

## Object Initialization

Most programmers know about classes and the `__init__()` method which
initializes an object:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)         #  Triggers Point.__init__(self, 2, 3)
```

However, this is only part of the story. 

## The Object Lifecycle

Consider the following operation in the above code:

```
p = Point(2, 3)
```

What actually happens is the following.  First, `Point` (the class) is
used as a callable--meaning a function call.  Function call in Python
is implemented using the special method `__call__()`.  So, the first
thing that happens is `Point.__call__(2, 3)`.  You can try this
yourself:

```
>>> p = Point.__call__(2, 3)
>>> p
<__main__.Point object at 0x10f35da90>
>>> p.x
2
>>> p.y
3
>>>
```

You've probably never thought about this before when it comes to
classes. To be sure, there are subtle details of how it works (for
instance the fact that `Point` doesn't contain the definition of a
`__call__()` method), but don't worry about that for now.

The `__call__()` method is responsible for actually creating the
instance and calling the `__init__()` function.  Internally, this is
performed in two different steps:

```
self = Point.__new__(Point, 2, 3)        # Create the instance itself
self.__init__(2, 3)                      # Execute the __init__() method
```    

Again, this is something you could try on your own.  Try it in the
interactive terminal:

```
>>> p = Point.__new__(Point, 2, 3)
>>> p
<__main__.Point object at 0x10f35da90>
>>> p.x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Point' object has no attribute 'x'
>>> p.__init__(2, 3)
>>> p.x
2
>>>
```

Most programmers never see the `__new__()` method.  That's something
that's usually predefined and hidden behind the scenes.  A class
normally only implements `__init__()`.

Once the instance is alive, it carries an internal reference
count. Assignment operations increase the reference count.

```
a = Point(2, 3)     # a: refcount = 1
b = a               # b: refcount = 2     (refers to a)
c = [10, 20, b]     # c[2]: refcount = 3  (refers to a)
```

You can view the ref count using `sys.getrefcount(x)`.  Any operations
that destroy a reference decrease the reference count. These include
the `del` operator, reassignment of a value, etc.  When the reference
count reaches 0, the `__del__()` method is triggered.  Normally this
isn't defined on a class.  However, if you define it, you can see when
an object is destroyed. For example:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __del__(self):
        print('Destroying Point')

>>> p = Point(2, 3)
>>> del p
Destroying Point
>>>
```

## Alternate Constructors and Class Methods

Sometimes a class needs to define an alternate constructor that
bypasses the usual `__init__()` method or does some other special
processing for some reason.  A common approach is to define a class
method like this:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_complex(cls, c):
        self = cls.__new__(cls)
        self.x = c.real
        self.y = c.imag
        return self

# Example
p = Point.from_complex(3 + 4j)
```

## Context Managers

Resource management of objects is sometimes more carefully controlled
with context managers and the `with` statement. You commonly encounter
it with files.

```
with open(filename) as file:
    data = file.read()
```

Under the hood, the above code translates to the following:

```
tmp = open(filename)
file = tmp.__enter__()
data = file.read()
tmp.__exit__(None, None, None)
```

The purpose of `__enter__()` and `__exit__()` is to monitor and clean
up resources.  For files, the `__exit__()` method closes the file.

You can make your own context manager by defining these methods on
your own class:

```
class Manager:
     def __enter__(self):
         return self
	 
     def __exit__(self, ty, val, tb):
         if ty is not None:
             # An error occurred
             # ty = Exception type
             # val = Exception value
             # tb = Traceback
```

A benefit of a context manager is that you get more precise control
over resource use.  The `__exit__()` method will always be called when
control leaves a `with` block.  This is more predictable than relying
on the invocation of `__del__()` during garbage collection.

