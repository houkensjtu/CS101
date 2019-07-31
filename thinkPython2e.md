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
 - Adding new function. (**Notice single quote mark and double quote mark are same in Python, no difference.**)
 ```Python
 def print_lyrics():
    print("I want your love, and I want your revenge")
    print("You and me could write a bad romance")
    
 def repeat_lyrics():
    print_lyrics()
    print_lyrics()
 ```
 
 - Variables and parameters are local
 ```Python
 # part1, part2, result are all local and cannot be access outside the function
 def cat(part1,part2):
    result = part1 + part2
    print(result)
 ```
 
 - Why functions? (抽象，封装的思想)
   - Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read and debug.
   - Functions can make a program smaller by eliminating repetitive code.  Later, if you make a change, you only have to make it in one place.
   - Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.
   - Well-designed functions are often useful for many programs.  Once you write and debug one, you can reuse it.
   
 ### Chapter 4 : Case study: interface design

 - The tutle module
"turtle" is a module for learning software design.

```Python
# Import the turtle module
import turtle

# Turtle() method creates a turtle object
bob = turtle.Turtle()

# => <turtle.Turtle object at 0xb7bfbf> shows that bob is now a Turtle type object
print(bob)

# Turtle's movement methods:
bob.fd(100)
bob.lt(90)
bob.fd(100)

# Execute the movement
turtle.mainloop()
```

 - Simple loop
 
 ```Python
 for i in range(10):
    bob.fd(100)
    bob.lt(100)
 ```
 
 - Small exercises
 ```Python
 # 1. Write a function, with a turtle t as argument. Pass bob to it.
 def square(t):
    for i in range(4):
       t.lt(90)
       t.fd(100)
 square(bob)
 
 # 2. Add length as a parameter. 
 def square(t, len):
     for i in range(4):
       t.lt(90)
       t.fd(len)
 square(bob,100)
 ```
 
 - Encapsulation
   - square(t) has a turtle as parameter. Calling square(bob) is the same as bob.lt()... Then why not call bob directly?
     It's because in such a way, t can be any turtle, not just bob! **通过封装，函数隐藏了函数的实现，并且拥有一个通用的接口
     可以让你接入任何同类型的数据进行运算.**
 - Generalization
   - Adding a parameter to a function is called generalization because it makes the function more general.
   - When a function has more than a few numeric arguments, it is easy to forget what they are, or what order they should be in. In that case it is often a good idea to include the names of the parameters in the argument list:
```Python
# When calling the function, including the name of the parameter; has to match function definition.
square(t=bob, len=10)
```

  - Interface design
     - The interface of a function is a summary of how it is used: what are the parameters? What
  does the function do? And what is the return value? An interface is “clean” if it allows the
  caller to do what they want without dealing with unnecessary details. 
  **函数的接口**粗略地说就是函数的参数和返回值。所谓**简洁精炼的接口设计**，就是将且仅将用户需要的参数交给用户处理，
  其他不需要由用户决定的参数都应该包装到函数内部。
  
 - Development plan
    1.  Start by writing a small program **with no function definitions.**
    2.  Once you get the program working, identify a coherent piece of it, **encapsulate the
    piece in a function** and give it a name.
    3.  **Generalize the function** by adding appropriate parameters.
    4.  Repeat steps 1–3 until you have a set of working functions. Copy and paste working
    code to avoid retyping (and re-debugging).
    5.  Look for opportunities to **improve the program by refactoring.**（所谓refactor就是抽出代码中通用的部分，将其函数化，并配以适当的端口
    且改动现有程序使得这个函数可以被接入）  For example, if you
    have similar code in several places, consider factoring it into an appropriately general
    function.
 
  - docstring   
    在函数定义中用三引号描述函数接口是一种良好的编程习惯。三引号字符串允许跨行。
 ```Python
 def square(t,len):
    """ Draw a square with edge length = len 
    by a turtle object t. """
    ...
 ```
 
 ### Chapter 5 : Conditionals and recursion

- floor division and modulus
  - Modulus can be used to determine if a number is divisible by another, just check a%b==0.
```Python
# In Python3
>>> minutes = 105
>>> minutes / 60
1.75

# Floor division
>>> minutes = 105
>>> hours = minutes//60
>>> hours
1

# Modulus
>>> remainder = minutes % 60
>>> remainder
45
```

- Boolean expressions
  - x == y
  - x != y
  - x >  y
  - x >= y
  
```Python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

-  Logical operators
   - There  are  three logical  operators : and, or, and not. **注意Python里是没有&&, | 这样的运算符的。**"&"表示位的and操作，"|"表示位的或操作。
```Python
x = True
y = False

# Output: x and y is False
print('x and y is',x and y)
```
- Conditional execution   
**Python的条件是不需要用括号的** 当然你用括号括起来也不是错误。C和Java都是严格要求用括号的，Javascript也要求，这么看来Python的外貌真的有点特立独行。。
```Python
if x > 0:
   print("X is bigger than 0.")

# 条件判断语句的后面至少要有一个语句，所以加一个pass作为占位是一种有用的技巧
if x > 0:
   pass # TO DO: add something here!
else:
   print("X is not bigger than 0!")
```

- Recursion   
A function that calls itself is recursive; the process of executing it is called recursion. 这里只是引入了递归的概念，还没有具体讲解递归的各种活用。作为一个基本认识，没有base case的递归是会无限引用下去的，在Python里呼叫超过一定的深度（1000次）以后会引发RunTimeError。
```Python
def countdown(n):
   if n<0:
      print("BANG!")
   else:
      print(n)
      countdown(n-1)
```

- User input   
Python provides a built-in function called **input** that stops the program and waits for the user to type something.  When the user presses
Return or Enter, the program resumes and input **returns what the user typed as a string.** In Python 2, the same function is called raw_input. 注意input()返回的总是一个string，如果需要数字型的话，可以用int(string)的方法将字符串转换成整数。
```Python
# input括号中的字符串会作为提示，出现在input之前
>>> name = input("What is your name? ")
What is your name?
Arthur
>>> name
'Arthur'
```

### Chapter 6 : Fruitful functions

- Functions with return values.

```Python
def area(radius):
    a = math.pi * radius**2
    return a

# A more concise version
def area(radius):
    return math.pi * radius**2

# return can be in a conditional branch
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
```

- Incremental development
    -  Start with a working program and make small incremental changes. Display and check value occasionally.

- Composition
```Python
def circle_area(xc,yc,xp,yp):
    radius = distance(xc,yc,xp,yp)
    result = area(radius)
    return result
```
- Boolean functions
    - Functions can return booleans, which is often convenient for hiding complicated tests inside functions.
    - It is common to give boolean functions names that sound like yes/no questions.
```Python
def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False
```
- More recursion
```Python
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
```
- Leap of faith
    - When  you  come  to  a function call, instead of following the flow of execution, you assume that the function works correctly and returns the right result.
    
```Python
def fab(n):
    if n == 0:
        return 0
    else if n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
```

- **Guardian branch**; this is a simplified/brute force way of checking type, will introduce **rasing exception in chapter11.**
    - If n is not an integer, the function above will never return because it never hit 0.
```Python
def fab(n):
# This if branch is sometimes called a guardian.
    if not isinstance(n, int):
        print("n must be an integer!")
        return None
    else if n == 0:
        return 0
    else if n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
```
- Debugging=> **Add print statements at the begining and the end of a function** to confirm input and output.   
    -There is something wrong with the arguments the function is getting; a precondition is violated.   
    -There is something wrong with the function; a postcondition is violated.   
    -There is something wrong with the return value or the way it is being used.   


### Chapter 7 : Iteration

- Updating variables: Updating a variable by adding 1 is called an increment; subtracting 1 is called a decrement.
```Python
# 变量在使用前是需要初始化的
>>> x = 0
>>> x = x + 1
>>> x
```
- The while statement: Example : [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
```Python
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = number*3 + 1
        print(number)

collatz(int(input('Enter a positive integer:')))
```
- break : 彻底退出循环
```Python
# 一个迷你terminal!!
while True:
    line = input('> ')
    if line == "done":
        break
    else:
        print(line)
```

- Square root: newton method (**an example of an algorithm**, using while loop)
```Python
# 不用break的写法
def newton_sqrt(f):
    eps = 1.0e-10
    guess = f/2
    while abs(guess-f/guess)>eps:
        guess = (guess + f/guess)/2
    return guess

# 使用break的写法
def newton_sqrt(f):
    eps = 1.0e-10
    guess = f/2
    while True:
        if abs(guess-f/guess)>eps:
            break
        else:
            guess = (guess + f/guess)/2
    return guess
```

### Chapter 8 : Strings

- string is a sequence of characters.
```Python
>>> fruit  = 'banana'
>>> letter = fruit[1]
# -> 'a'
```
- strings can be sliced, like a list; but **string is immutable.**
```Python
fruit[:2]
fruit[0] = 'c'
#-> Error
```

- search a letter in a string; this is a **reverse** of the [] operator! There is also a built-in find() method in Python
```Python
def find(word,letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
```

- string's built-in methods.
```Python
# Return length
>>> fruit.len()

# Case change
>>> fruit.upper()

# Find letter
>>> fruit.find('a')
#-> Return the index of the letter if found; return -1 if not.

# In operator
>>> 'a' in fruit
#-> True
```

- Debugging: when using slices of string, it might be confusing because the handling of index sometimes include/exclude a letter.
You can **insert print statement to confirm the current index before where Errors** (For example, "IndexError: string index out of range" come out)
