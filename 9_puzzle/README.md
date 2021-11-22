# Linguistic Abstraction

When solving complex problems, you might struggle to map the problem
to a programming language.  However, a different approach is to work
in the other direction.  Perhaps you can modify the programming
language to better fit the problem.

There's a long history of using Python as a kind of "domain specific
language."  For example, much of what happens in scientific computing
with numpy, pandas, and similar libraries is all about this--extending
Python's operators and container semantics to operate on arrays and
data frames.  Much of this is about implementing various magic methods
on classes as we did in the first few projects.

Potentially you take this even further and end up writing an entirely
new programming language.  In doing so, you'd end up reinventing
something like SQL or maybe Prolog.  We're not going to go that far.
However, we are going to explore the general idea by taking a few
small steps into Python metaprogramming. 

## Function Decorators

Function decorators are used to change the behavior of function calls.
Here's an example of using a decorator from the standard library to
implement an overloaded function that dispatches based on the type of
the first argument:

```
from functools import singledispatch

@singledispatch
def f(x):
    print("Generic f:", x)

@f.register
def _(x: int):
   print("Integer f:", x)

@f.register
def _(x: str):
   print("String f:", x)

f(2.5)     # -> Generic f
f(2)       # -> Integer f
f("hello") # -> String f
```

A decorator is usually implemented as a function that creates a
so-called wrapper function.  Here is a very basic example that shows
how to define one for logging:

```
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

# Example use

@logged
def add(x, y):
    return x + y

add(2,3)   # Should see the "Calling add" message added
```

## Class Decorator

A class decorator is often used to modify the contents of a class
body.  One example is the `@dataclass` decorator from the standard
library:

```
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(2,3)
```

A class decorator is implemented much in the same way as a function
decorator.  Here is an example of a class decorate that automatically
makes a `__repr__()` method from the signature of the `__init__()`
method.

```
import inspect

def make_repr(cls):
    sig = inspect.signature(cls)
    names = list(sig.parameters)
    # Create a repr() method and put it on the class
    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in names)
        return f'{cls.__name__}({values})'
    cls.__repr__ = __repr__
    return cls

# Example use
@make_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2,3)
print(p)     # -> Should produce "Point(2, 3)"
```

## Supervised Inheritance

A base class can supervise the definition of child classes.  Here is
an example of a base class that automatically applies the `@dataclass`
decorator:

```
from dataclasses import dataclass

class Base:
    @classmethod
    def __init_subclass__(cls):
        dataclass(cls)

# Example
class Point(Base):
    x : int
    y : int
```

Sometimes this technique is use to hide a class decorator or to
perform some other kind of magic in the inheritance process.

## eval() and exec()

The built-in `eval()` and `exec()` functions can be used to evaluate
and execute code fragments.  `eval()` is used to evaluate a string
that represents an expression (i.e., could be used on the right-hand
side of an assignment).  For example:

```
>>> a = eval('4 + 5 * 6')
>>> a
34
>>>
```

`exec()` is used to execute a string containing one or more
statements. For example:

```
>>> exec('''
for i in range(5):
    print('Hello', i)
''')
Hello 0
Hello 1
Hello 2
Hello 3
Hello 4
>>>
```

Some programmers react badly to the idea of using `eval()` and
`exec()`.  Moreover, they're often insecure if combined with
user-provided input (i.e., provided on a web form or something).
However, they're also widely used behind the scenes of common tools
like `NamedTuple`, dataclasses, and other techniques for reducing the
amount of code that you write.

## Metaclasses

Using `__init_subclass__()`, it is possible to observe class
definitions after they have been defined.  However, it is also
possible to observe a class definition as it is in the process of
being defined!  This opens up all sorts of wild possibilities, but
here is an example to show how you might do it:

```
# A custom dictionary where you can observe setting/getting

class mydict(dict):
    def __getitem__(self, key):
        print('Getting:', key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting:', key, value)
        super().__setitem__(key, value)

# A custom metaclass that injects a magic dictionary into class creation
class mytype(type):
    @classmethod
    def __prepare__(meta, *args, **kwargs):
        return mydict()

# Watch what happens
class Example(metaclass=mytype):
    def __init__(self, x):
        self.x = x

    def yow(self):
        print('Yow:', x)
```

I'll leave it to your imagination as to how you might use this
knowledge.  However, if you are clever, you can turn the body of a
class into an entirely different universe where the normal rules of
Python coding no longer apply.








