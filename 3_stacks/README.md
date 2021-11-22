# Programming with Objects

Classes are sometimes used to define data.  However, classes are also
sometimes used to define behavior and programming interfaces.  This
project explores various facets of defining objects, relationships
between objects, designing for testability, and more.  We'll also peek
a bit inside the internal workings of an interpreter--incuding Python.

Got to the file `stacks.py` and follow the instructions inside.  The
rest of the document provides some review of Python features related
to classes.

## Review of Classes

An object is defined by a `class` statement. For example:

```
class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Example use
p = Player('Guido', 2, 3)
p.move(-1, 2)
print(p.x, p.y)    #  Prints 1 5
```

Defining an object is usually a straightforward process--just
use the `class` statement.  However, challenges start to arise once
you realize that defining code in a class can serve different kinds of
roles within a program.  For example, a class might define a
"thing."  The `Player` class above is a good example of that.
However, classes can also be used to describe a "behavior."  This is
closely coupled to the idea of defining an "interface".  For example,
you might define a class like this:

```
class Movable:
    def move(self, dx, dy):
        raise NotImplementedError()
```

This is not something that's meant to be used directly (what is an
instance of a "Movable" anyways). Instead, other classes inherit from
it to assert the existence of a behavior:

```
class Player(Movable):
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    ...
```

Such an inheritance relationship might be useful in type-checking or
performing some sort of case-analysis. For example:

```
if isinstance(p, Movable):
    p.move(dx, dy)
else:
    raise RuntimeError("Not movable!")
```

A more subtle use of a class is to define a kind of "code modifier."
This is much more subtle, but you could write something like this:

```
class DoubleSpeed:
    def move(self, dx, dy):
        super().move(2*dx, 2*dy)
```

At first glance, that looks broken.  However, it's a fragment of code
that you could combine with an existing object:

```
class SuperPlayer(DoubleSpeed, Player):
    pass
```

This is an example of something known as a "Mixin" class.  It's a
class that serves no useful purpose on its own, but can modify the
behavior of other existing classes.

## Abstract Base Classes

The `abc` module is sometimes used to define interfaces.  For example:

```
from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self, dx, dy):
        pass
```

An abstract class can not be instantiated.  For example:

```
>>> m = Movable()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Movable with abstract methods move
>>> 
```

## super()

`super()` delegates an operation to the parents (or superclasses) of a
given class.  It invokes the method that would have been invoked on a
class had it not been defined.  For example:

```
class Base:
    def yow(self):
        print('Base.yow')

class Child(Base):
    def yow(self):
        print('Child.yow')
        super().yow()           # Calls Base.yow()
```

There are some subtle features of `super()` when it is used with
multiple inheritance.  Specifically, consider the following
arrangement of classes:

```
class Base:
    def yow(self):
        print('Base.yow')

class A(Base):
    def yow(self):
        print('A.yow')
        super().yow()

class B(Base):
    def yow(self):
        print('B.yow')
        super().yow()

class C(A, B):
    def yow(self):
        print('C.yow')
        super().yow()

c = C()
c.yow()     # What gets printed????
```

Looking at this code, there are four definitions of `yow()`.  You
might start to wonder what happens in the final operation (`c.yow()`).
Surprisingly, it causes all four implementations to execute.  You'll get
this output:

```
C.yow
A.yow
B.yow
Base.yow
```

We'll talk more about why this happens as we work on the project.
However, the order is the same order as classes are listed in
`C.__mro__`.  Inspect it:

```
>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
>>>
```

## getattr()

Another method that's sometimes used on a class is `getattr()`.  This
is sometimes used as an alternative mechanism of attribute lookup.
For example:

```
p = Player('Guido', 3, 4)
print(getattr(p, 'x'))   # -> 3
print(getattr(p, 'y'))   # -> 4

# Can also be used to access methods
getattr(p, 'move')(-1, 2)
```

There are some unusual uses for `getattr()` that get covered in later
parts of the project.

