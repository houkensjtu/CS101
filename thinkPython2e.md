## :bird: Think Python 2e notes

> How to think like a computer scientist <= 言い過ぎ

### Chapter 1 : The way of the program

- What is a program? 
- Running Python. (Used Python 3.4 vanilla version)
- First program (just print("hello world"))
- Arithmatic operations
- Value and types (can use type() to check the type of a value)
```Python
>>> type(42)
>>> <class 'int'>
>>> type('42')
>>> <class 'str'>
```
- Compare natural and formal language
- Debugging (Only introduced what is debugging; no actual debugging skill)

### Chapter 2 : Variables, expressions and statements

- Assignment statemet （create a varialbe and give it a value)
```Python
n  = 17
pi = 3.1415926
```
- Variable name (don't use Python's keywords)
- Expressions and statments
  - Expression : combination of values and variables and operators. The interpreter **evaluates the expression.**
  - Statement : A unit of code that **has an effect.** The interpreter **execute the statement.**
```Python 
# Expression : will return a value
>>> 43 + 12
>>> 55
# Statement : effect is creating a variable
>>> a = 55
>>> 
```
- Script mode : In script mode, the result of an expression won't be printed out.
- String operations : Strings can be connected simply using "+"; but no "-", "*" or "/" is allowed.
- 3 types of error :
  - Syntax error : Illegal expression.
  - Runtime error : Also called exceptions. Only happen when the programm running.
  - Semantic error : Logic error. The program is not doing what's supposed to be done.
  
 ### Chapter 3 : Functions
 
 - Making call to functions
 ```Python
>>> type(42)
>>> <class 'int'>

>>> str(42)
>>> '42'
 ```
 
 - Math module
 ```Python
# This statement creates a module object named math. 
# If you display the module object, you get some information about it:
>>> import math
>>> math
>>> <module 'math' (built-in)>
# To see what's included in math module:
>>> dir(math)
>>> help(math)

# The dot notation:
>>> math.sqrt(2)
>>> 1.414...

# Or use the following statment to avoid dot, but it's not recommended.
>>> from math import *
>>> sqrt(2)
    
# Recommend
>>> import math as m
>>> m.sqrt(2)
    
# Or 
>>> from math import sqrt
>>> sqrt(2)
```
  
