# Week2 Notes 

### tips in lab01 &  hog & disc01 & hw02

**Using python**
- run command -> `python lab.py` 
- open an interative session -> `python -i lab.py` 
- run doctest in a particular file -> `python -m doctest lab.py`

**Using OK**
- use *OK* to run doctests for a specified function -> `python ok -q <specified function name>`
- Default, test all function -> `python ok -v`
- debug printing feature -> `print("DEBUG:",x)`

*Q2: Accumulate*
**Takeaway:** Notice how quick it is now to create accumulator functions with different merger functions! This is because we `abstracted` away the logic of product and summation into the accumulate function. Without this abstraction, our code for a summation function would be just as long as our code for the product function from Question 1, and the logic would be highly redundant!

**Lambda function(record)**
```py
def mod_maker():
    """Return a two-argument function that performs the modulo operation and
    returns True if the numbers are divisble, and the remainder otherwise.

    >>> mod = mod_maker()
    >>> mod(7, 2) # 7 % 2
    1
    >>> mod(4, 8) # 4 % 8
    4
    >>> mod(8,4) # 8 % 4
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'mod_maker', ['If', 'IfExp']) # no if / if-else statements
    True
    """
    return lambda x,y: x % y or True
```

### If Statements and Call Expressions
```py
def if_(t, c, n):
     if t:
        return c
    else:
        return n
```

### Generalizing Patterns with Arguements

`Note: function_name can be as an argument in a function.`
**Generalizing Over Computational Processes**
The common structure among functions may be a computational process, rather than a number.

$$\sum^{5}_{k=1} k = 1+2+3+4+5 = 15$$
$$\sum^{5}_{k=1} k^3 = 1^3+2^3+3^3+4^3+5^3 = 225$$

```py
""" Generalization """
def sum_naturals(n):
    """
    Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = totl + k, k + 1
    return total

def sum_cubes(n):
     """
     Sum the first N cubes of naturnal numbers.

     >>> sum_cubes(5)
     225
     """
     total, k = 0, 1
     while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total
```
To generalize the same part in *while* loop, define the next functions:
```py
def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    # Notice: "term" is a formal parameter that will be bound to a function, not a calling.
    """
    Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k  = total + term(k), k + 1
    return total
```

### Function as Return Value

Functions defined within other function bodies are `bound to names in a local frame.`

```py
def make_adder(n):
    """
    Return a function that takes one argument k and returns k + n

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k): # A local def statement
        return k + n
    return adder # return a function
```

### The Purpose of Higher-Order Functions

**Functions are first-class:** Functions can be manipulated as values in our programming language.

**Higher-Order function:** A function that takes a function as an argument value or returns a functiopn as a return value.

**Why we need it?**
- Express general methods of computation
- Remove repetition from programs
- Seperate concerns among functions

### Environment for Higher-Order Function 

- Name can be bound to functional arguments
- Example \
*Step 1:*
```py
    def apply_twice(f, x):        # Global frame
        return f(f(x))            # apply_twice --> func apply_twice(f, x) [parent=Global]
                                # square(x) --> func square(x) [parent=Global]
    def square(x):
        return x * x              # Applying a user-defined function:
                                # 1. Create a new frame
                                # 2. Bind formal parameters (f & x) to atguments
                                # 3. Execute the body: return f(f(x))

==> result = apply_twice(square, 2)
```
Step 2:
```py
    def apply_twice(f, x):        # Global frame
==>     return f(f(x))            # apply_twice --> func apply_twice(f, x) [parent=Global]
                                  # square(x) --> func square(x) [parent=Global]
    def square(x):                #                                 ^
        return x * x              # f1: apply_twice [parent=Global] |
                                  #                         f ------
                                  #                         x 2
    result = apply_twice(square, 2)
```

### Environment for Nested Definitions
```py
def make_adder(n):
    def adder(k):
        return k+n
    return adder

'''
Global frame 
        make_adder ------------> func make_adder(n) [parent=Global]
        add_three -------------> func adder(k) [parent=f1]
                            ^  ^
f1: make_adder [parent=G]   |  |
        n      3            |  |
        adder  -------------   |
        return ----------------

f2: adder [parent=f1]
        x      4
        return 7
'''         
```
- Every user-defined function has a parent frame (often global)
- The parent of a function is the frame in which it was defined
- Every local frame has a parent frame (often global)
- The parent of a frame is the parent of the function called

**How to Draw an Environment Diagram** \
> *When a function is defined:*
> 1. Create a function value:
> 2. Its parent is the current frame.
> 3. Bind \<name> to the function value in the current frame.

> *When a function is called:*
> 1. Add a local frame, titled with the \<name> of the function being called.
> 2. Copy the parent of the function to the local frame: [parent=\<label>].
> 3. Bind the \<formal parameters> to the arguments in the local frame.
> 4. Execute the body of the function in the environment that starts with the local frame. 


### Local Names
 - Local names are not visible to other (non-nested) functions
 - An environment is a suquence of frames.
 - The environment created by calling a top-level function (no def within def) consists of one local frame, followed by the global frame.

### Function Composition

### Lambda Expressions

```sh
>>> x = 10
>>> square = x * x # An expression: this one  evaluates to a number
>>> square = lambda x: x * x # Also an expression: evaluates to a function
             ------ - ------
              |     |    |
              v     |    v
       A function   |    that returns the value of "x * x"
                    v
            with formal parameter x    
>>> square(4)
16    
```
**Note:** 
- No "return" keyword!
- Must be a single expression in the body of lambda function that you create
- Lambda expressions are not common in Python, but important in general

### Currying

> In mathematics and computer science, currying is the technique of translating the evaluation of a function that takes multiple arguments into evaluating a sequence of functions, each with a single argument.  —— wikipedia

```py
def make_adder(n):
    return lanmbda k: n + k

"""
>>> make_adder(2)(3)
5
>>> add(2, 3)
5
"""
```

```py
def curry2(f):
    # 2 means that the function I pass in takes two arguments.
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

"""
>>> from operator import add
>>> add(2,3)
5
>>> m = curry2(add)
>>> add_three = m(3)
>>> add_three(2)
5
>>> add_three(2010)
2013
>>> curry2 = lambda f: lambda x: lambda y: f(x, y)
>>> m = curry2(add)
>>> m(2)(3)
5
"""
```

