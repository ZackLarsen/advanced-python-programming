# Data Abstraction

One of the most fundamental foundations of programming is that of data
abstraction.  Loosely described, this is about the separation of
high-level code that uses data (i.e., applications) versus low-level
code that implements data representation.  In this project, we'll look
at the interplay between layers as well as gain some insight about how
Python handles data abstraction through operators.

Start with the file `frac.py`.  Then, move on to the exercises in 
`ex1.py` - `ex8.py`.

## Creating a "Pythonic" Data Structure

Later parts of the project have you implement a more fully Pythonic
object that overrides various Python operators such as `+`, `-`, `*`,
and `/`.  To do this, you need to know that Python operators map to
predefined so-called "magic" or "special" methods.  Here is a short
list of some common methods and the operators that they implement:

```
a + b          # a.__add__(b)
a - b          # a.__sub__(b)
a * b          # a.__mul__(b)
a / b          # a.__truediv__(b)
a == b         # a.__eq__(b)
a <= b         # a.__le__(b)
a < b          # a.__lt__(b)
a >= b         # a.__ge__(b)
a > b          # a.__gt__(b)
repr(a)        # a.__repr__()
hash(a)        # a.__hash__()
```

Sometimes the math operators are applied in reverse order if they're
not implemented on the left-hand side.  For that, the following
methods might also be required:

```
a + b         # b.__radd__(a)
a - b         # b.__rsub__(a)
a * b         # b.__rmul__(a)
a / b         # b.__rtruediv__(a)
```

## Controlling Attribute Access

In certain exercises, you may be asked to more tightly control access
to object attributes.  There are various ways to do this.  First, you
could override the following special methods:

```
a.__getattribute__(name)       # Implements: a.name
a.__setattr__(name, value)     # Implements: a.name = value
a.__delattr__(name)            # Implements: del a.name
```

Alternatively, you can redefine attribute access using a property

```
class Spam:
   @property
   def name(self):
       print('getting')
   @name.setter
   def name(self, value):
       print('setting', value)
   @name.deleter
   def name(self):
       print('deleting')
```

## Duck Typing

One really important idea about data in Python is that of "duck
typing."  Python's operators usually just "work" as long as the
provided datatypes implement them.  Consider the following function:

```
def add(a, b):
    return a + b
```

It works with literally any set of arguments that implements `+`.  For
example:

```
>>> add(2, 3)
5
>>> add("two", "three")
'twothree'
>>> add([2,2], [3,3,3])
[2, 2, 3, 3, 3]
>>>
```

In some sense the magic methods are Python's mechanism for data
abstraction.  If you provide an object that properly implements the
required abstraction layer (in the form of magic methods), it will
work.




