# Owning Your Abstractions

As a programmer, it is common to define data structures--typically
in the form of a class.  For example, if you want to represent a
holding of stock, you might write a class like this:

```
class Holding:
    def __init__(self, name, shares, price):
        self.name = name
	self.shares = shares
	self.price = price
```

or, if you prefer, you could write it using a dataclass:

```
from dataclasses import dataclass

@dataclass
class Holding:
    name: str
    shares: int
    price: float
```

However, it is also common to use built-in objects such as lists and
dicts.  For example, if you wanted to represent a portfolio of stocks,
maybe a list is good enough:

```
portfolio = [ Holding('IBM', 50, 91.1), Holding('AA', 75, 34.12) ]
```

Or is it?   This project explores the idea of making your own
containers.  To start, go to the file `report.py`.   Then work on the
exercises in `ex1.py`-`ex4.py`.

## Making Custom Containers

A parts of this project involves making new objects that are
"list-like" or "dict-like." This is commonly done by implementing
classes with one or more of the following magic methods:

```
a[index]            # a.__getitem__(index)
a[index] = value    # a.__setitem__(index, value)
del a[index]        # a.__delitem__(index)

len(a)              # a.__len__()
x in a              # a.__contains__(x)

for x in a:         # i = a.__iter__(), i.__next__()
    ...
```

It might also be necessary to redefine object attribute access:

```
a.attr              # a.__getattribute__("attr")
a.attr = value      # a.__setattr__("attr", value)
del a.attr          # a.__delattr__("attr")
```
