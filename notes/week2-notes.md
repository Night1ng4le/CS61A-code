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

### The Project 1: Hog

**Rule:** 
2 players alternate roll dice, to choose the one that the 1st's score >= 100.
For Each Player:
- choose the number of dice, <= 10
- if any dice turns 1, the score = 1; else score = sum of each dice number
