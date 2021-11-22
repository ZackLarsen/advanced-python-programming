# stacks.py
#
# Introduction
# ------------
# In an unusual shift in business strategy, management has decided
# that a full effort will be made to recreate the greatest handheld
# computer ever created--the HP 35 calculator (only sleeker and with
# BlueTooth).  HP Calculators are somewhat infamous for their use
# of RPN (https://en.wikipedia.org/wiki/Reverse_Polish_notation)
# wherein to perform a calculation such as "3 + 4", you would first
# enter 3, enter 4, and then hit the "+" key last.  The underlying 
# architecture is based on a stack.
# 
# Thus, you've been tasked with the problem of making stacks. How
# hard could it be?

# -----------------------------------------------------------------------------
# Exercise 1 - The stack
#
# Define a Stack data structure.  It should support push() and pop() operations
# that work as follows:
#
#    >>> s = Stack()
#    >>> s.push(23)
#    >>> s.push(45)
#    >>> len(s)
#    2
#    >>> s.pop()         # Returns the last item pushed
#    45
#    >>> s.pop()
#    23
#    >>> len(s)
#    0
#    >>>
# -----------------------------------------------------------------------------

def test_stack():
    s = Stack()           # You need to define the Stack class
    s.push(23)
    s.push(45)
    assert len(s) == 2
    assert s.pop() == 45
    assert s.pop() == 23
    assert len(s) == 0
    print("Good stack!")

test_stack()

# -----------------------------------------------------------------------------
# Exercise 2 - A Calculator
#
# Use your stack class to make a simple 4-function calculator.  You
# need to support four operations (add, sub, mul, and div) in addition
# to push/pop.  For example:
#
#     >>> s.push(23)
#     >>> s.push(45)
#     >>> s.add()
#     >>> s.pop()
#     68
#     >>>
#
# All math operations consume the top two items on the stack and
# replace them with the result.  Here's how you would calculate 2 * (3 + 4)
#
#     >>> s.push(2)
#     >>> s.push(3)
#     >>> s.push(4)
#     >>> s.add()
#     >>> s.mul()
#     >>> s.pop()
#     14
#     >>>
#
# Some details have been left intentionally vague. How would you implement this?
# -----------------------------------------------------------------------------

def test_calculator(calc):
    calc.push(23)
    calc.push(45)
    calc.add()
    assert calc.pop() == 68

    calc.push(2)
    calc.push(3)
    calc.push(4)
    calc.add()
    calc.mul()
    assert calc.pop() == 14

    calc.push(10)
    calc.push(3)
    calc.sub()
    assert calc.pop() == 7

    calc.push(10)
    calc.push(5)
    calc.div()
    assert calc.pop() == 2.0
    print("Good calculator!")

# For the above test, you need to create the "Calculator" instance s and pass 
# it to the above test
#
# calc = ... ???
# test_calculator(calc)            # Uncomment

# -----------------------------------------------------------------------------
# Exercise 3 - The Debate
#
# A slack-channel debate has erupted over the proper way to implement a
# stack. Chances are you used some kind of list to make your stack.
# However, "what about immutability?"  asks Peter.  "I don't like the
# fact that you can just side-step around the push()/pop() functions and
# change whatever you want inside a list."  For example:
#
#      >>> s = Stack()
#      >>> s.push(1)
#      >>> s.push(2)
#      >>> s.push(3)
#      >>> s._items[1] = 10      # Might vary on your implementation
#      >>>
#
# "But what about types?" says Arjoon. "If we're making a calculator,
# surely it should only work with numbers."  Why is this kind of mixed
# type processing being allowed?
#
#      >>> s = Stack()
#      >>> s.push('hello')
#      >>> s.push(4)
#      >>> s.push(3.5)
#      >>>
#
# Meanwhile, as this debate rages into its second week, you ask "what
# about the calculator? Which stack am I supposed to use while everyone
# debates the stack implementation?"
#
# Your task is as follows: Figure out some way to implement the Calculator
# functionality so that it works with any kind of stack that is provided.
# A couple of alternative stack implementations are provided below so you
# can test.
# -----------------------------------------------------------------------------

# An implementation of an "immutable" stack, built from tuples
class ImmutableStack:
    def __init__(self):
        self._items = None
        self._size = 0

    def push(self, item):
        self._items = (item, self._items)
        self._size += 1

    def pop(self):
        item, self._items = self._items
        self._size -= 1
        return item

    def __len__(self):
        return self._size

# An implementation of a "numeric" stack where items must be numbers
class NumericStack:
    def __init__(self):
        self._items = []
        
    def push(self, item):
        assert isinstance(item, (int, float)), "Number is required"
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

# Figure out some way to use either one of these stacks with your 
# calculator.  Make sure you can run the test_calculator() test and
# that it works without modification.
#
# test_calculator(... use ImmutableStack ...)
# test_calculator(... use NumericStack ...)

# -----------------------------------------------------------------------------
# Exercise 4 - Interfaces
#
# When designing your Calculator class to work with any kind of stack,
# the most important thing is the stack interface, not the precise
# stack implementation (that's data abstraction!). That is, you really
# only care about the operations that are expected to be implemented
# by a stack (e.g., push(), pop(), len(), etc.).
#
# How would design the Calculator class to enforce/document an
# expected interface for the associated Stack object that must be
# provided?  How would modify the various Stack implementations to
# more strictly adhere to this interface?

# -----------------------------------------------------------------------------
# Exercise 5 - Mixins
#
# Mary has lamented that all of this is "getting too complicated."
# There are now at least three different stack implementations focused on
# different problems (immutability, type checking, etc).  With a wry
# smile, she observes that the problem of type-checking could be more
# easily reduced to the following so-called "Mixin" class which would
# work in combination with any other implementation of a Stack:

class NumericStackMixin:
    def push(self, item):
        assert isinstance(item, (float, int))
        super().push(item)

# Your challenge: Show how you would use this class in combination
# with either of the other stack implementations to enforce items to
# be numbers.  For example, how could you make an immutable numeric
# stack?
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Exercise 6 - The Machine
#
# Mel has noted that the calculator object could form the basis of a simple
# virtual machine that executes an instruction sequence provided as a
# list of tuples.  Define a StackMachine class that does just this.
# -----------------------------------------------------------------------------

instructions = [
    ('push', 2),
    ('push', 3),
    ('push', 4),
    ('mul',),
    ('add',),
]

class StackMachine:
    ... # you define
    def run(self, instructions):
        ... # you define

def test_stack_machine():
    mach = StackMachine()    # Might need additional args
    result = mach.run(instructions)
    assert result == 14
    print("Good machine!")

# Uncomment
# test_stack_machine()

# -----------------------------------------------------------------------------
# Exercise 7 - The Parser (Challenge)
#
# "What is this madness with stack machines???!?!? Everyone knows that
# normal people want to use standard math notation like 2 + 3 * 4.
# Can't you make that work instead?"
# 
# Undeterred, you realize that Python has a standard library "ast" that
# can be used to parse expression strings into a tree structure.  From
# there, perhaps you can generate the appropriate stack instructions by
# walking the tree.  For example, suppose you have a tree node representing
# a binary operator like +:
#
#           Add
#          /   \
#       left  right
# 
# You can perform the calculation by imagining yourself at the calculator:
#
#      push left
#      push right
#      add
#
# Your challenge is to write Python code that can take arbitrary math
# expressions involving numbers and turn them into stack machine
# instructions.  To do this, study the output of ast.parse() below for
# a bit.  Think about how you might write code to traverse the tree
# structure in some way.
# -----------------------------------------------------------------------------

def parse_challenge():
    import ast
    tree = ast.parse("1.0 + (2 * (3 - (4 / (5 + (6 * (7 - (8 / 9)))))))", mode='eval')

    # Study this output
    print(ast.dump(tree))

    # Make instructions (somehow)
    instructions = []

    # Run the instructions
    s = StackMachine()
    result = s.run(instructions)
    print(result)

# Uncomment
# parse_challenge()    




        

        
