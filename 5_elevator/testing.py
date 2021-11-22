# -----------------------------------------------------------------------------
# The Testing Challenge
#
# One issue with the elevator software is the problem of testing it.
# Yes, you can probably write some unit tests for selected parts of
# your state machine.  However, can you be sure that you've tested
# every possible scenario of events?  Also, just what kinds of things
# can go wrong with an elevator anyways?
#
# In answering that last question, there are probably a few obvious
# "safety" issues you could envision. For example, the elevator should
# probably never move with the doors open.  Likewise, it probably
# shouldn't try to move up when already on the top floor (or down when
# at the bottom).  Other kinds of problems are more subtle.  For
# instance, you probably wouldn't want the elevator software to
# deadlock (i.e., just freeze with nothing happening at all).  Or have
# a situation where kids on two floors could launch a denial of
# service attack on the elevator by constantly pressing buttons and
# making the elevator ping-pong back and forth between just those
# floors.
# 
# One way to explore this space is to write a elevator simulator.
# Think of it as the "Game of Elevator."  The game starts with the
# elevator in some starting state.  From that starting state, any
# event could happen (i.e., any button could be pressed).  Each of
# these cause the elevator to change to a new state.  From all of
# these new states, you repeat the process to get more states and so
# on.  It's like exploring all possible moves that could occur in a
# board game.  Can you write something like this for the elevator?
# That is, can you write a simulation that runs the elevator software
# through every possible combination of runtime state, checking for
# potential problems?  This is your mission, should you choose to
# accept it.
#
