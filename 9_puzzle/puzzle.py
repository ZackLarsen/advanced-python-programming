# puzzle.py
#
# Objectives:   
# 
# In this project, we explore linguistic abstraction.  Sometimes when
# solving a problem, it makes sense to define a domain-specific
# language.  There are many angles on doing that in Python.  For
# instance, you can use Python itself as the language, redefining its
# various operators via special methods. Or you can use various
# metaprogramming features such as decorators, code inspection,
# metaclasses, etc.
#
# Consider the following logic puzzle:
#
# Baker, Cooper, Fletcher, Miller, and Smith live on different floors
# of an apartment house that contains only five floors. Baker does not
# live on the top floor. Cooper does not live on the bottom
# floor. Fletcher does not live on either the top or the bottom
# floor. Miller lives on a higher floor than does Cooper. Smith does
# not live on a floor adjacent to Fletcher's. Fletcher does not live on
# a floor adjacent to Cooper's. Where does everyone live?

# -----------------------------------------------------------------------------
# Exercise 1 - Brute force
#
# Write a program that finds all solutions to the problem.  The program
# should output the floor on which each person lives.
#
# To do this, think about a brute force solution. You know that Baker,
# Cooper, Fletcher, Miller, and Smith all live on different floors
# of an apartment.  One way to solve it would be to cycle through
# all permutations of the floors and to enforce the various rules 
# as a series of constraints.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Exercise 2 - Bending the rules
#
# Sometimes when faced with a complicated problem domain, it makes sense
# to abstract things into a kind of domain-specific language.  For example,
# one way to express the above logic puzzle is as a series of definitions
# and constraints expressed as expressions:
#
#    # Definitions of possible values
#    baker = {1, 2, 3, 4, 5}
#    cooper = {1, 2, 3, 4, 5}
#    fletcher = {1, 2, 3, 4, 5}
#    miller = {1, 2, 3, 4, 5}
#    smith = {1, 2, 3, 4, 5}
#
#    # -- Constraints
#    require(distinct(baker, cooper, fletcher, miller, smith))
#    require(baker != 5)
#    require(cooper != 1)
#    require(fletcher != 1 and fletcher != 5)
#    require(miller > cooper)     
#    require(abs(smith-fletcher) > 1)
#    require(abs(fletcher-cooper) > 1)
#
# Python has a wide range of metaprogramming features (e.g.,
# decorators, metaclasses, etc.) that allow you to change the way that
# functions and classes work.  Sometimes these features can be used
# to bend the rules a bit--or a lot.
#
# That's your challenge in this exercise: Can you implement a logic
# puzzle solver in the form a function decorator?  Like this:
#
# @solver
# def multi_dwelling(baker, cooper, fletcher, miller, smith):
#     require(distinct(baker, cooper, fletcher, miller, smith))
#     require(baker != 5)
#     require(cooper != 1)
#     require(fletcher != 1 and fletcher != 5)
#     require(miller > cooper)
#     require(abs(smith-fletcher) > 1)
#     require(abs(fletcher-cooper) > 1)
#
# solutions = multi_dwelling(
#     baker={1, 2, 3, 4, 5},       # possible values for each variable
#     cooper={1, 2, 3, 4, 5},
#     fletcher={1, 2, 3, 4, 5},
#     miller={1, 2, 3, 4, 5},
#     smith={1, 2, 3, 4, 5}
# )
#
# for soln in solutions:
#     print(soln)
#
# As output the "solver" function should return an iterable (or generator)
# that produces all of the solutions that can be found.  Each solution
# should a dictionary.  For example, in the above code, a solution
# might be a dict like:
#
#    {'baker':3, 'cooper':2, 'fletcher': 4, 'miller': 5, 'smith': 1 }
#
# The basic idea is that you just call the function with arguments set
# to the possible values and it magically finds all solutions if there
# are any.
#
# Note: To do this, you'll need to implement the @solver decorator along
# with supporting functions such as require() and distinct()
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Exercise 3 - A Problem Class
#
# Sometimes classes can be used to define domain-specific problems.
# Can you recast your solver to work with code similar to the following?
#
# class MultiDwelling(Problem):
#    # Definitions of possible values
#    baker = {1, 2, 3, 4, 5}
#    cooper = {1, 2, 3, 4, 5}
#    fletcher = {1, 2, 3, 4, 5}
#    miller = {1, 2, 3, 4, 5}
#    smith = {1, 2, 3, 4, 5}
#
#    # -- Constraints
#    require(distinct(baker, cooper, fletcher, miller, smith))
#    require(baker != 5)
#    require(cooper != 1)
#    require(fletcher != 1 and fletcher != 5)
#    require(miller > cooper)     
#    require(abs(smith-fletcher) > 1)
#    require(abs(fletcher-cooper) > 1)
#     
# solutions = MultiDwelling()     # Create all solutions (as an iterable)
# for soln in solutions:
#     ...
#
# Hint:  There are many potential ways of tackling this problem.  However,
# you might start by playing around with __init_subclass__()
#

class Problem:
    @classmethod
    def __init_subclass__(cls):
        ...  # Do something to make it work.

class MultiDwelling(Problem):
    ...

# -----------------------------------------------------------------------------
# Exercise 4 - The Elevator Puzzle
#
# An apartment house features a elevator that services 5 floors.  The
# elevator operates in three basic modes:
#
# IDLE: The elevator is just sitting there with the doors closed.
# there are no pending requests of any kind. It is not moving in any
# direction.
#
# LOADING: The elevator is stopped, loading passengers with the
# door open.
#
# MOVING: The elevator is in motion, moving between floors.
#
# The elevator system consists of the following operational state:
#
# 1. The current floor (1-5)
# 2. Current direction of motion (UP, DOWN, NONE)
# 3. Destinations (1-5). These are buttons pressed inside the elevator car.
# 4. Up requests (1-4). These are "up" buttons pressed in the hallway.
# 5. Down requests (2-5). These are "down" buttons pressed in the hallway.
#
# There are logical constraints that dictate valid elevator operational states.
#
# 1. If there are no pending requests of any kind (destinations, up requests,
#    down requests), the elevator must be IDLE.  Conversely, the elevator
#    can not be IDLE if there are pending requests. 
#
# 2. The elevator should never be on the top floor with a direction of UP.
#    The elevator should never be on the bottom floor with a direction of DOWN.
#
# 3. If the elevator is MOVING, there must be a pending request in the
#    current direction of motion.  For example, if the elevator is
#    on floor 2 and moving up, there must be some kind of request
#    on floors 3-5.  Note: this could be any kind of request (destination
#    button or an up/down request in the hallway).
#
# 4. If the elevator is LOADING, the following rules apply:
#       a. The current floor is NOT in destinations (we're already there)
#       b. If going UP, the current floor is NOT in up requests.
#       c. If going DOWN, the current floor is NOT in down requests.
#       d. If on the top floor, the current floor is NOT in down requests.
#       e. If on the bottom floor, the current floor is NOT in up requests.
#
# Your challenge:  Write a logic specification that produces ALL possible
# *valid* elevator operational states.
# -----------------------------------------------------------------------------

# @solver
# def elevator_states(mode, floor, direction, destinations, up_requests, down_requests):
#    require(not (mode == 'IDLE' and direction != 'NONE'))
#    ...

# Uncomment when ready. You may also use your class formulation if you wish.
#
#elevators = elevator_states(
#    mode = { 'IDLE', 'LOADING', 'MOVING' },
#    floor = { 1, 2, 3, 4, 5},
#    direction = { 'UP', 'DOWN', 'NONE' },
#    destinations = ...,
#    up_requests = ...,
#    down_requests = ...
#    )

# Hint: The destinations, up_requests, and down_requests capture
# the entire state of the associated buttons.  For example, possible values
# for destinations could be:
# 
#    set(), {1}, {2}, {3}, {4}, {5}, {1, 2}, {1, 3}, ... {1, 2, 3, 4, 5}.
# 
# Technically, it is the set of all possible subsets of { 1, 2, 3, 4, 5}
# or the "power set" of { 1, 2, 3, 4, 5 }.  You might want to define
# a helper function for this.

# -----------------------------------------------------------------------------
# Exercise 5 - The Elevator Challenge
#
# In Project 5, you implemented the logic for an elevator.  In exercise 4
# above, you defined a function that produces every possible valid 
# state of the elevator according to mathematical constraints.  How
# might you put these two pieces together to create a testing framework
# for the elevator software?
#
# One possible idea: Use the elevator_states() function to create all
# valid states. Then create an Elevator object from each state and
# execute various events on it.  Does this drive the elevator into an
# invalid state?  This is a bit different than the idea of
# simulation. It's more a check to see if the elevator can somehow be
# forced to transition from a known good state to a bad state.
# -----------------------------------------------------------------------------




