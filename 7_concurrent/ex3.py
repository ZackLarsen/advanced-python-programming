# -----------------------------------------------------------------------------
# Exercise 3 - Coordination 
#
# With concurrency, you often have tasks that need to coordinate with each
# other in some way.  A common technique for doing that is to use a 
# Queue.  A Queue has methods .put() and .get() that add and remove items
# from the queue respectively.  The .get() method is special in that it
# waits (blocks) until data becomes available if the queue is empty.
#

def producer(q):
    for i in range(5):
        print('Producing', i)
        q.put(i)
        time.sleep(1)            
    q.put(None)
    print('Producer done')

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('Consuming', item)
    print('Consumer done')

def test_prod_cons():
    q = Queue()       # You must define
    run(producer(q))  # Pseudocode
    run(consumer(q))  # Pseudocode

# The expected output of the program is as follows:
#
#     Producing 0
#     Consuming 0
#     Producing 1
#     Consuming 1
#     Producing 2
#     Consuming 2
#     Producing 3
#     Consuming 3
#     Producing 4
#     Consuming 4
#     Producer done
#     Consumer done

# -----------------------------------------------------------------------------
# YOUR TASK:
#
# Your task: implement a Queue class that can be used to implement a
# classic produce/consumer problem as illustrated in the above functions.
#
# You are not allowed to use any existing Python libraries.  And certainly
# not the built-in threading or queue modules.
#
# You *MAY* use the code your wrote in Exercise 2, but you may *NOT* modify it.
# Moreover, you *MAY* modify the implementation of producer() and
# consumer() to make it work.  Remember, we can't have any looping
# constructs so you'll need to eliminate that.

