# It's All About Time

This project starts our journey into thinking about time. In this
case, you're tasked with writing software for an event-driven
system. A major challenge is figuring out how to structure the 
parts in a way that allow the code to be adapted and tested.

## Stateful Objects

Part of this project involves the design and implementation of a
"stateful object."  In this context, a "stateful object" refers to the
idea that an object might have different operational modes.  Here is a
very simple example:

```
class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def open(self):
        if self.state != 'CLOSED':
            raise RuntimeError('Connection not closed')
        self.state = 'OPEN'

    def close(self):
        if self.state != 'OPEN':
            raise RuntimeError('Connection not open')
        self.state = 'CLOSED'

    def receive(self):
        if self.state != 'OPEN':
            raise RuntimeError('Connection not open')
        print('Receiving')

    def send(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Connection not open')
        print('Sending')
```

In this class, the behavior of each method varies according to an
internal operational state (`'CLOSED'` or `'OPEN'`).  Certain methods
might change the internal state.

Part of the challenge involves the inherent complexity of the methods.
If there are many states, each method can quickly turn into a tangled
mess of `if`-statements and conditionals.  Is there any way to NOT
code it in that way?

## Events and Time

A second problem addressed in the project concerns objects that must
respond to events and time sequencing.  For example, you might have a
class like this:

```
class Thing:
    def handle_clock_tick(self):
        ...
    def handle_button_press(self):
        ...
```

Each method might make adjustments to the internal operational state
of the object.  However, the dependence on external events can make
testing and debugging more challenging.  So, you'll have to think
about about that.

Proceed to the file `elevator.py` to start.

