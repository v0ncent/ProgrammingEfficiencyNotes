# Programming Efficiency Master Notes

# Understanding Program Efficiency in relation to Time Complexity

"""
"Function of the size of the input" when refering to time, means that the time an algorithm needs to run
 (that is, the algorithm's complexity) depends on the the number of elements of the input you give to the algorithm.
"""
"""
An algorithm can be implemented in many different ways. So how can I actually measure the actual
efficiency of the algorithm?

and

I might for a given problem have different choices of algorithms, recursive vs iterative one, using
divide and conquer versus straight forward search.

3 ways you might do it:
1. Be scientists and time it!
2. We could count operations (how many operations do I use in my algorithm as a function of the size of the input)
3. abstract notion of ->ORDER OF GROWTH or BIG O Notation<-
   - Will argue that this is the most appropriate way of assessing the impact of choices of algorithm in
     solving a problem; and in measuring the inherent difficulty in solving a problem.
"""
# an example with 1.Timing

import time  # we can import the time module because python provides us with a timer


# an example of a algorithm that converts Celsius to Fahrenheit

def c_to_f(c):
    return c * 9 / 5 + 32

print(
    "An example using 1.Timing"
)
t = time.time()  # start clock
c_to_f(100000)  # call function
print("t=", t, "s,") # print out how long it takes

"""
Here is the problem with this method

Its not a bad idea, but again the goal is to evaluate algorithms
Do different algorithms have different amounts of time associated with them?

If I measure running time it will certainly vary as the algorithm changes, this is good but
one of the problems is that it will also vary as a function of the implementation.

Worse is, timing will depend on the computer. It will vary from device to device

And running time is NOT PREDICTABLE base on small inputs

So time varies for different inputs but cannot really express a relationship
between inputs and time.
"""
"""
Lets abstract that ^

To abstract this, we will identify a set of primitive operations
One of the obvious ones is, what does the machine do for me automatically,
Assume these steps take constant time: 
    - things like math operations (+,-,...)
    - comparisons something equal to another thing or < >
    - assignments, set a name to a value
    - retrieval from memory
The nice thing about this is then now it doesnt matter what machine im using when I assume these things, im measuring
how long the algorithm takes by counting how many operations of this type are done inside of the algorithm and im going to
use that count to come up with a number of operations executed as a function of the size of the input.
"""
# An example using 2. Counting Operations
