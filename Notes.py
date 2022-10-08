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
print("t=", t, "s,")  # print out how long it takes

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

# using what we said above we can attempt to get the function of the size of the input by counting the number
# of the above operations that happen

# example with the same function above

# def c_to_f(c):
#    return c * 9 / 5 + 32
"""
We have four steps here
1. return 2. multiplication 3. division 4. addition
so 4 steps including return statement
"""


# Another example with mySum function
def mySum(x):
    total = 0  # 1 operation
    for i in range(x + 1):  # 2 inside our loop we have in essence one operation
        total += i  # 3 we have two operations here assignment and addition
    # we are then going to go through the loop x times
    return total  # 4 if you include return statements


# so mySum has 2+3x operations

"""
This is pretty good but its not quite what we want

First of all it certainly depends on the algorithm im trying to measure,
which is what we are after

but sadly it still DEPENDS ON IMPLEMENTATION
    - Suppose we were to change mySum to have a while loop instead of a for loop
    by setting i = 0 outside of the loop and then while i is less than x + 1 do the stuff
    
    this would actually add one more operation inside of the loop,
    so we would have 2+4x operations instead of 2+3x

Another good thing is counting is independent of what computer I am on as long as they come with the 
same set of basic operations.

Another thing is there isn't a clear definition of which operations to count or not.

So counting is closer, 
count varies for different inputs and can come up with a relationship between inputs and the count
"""


# So what I want to do is just evaluate the algorithm, not the machine or the implementation
# and I especially want to understand how does it scale?

# Now comes in orders of growth and focus on that idea of counting operations but not worry about small variations
# for example we do not care about the pieces inside of our loops or not

# Sometimes the amount of time the code takes depends on the input

# an example: A function that searches for an element in a list
def search_for_elmt(lst, element):
    for i in lst:
        if i == element:
            return True
    return False


"""
This above algorithm could take minimum 3 steps, but it depends on how lucky we are

if e is the first element it only goes through those steps once and we are done. Great!
But we arent always so lucky, if the element is not in the list then it will go through this
entire loop until it gets all the way through the list before saying false

Best and worst case ^


Our best case will be the minimum amount of run time

The average case a practical measure (test it out take average of steps for many inputs)

Worst maximum running time over all possible inputs of a given size, the length of the list

But we are gonna focus on the worst case scenario
Luckily the worst case grows linearly with the input, so if I double the input I double the amount of time it takes in the worst case
This is what we will focus on

We can do this with orders of growth:
We want to evaluate efficiency particularly when the input is large

We want to express the growth of the programs runtime as the input grows (not exact runtime, but the notion if I doubled it)

We are not going to worry about being precise
"""


# 3 BIG 0 Notation

# ab example with fact_iter function
def fact_iter(n):
    """assumes n an int >= 0"""
    answer = 1  # 1 step
    while n > 1:  # 2 test n
        answer *= n  # 4 multiplication and assignment
        n -= 1  # 6 decrease and reassign
    return answer  # 6 return the answer

# total steps are 1 + 5n + 1 or 5n + 2 steps

# Worst case: ignore additive constants, ignore multiplicative constants
# We want to know what captures the way the function grows
# and that is O(n) grows linearly meaning if I do anything to the input it also increases the steps, so double input, double the steps

# Simplification examples
"""
- Drop constants and multiplicative factors
- Focus on dominant terms

for all of these if you were to plot out how these terms grow the simplified terms are going to be the dominant terms

n^2 + 2n + 2 is simplified to O(n^2)

n^2 + 100000n + 3^1000 is simplified to O(n^2)

log(n) + n + 4 is simplified to O(n) because n grows faster than log(n)

0.0001 * n * log(n) + 300n is simplified to O(n log n) 

2n^30 + 3^n is simplified to 0(3^n)
"""
"""
Analyzing programs and their complexity: 

Given a piece of code, you are going tto reason about each chunk of code separately,
combine complexity classes
    - analyze statements inside functions
    - apply some rules, focus on dominant term

Law of Addition for O():
    - used with sequential statements <--
    - O(f(n) + O(g(n)) is O(f(n) + g(n))
    - for example 
for i in range(n):
    print('a')
for j in range(n*n):
    print('b')

is o(n) + o(n*n) = O(n+n^2) = O(n^2) because of dominant term

Law of Multiplication for O():
    - used with nested statements/loops
    - O(f(n)) * O(g(n)) is O(f(n) * g(n))
    - for example
for i in range(n):
    for j in range(n):
        print('a')
        
    is O(n) * O(n) = 0(n*n) = O(n^2) becuase the outer loops goes n
    times and the inner loop goes n times for every outer loop iteration.
"""

# Complexity Classes
"""
1. O(1) denotes constant runtime (problem doesnt change run time as it grows)
2. O(log n) denotes logarithmic running time (problem grows, runtime grows logarithmically)
3. O(n) denotes linear running time (Problem grows, runtime increases linearly) (and so on)
4. O(n log n) denotes log-linear running time 
5. 0(n^c) denotes polynomial running time (c is a constant)
6. O(c^n) denotes exponential running time (c is a constant being raised to a power based on size of input)
"""
