# Week1 Notes

### Type of Expressions

*Primitive Expressions*
- Number or Numeral
- Name
- String

*Call Expressions*
- Operator(Operand,Operand)

**Discussion:** 
What' the value of the final expression in this sequence?
```python
>>> f = min
>>> f = max
>>> g, h = min, max
>>> max = g
>>> max(f(2, g(h(1, 5), 3)), 4)
```
*Answer is 3.* 


### Environment Diagrams

[a tutor website](https://www.composingprograms.com/)

### Assignment Statements

*Execution rule for assignment statements:*
1. Evaluate all expressions to the right of = from left to right.
2. Bind all names to the left of = to the resulting values in the current frame.

### Defining Functions

`Assignment` is a simple mean of abstraction: bind names to values. \
`Function` definition is a more powerful means of abstraction: binds names to *expressions*.

```python
>>> def <name>(<formal parameters>):
        return  <return expression>
```

**Execution procedure for def statements:**
1. Create a fuction with signature \<name>(\<formal parameters>);
2. Set the body of that function to be everything indented after the first line;
3. Bind \<name> to that function in the current frame.

### Calling User-Defined Functions

*Procedure for calling/applying user-defined functions (version 1)*
1. Add a local frame, forming a *new* environment.
2. Bind the function's formal parameters to its arguments in that frame.
3. Execute the body of the function in that new environment.

### Looking up Names in Environments

Every expression is evaluated in the context of an environment.

So far, the current environment is either :
- The global frame alone, *or*
- A local frame, followed by the global frame.

> Most important 2 things: 
> 1. An environment is a *sequence* of frames.
> 2. A name evaluates to the value bound to that name in the earliest frame of the current environment in which that names is found.

**e.g.: to look up some name in the body of *square* function:**
- Look for that name in the local frame.
- If not found, look for it in the gloabal frame.\
(Built-in names like "max" are in the global frame too, but to keep simple,  we don't draw them in environment diagrames.)

### None Indicates that Nothing is Returned

The soecial value `None` represents nothing in Python.\
A function that does not explicitly return a value will return `None`. \
*Careful:* `None` is *not displayed* by the interpreter as the value of an expression.

### Pure Functions & Non-Pure Functions

*Pure Functions:* just return values \
*Non-Pure Functions:* have side effects (take some *input* & have some *output*) \
A side effect isn't a value; it's anything that happens as a consequence of calling a function.

### Nested Expressions with Print

```python
>>> print(print(1), print(2))
1
2
None None
```
*A function tree:*
```python
       print(print(1), print(2))  -> func print(...)
            --------   ---------
               /          |
        print(1)        print(2)
        ----- --        ----  --
          /   |          /     \
func print()  1   func print()  2


# print(1) will display 1, and value of the statement expression is None.
# print(2) same as print(1)
```