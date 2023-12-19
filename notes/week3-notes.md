# Week3 Notes

### Sound(Example)

**WAV Files:** The Waveform Audio File Format encodes a sampled sound wave \
-> recording the height or amplitude of the wave at particular moments

### Environment Diagram with Lambda 
A lambda function's parent is the current frame in which the lambda expression is evaluated. 
```py
# which a is used in each of these cases?
a = 1
def f(g): 
    a = 2 # each "a" in the body of function "f" is assigned to 2
    return lambda y: a * g(y)

f(lambda y: a + y)(a)  # all "a" are global "a"

"""
      Frames          Objects
Global frame  
        a  1
        f  ·---------> func f(g) [parent=Global]

f1: f [parent=Global]
        g  ·---------> func λ(y) [parent=Global] <line 5>
        a  2
   Return
    Value  ·---------> func λ(y) [parent=f1]  <line 4>

f2: λ <line 4> [parent=f1]
        y  1
   Return
    Value  4

f2: λ <line 5> [parent=Global]
        y  1
   Return
    Value  2 
"""
```

### Return 

**Return statement:** A return statement completes the evaluation of a call expression and provides its value.

f(x) for user-defined f: switch to a new environment; execute f's body `return` statement within f: switch back to the previous environment; f(x) now has a value.

Only one return statement is ever executed while executing the body of a function

### Functional Abstractions

```py
def square(x):
    return mul(x, x)

def square(x):
    return pow(x, 2)

def square(x):
    return mul(x, x - 1) + x
```

```py
def sum_square(x, y):
    return square(x) + square(y)
```
If the name "square" were bound to a built-in function, sum squares would still work identically. It doesn't matter whether square is user-defined or built-in for sum_square to use.

### Choosing Names

Names typically don't matter for correctness `but` they matter a lot for composition. (Reasonable Name)
- Names should convey the meaning or purpose of the values to which they are bound.
- The type of value bound to the name is best documented in a function's docstring.
- Function names typically convey their effect (print), their behavior (triple), or the value returned (abs).

------------------------------------------------
### Lab 02 notes

Example:
```py
>>> def cake():  # closure function
...    print('beets') # nested function
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
>>> chocolate
<function cake.<locals>.pie at 0x00000139BA1F09A0>
>>> chocolate1 = cake()
>>> chocolate1
<function cake.<locals>.pie at 0x00000139BA1F0A40>  
# the addresses are different because "A new instance of the nested function is created each time the closure function is called."
```
