# Python crash course

整本书分为两大部分，Part I介绍了Python从基本语法，到函数以及类的基本概念，Part II包含三个Projects，第一个是射击游戏，第二个是数据可视化，第三个是 Web application。虽然内容不是很高深，但是循序渐进使得内容比较多，希望可以持之以恒，一步一步看完敲完。

### Part I : BASICS

### 1. Getting started

* 安装Python，使用Python3。
* 写一个Hello world程序，并用解释器或者脚本模式运行。
* Python3和Python2的3个明显区别，print语句，除法运算和用户输入。

  \`\`\`Python

  **Python2中导入future这个特殊模块，就可以像3一样使用print和除法运算**

  from **future** import print\_function, division

## Python3中的input语句会将用户输入变成一个字符串

s\_number = input\("Input a number and hit \[Enter\]:"\)

```text
### 2. Variables and simple data types
- 变量命名规则，不要使用Python关键字
- 如果打错字导致变量名没有声明过，Python会给出NameError
```Python
message = "Hello"
print(messg)
# => NameError : name 'messg' is not defined.
```

* String型
  * 在Python中用双引号和单引号都可以表示string，没有区别
  * .upper\(\), .lower\(\)和.title\(\)用来转换string的大小写
  * 用+运算符来组合string
  * 在String中用"\n" "\t"表示换行和tab，用"\'"在字符串中表示引号
  * 用.strip\(\)来除去字符串中的空格
* int型 : Python3中的除法会自动将1/2的结果转换成0.5
* float型 : 指数运算在python中是两个星号\*\*
* 在解释器中输入import this可以查看Then Zen of Python

### 3. Introducing lists

* List在Python中方括号定义，List中的元素不需要同类型
* 取用List元素时也用方括号表示index，注意List的元素都是从0而不是1开始;-1代表的是List中最后一个元素。

  ```python
  motorcycles = ["honda","yamaha","suzuki"]
  ```

* List是可以动态加减的，也就是说，可以在程序运行过程中增减元素。例如，在一个游戏中你用List存储alien的个体。画面中显示的

  alien需要不断增加或者删除，这个时候就需要动态修改List的元素。

  \`\`\`Python

  **在List末尾添加元素**

  motorcycle.append\("ducati"\)

## 插入元素

motorcycle.insert\(0,"ducati"\)

## 删除一个元素

del motorcycle\[1\]

## 推出一个元素

popped = motorcycle.pop\(\)

## pop\(\)之后motorcycle就少了一个元素，而这个元素被保存到了popped变量中

## pop也可以接收参数，推出list中任意位置的元素

## 这里是pop出第一个元素

popped = motorcycle.pop\(0\)

## 移除一个特定值的元素; 注意remove只移除list中首次出现的值，如果要移除全部重复出现的元素，需要用循环来实现

motorcycle.remove\("ducati"\)

```text
- List元素的管理与整理。
```Python
# sort()将list中元素进行排序，执行后car将不再保存原来的序列
car = ["bmw","audi","toyota","subaru"]
car.sort()
print(car)

# 逆序排列
car.sort(reverse=True)

# 暂时排序但是不修改原有list
print( sorted(car) )
```

* List的长度,len\(\)

  ```python
  len(car)
  ```

### 4. Working with lists

* 循环遍历List的每个元素是对List的一种普遍操作。

  ```python
  # 一个简单的遍历例子
  # 注意for循环格式，末尾要有冒号; 另外，magician只是一个暂时的变量名，可以随便取
  magicians = ["alice","david","carolina"]
  for magician in magicians:
    print(magician)
  ```

* Python的for循环语句，需要一个冒号结尾，循环体则用indent来标识。
* 生成数字序列用的是range这个函数（numpy里用的则是numpy.arange这个函数，生成的就是矩阵而不是List了）

  ```python
  for i in range(1,5):
    print(i)
  # 注意这里只会打印出1,2,3,4
  ```

* **注意range\(\)返回的并不是list，而是一个range**，可以用list\(range\(\)\)来将其转换成List

  \`\`\`Python

  numbers = list\(range\(1,6\)\)

  print\(numbers\)

  **\[1,2,3,4,5\]**

## range的第三个参数是调整间隔用

evenNumbers = list\(range\(1,10,2\)\) print\(evenNumbers\)

```text
- 数字list可以使用min，max等简单函数来处理
```Python
>>> digits = [0,1,2,3,4,5]
>>> min(digits)
0
>>> sum(digits)
15
```

* **高级概念：List comprehension**

  \`\`\`Python

  **普通的生成方法**

  square = \[\]

  for i in range\(1,5\):

    square.append\(i\*\*2\)

## List comprehension大法，一行解决从声明，循环到添加元素

square = \[i\*\*2 for i in range\(1,5\)\]

```text
- List的切片(slicing);同样用的是方括号，括号中用冒号隔开起始与终止元素。
```Python
# 注意这里的0:3切出的是第一，第二和第三个元素（0,1,2）
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# 切片也可以组合for循环使用;省略第一个元素的写法表示从0开始
for player in players[:3]:
    print(player)
```

* List的复制

  \`\`\`Python

  my\_foods = \["pizza", "falafel", "cake"\]

  friend\_foods = my\_foods\[:\]

  **这样就复制了一个list，从而使两个list互相独立**

friend\_foods = my\_foods

## 这是复制了地址，这两个名字将指向同一个list

```text
- 元组Tuple;定义时用括号而不是方括号，但是取元素时是一样的
```Python
dimensions = (200,30)
dimensions[0]
```

* PEP8代码风格指南
  * indent推荐使用4个空格，不使用tab
  * 一行推荐不超过80个字符

### 5. If statement

* Python的if语句不需要括号条件，语句后面需要加冒号，与for保持一致

  \`\`\`Python

  cars = \["bmw","subaru","toyota","audi"\]

for car in cars:

## 这里注意的是if文的条件，不需要用括号

```text
if car == "bmw":
    print(car.upper())
else:
    print(car.title())
```

> > > BMW Subaru Toyota Audi \`\`\`

* 复合多个逻辑条件,Python中用的是and和or关键字

  ```python
  >>> age_0 = 18
  >>> age_1 = 21
  >>> age_0 >= 22 and age_1 >= 22
  False
  ```

* 检查一个元素是否在list中: in关键字;反之，检查是否不在list中，用not in关键字

  ```python
  >>> requested_toppings = ["mushroom","onions","pineapple"]
  >>> "mushroom" in requested_toppings
  True
  >>> "pepperoni" in requested_toppings
  False
  >>> "pepperoni" not in requested_toppings
  True
  ```

* if-elif-else例子

  ```python
  age = 12
  if age < 4:
    price = 0
  elif age < 18:
    price = 5
  else:
    price = 10
  print("Your price is $" + str(price) + ".")
  ```

### 6. Dictionaries

* Dictionary用花括号表示，括号中是一个一个的key-value对子。下面的例子演示了用一个dic来模型一个游戏中alien的例子。

```python
# Key-value对子用冒号隔开
# Key除了字符串以外其实也可以用数字，value则可以是任意的object
alien_0 = {"color":"green", "points":5}
print(alien_0["color"])
print(alien_0["points"])

# 向alien_0中添加属性
alien_0["x_position"] = 0
alien_0["y_position"] = 25

# 删除元素
del alien_0["points]
```

* Dictionary也可以用来保存多个并列的元素

```python
favorite_languages = {
    "jen"   : "python",
    "sarah" : "c",
    "edward": "ruby",
    "phil"  : "python,
}
```

* Dictionary元素的循环，循环方式有3种：循环key值，循环value值，或者循环所有key-value对。

  \`\`\`Python

  user\_0 = {

    "username" : "efermi",

    "first" : "enrico",

    "last" : "fermi",

  }

  for key,value in user\_0.items\(\):

    print\("key" + key\)

    print\("value" + value\)

for name in user\_0.keys\(\): print\(name.title\(\)\)

```text
- Nesting。在Dictionary中可以嵌套list，也可以在List中嵌套Dictionary
```Python
# Dictionary组成的List
alien_0 = {"color":"green", "points":5}
alien_1 = {"color":"blue", "points":15}
alien_2 = {"color":"yellow", "points":10}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

# Dictionary中包含list

pizza = { "crust":"thick", "toppings":["mushroom","cheese","tomato"]}

for topping in pizza["toppings"]:
    print(topping)
```

### 7. User input and while loops

* input\(\)收取一个参数作为提示用户的文字，返回用户输入的字符串

  ```python
  message = input("Input something, and I will repeat it to you:")
  print(message)
  ```

* 将input\(\)的返回值变成整数型可以用int\(\)这个方法
* Python2中也有input\(\)这个方法，但是在Python2中input\(\)会企图将用户输入的字符进行解释运行，而在Python2中实现输入字符串功能用的是raw\_input\(\)
* 结合input和while循环可以实现不断从用户取得输入

  \`\`\`Python message = "" while message != "quit": message = input\("Please input your words. Enter quit to quit:"\) print\(message\)

```text
- 用flag的概念来控制程序的while循环。大多数程序都会有一个主循环，而在运行过程中，有很多事件可以导致程序终止。如果在while的条件中测试这些
条件会让程序显得过于冗长繁琐。比较好的做法是让while仅仅观察这个flag，而由其他部分完成flag的变化
```Python
active = True
message = ""
while active:
    message = input("Plesae intput some words. Enter quit to quit.")
    if message == "quit":
        active = False
    else:
        print(message)
```

* break和continue:break用来跳出循环（不再返回），**而continue用来跳过循环体的一部分内容（之后重新回到循环头部）**

  \`\`\`Python

while True: city = input\("Enter your favorite city. Enter quit to quit."\) if city == "quit": break else: print\("Your favorite city is" + city + "!"\)

## 输出一串奇数

for i in range\(1,10\): if i%2==0: continue else: print\(i\)

```text
- 用while循环将一个list中的内容转移到另一个中的例子
```Python
user_list = ["Andy", "Brian", "David", "Josh"]
verified_user = []

# 这里是一个技巧，用user_list本身作为一个条件来判断，当所有元素变空时判断为否
while user_list:
    current_user = user_list.pop()
    print("Verifying user:" + current_user)
    verified_user.append(current_user)
for user in verified_user:
    print(user)
```

* while配合in使用，**表示对list中所有匹配的元素进行处理**；for配合in则是对所有元素，**不管匹配与否都进行处理**.

  \`\`\`Python

  pets = \["cat","rabbit","dog","cat","cat","spider"\]

  **注意这里是用字面量“cat”，而不是像for循环中一样用一个临时变量。for是不能用这种写法的**

  while "cat" in pets:

    pets.remove\("cat"\)

print\(pets\)

```text
- 用while循环来填充一个dict
```Python
#这个片段在Jupyter中会有bug，重复显示同一个元素？？！
response = {}
responses= []
active = True

while active:
    user_name = input("Enter your name:")
    user_city = input("And what's your favourite city?")
    response["name"] = user_name
    response["city"] = user_city
    responses.append(response)

    ans = input("Do you want to pass to another user? (Yes/No) :")
    if ans == "No":
        active = False
# 此段代码正常
responses= {}
active = True

while active:
    name = input("Enter your name:")
    responses[name] = input("And what's your favourite city?")
    print(responses)
    ans = input("Do you want to pass to another user? (Yes/No) :")
    if ans == "No":
        active = False
print(responses)
```

### 8. Functions \(1\)

* function基本的结构类似循环体，使用def关键词开头，声明结尾需要冒号，函数体用indent区分。三引号表示docstring，用来描述函数作用。

  \`\`\`Python

  def greet\_user\(\):

    """ Display greeting."""

    print\("Hello!"\)

## Passing information to function

def greet\_user\(name\): """ Display greeting.""" print\("Hello!" + name\)

```text
- **函数参数的指定传递**。这是个好习惯，使得代码可读性大大提高，也很有X格。。
```Python
def describe_pet(type,name):
    print("I have a " + type)
    print("His name is " + name)

# 在呼叫函数时指定参数的名字并传递，这样就算顺序颠倒结果也不会出错
describe_pet(type = "hamster", name = "Harry")
describe_pet(name = "Harry", type = "hamster")
```

* 参数默认值的设定。在函数定义时，可以给预计不会有太多变化的参数顺便定义默认值。

  \`\`\`Python

  **定义默认值时注意，没有默认值的参数要放在前面，这样后面呼叫时不会出差错**

  def describe\_pet\(name, type="dog"\):

    print\("I have a " + type\)

    print\("His name is " + name\)

## 我有一只狗叫做Jimmy

describe\_pet\("Jimmy"\)

```text
- 返回值
```Python
def get_formed_name(first, last):
""" Return a full name, neatly formatted."""
   formal = first + " " + last
   return formal.title()

musician = get_formed_name("jimi","hendrix")
print(musician)
```

* 定义一个可选参数的函数：有时候我们希望某些参数是可选的，如果用户提供则使用，否则不使用，这可以用参数的默认值写法来实现

```python
def get_formed_name(first, last, middle=''):
""" Return a full name, neatly formatted."""
   if middle:
      formal = first + " " + middle + " " + last
   else:
      formal = first + " " + last
   return formal.title()

musician = get_formed_name("jimi","hendrix","lee")
print(musician)
```

* 返回一个dict型，函数并不是只能返回单一数值，而是可以返回任何数据结构

  ```python
  def build_person(first, last, age=''):
  """ Return a full name, neatly formatted."""
   person = {'first': first, 'last':last}
   if age:
      person['age'] = age
   return person
  ```

* 用while循环反复呼叫函数

  ```python
  while True:
    first_name = input("Please input your first name")
    last_name = input("Please input your last name")
    print("Hello!" + get_formal_name(first_name, last_name))
  ```

* 向函数传递一个list

  \`\`\`Python def greet\_users\(name\_list\): for name in name\_list: print\("Hello!" + name\)

user = \["Jimmy", "Sarah", "Steve"\] greet\_users\(user\)

```text
- 向函数传递一个list，并做一些相应的处理。这里的例子是，假设我们有一个等待处理的模型列表，我们希望每次弹出一个模型，打印他的名字，然后保存到完成列表中
- 下面这个例子演示了几个概念：首先，使用函数使得代码复用变得容易，有了函数以后处理不同列表只需重复呼叫同一个函数即可;另外，函数的功能应该相对单一，
一个函数只完成一个特定目标

```Python
def print_model(model_list, completed_models):
    while model_list:
        current = model_list.pop()
        print("The current model is " + current)
        completed_models.append(current)
 def display(completed_models):
     for model in completed_models:
         print(model)

model_list = ["Pikachu", "Soma", "Hikaru"]
completed_models = []
print_model(model_list, completed_models)
display(completed_models)
```

### 8. Functions \(2\)

* 向函数传递任意个数的参数;这里星号意味着参数是一个不定长度的tuple。

  \`\`\`Python

  def makePizza\(\*toppings\):

    for topping in toppings:

  ```text
    print("Added a " + topping)
  ```

```text
- 比如说我们要写一个乘法函数，如何定义一个可以接受不定个数的数字并将他们全部相乘的函数呢？

```Python
# 不用星号的话，只能这样写
def multi(x,y)
    return x*y

# 这样的话就可以传递不定个数的参数了
def multi(*args):
    n = 1
    for i in args:
        n *= i
    return n
```

* 两个星号的作用是接受一个dict，其用法和一个星号类似

```python
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print("Key:" + key)
        print("Value:" + value)

# 呼叫这个函数的时候，key的传递方法
user_profile(key1="xxx", key2="yyy")

# 注意这里的key是不需要加引号的，用起来的感觉就像指定名字的参数，和dict['key']的取法是两回事
```

* 把制作好的函数存放到module里：在Python里，**文件名就是module名，可以import**

  \`\`\`Python

  **pizza.py**

  def make\_pizza\(\*toppings\):

    for topping in toppings:

  ```text
    print("Adding " + topping)
  ```

    print\("Finished"\)

## main.py

import pizza

pizza.make\_pizza\("mushroom","cheese","tomato"\)

```text
- 从module导入某个特定函数
```Python
from pizza import make_pizza
make_pizza(...)

# 缩写格式
from pizza import make_pizza as mp
mp(...)

# 或者缩写module名字
import pizza as p
p.make_pizza(...)
```

* from module import \* 的写法是不推荐的，因为会引入你并不知道的函数，可能和现有的函数冲突
* 函数编写风格的一些规定

  \`\`\`Python

  **写参数的默认值不要用空格**

  def func\(value=1, arg="hello"\): print\(arg\)

## 参数过多时，用换行来整理格式，行首用2个tab或者8空格

def longPar\( parameter1="a", parameter2="b", parameter3="c", parameter4="d"\): print\(...\)

```text
### 9. Class

- 创建class的方法;括号中是表示继承的父类。在Python2版本中，所有类都需要继承object类，但是目前在Python3中已经不需要

```Python
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll(self):
        print(self.name.title() + " is now rolling.")

my_dog = Dog("Willie",6)
```

* 注意到**init**方法的参数中，除了name和age以外，还包括了self。self是表示对象本身，意味方法可以访问对象本身内部的所有内容.
* 另外，**init**这个方法虽然没有写return语句，但是Python会自动返回一个对象，所以可以把初始化的对象传递给一个名字
* 下面看一个修改class的属性的例子;修改属性共有几种方法
  * 直接通过对象访问属性，并设置其值
  * 通过method来修改属性
  * 通过method来increment

```python
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0.0

    # 这里注意，虽然get_name并不需要参数，但是还是要传入self    
    def get_name(self):
        long_name = str(self.year) + " " + self.make + self.model
        return long_name.title()

    def read_meter(self):
        print("This car has " + str(self.odometer) + "miles on it.")

    # 用来修改属性的method    
    def update_odometer(self,mileage):
        self.odometer = mileage

    # 用来增加属性值的方法，本质和上面一样
    def increment_odometer(self,mile):
        self.odometer += mile

 car = Car("Audi","A4",2019)
 print(car.get_name())
 #=> 2019 Audi A4

 car.read_meter()
 #-> This car has 0.0 miles on it.

 # 直接修改属性
 car.odometer = 23

 # 通过method来修改属性
 car.update_odometer(23)

 # 通过mehod来增加
 car.increment_odometer(10)
```

* 直接修改属性很方便，**但是让用户直接修改属性是有risk的**，比如说，有用户在增加一定的mile之后，又设置其属性归0,而实际mile是只增不减， 这样**逻辑错误**就产生了
* 类属性\(class attribute\)和对象属性的问题

  ```python
  # 如下所示，在Class定义下面写的属性属于类，故所有对象都会拥有这个相同属性
  # 在__init__里的属性就属于对象属性，每个对象可以有不同的属性值
  Class Car():
    class_attribute = 0.0
    def __init__():
        ins_attribute = 1.0
    def update(self):
        self.ins_attribute = 10.0
  ```

* Inheritance 继承;定义中用括号表示父类，另外在**init**里要用super\(\)来呼唤父类;
* 在子类中可以新定义新的属性和方法，也可以override父类中的方法，只要用同样的函数名字即可

  \`\`\`Python

  ElectricCar\(Car\):

    def **init**\(self,make,model,year\):

  ```text
    super().__init__(make,model,year)
    self.battery_size = 70
  ```

Tesla = ElectricCar\("Tesla","Model S",2016\) print\(Tesla.get\_name\(\)\)

```text
- importing class. 为了更好的整理文件，可以把比较大的类单独做成一个文件module。比如上面的Car这个类，可以存放到car.py
```Python
# car.py
class Car():
    """ A simple attempt to model a car. """
    def __init(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

# my_car.py
from car import Car

my_new_car = Car("Audi","A4",2016)
...
```

* 老生常谈import的一些方法比较

  \`\`\`Python

  **普通的import，可以逗号隔开import多个类**

  from car import Car, ElectricalCar

## 引入整个module，在调用时需要前缀module名字

import car

my\_new\_car = car.Car\("BMW","BX",2019\)

## 不推荐wildcard引用，理由有很多，有可能导入你不知道的method与自己代码重叠

## 另外，第三者阅读代码时，光看这个语句不知道作者的意图是要导入什么，影响代码可读性

from car import \*

```text
### 10. Files and exceptions

- 打开文件用open()函数，这个函数**不需要import**。另外，open函数经常与with语句共用，使得程序更简洁。
另外，with语句会在block结束后负责关闭文件。否则，你需要先open()一个文件，然后再close()。在写程序的过程中老是需要记住close()是比较麻烦的，
因此有了with这个用法。

```Python
with open("pi.txt") as file_object:
    # 这样会打印出文件所有内容
    contents = file_object.read()
    print(contents)

    # 这样可以一行一行输出文件内容
    for line in file_object:
        print(line)
```

* 把文件的内容一行一行存入一个list的方法readlines\(\)，也就是说readlines\(\)返回的是一个list。rstrip\(\)这个方法是除去多余的换行。

  \`\`\`Python

  with open\("file.txt"\) as file\_object:

    lines = file\_object.readlines\(\)

for line in lines: print\(line.rstrip\(\)\)

```text
- 作为一个简单的处理文件数据例子，作者给出一个问题，你的生日有没有出现在pi的前100万位中？
```Python
with open("pi.txt") as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday:")

if birthday in pi_string:
    print("Your birthday appeared in pi!")
else:
    print("Your birthday didn't show up in pi!")
```

* 写入文件：用的还是open函数，只是后面要加一个写入的参数设定;备注**Python只能写入string数据，所以你要写入数字的时候，也必须通过str\(\)方法把数字转换成字符才可以**

  \`\`\`Python

  **注意这里open\(\)里的参数w**

  with open\("data.txt",w\) as file\_object: file.object.write\("I love programming!"\)

  **另外，写入的时候如果不表明换行，Python是不会自动换行的**

  file.object.write\("Hello, \n"\) file.object.write\("World! \n"\)

```text
- Exceptions 例外的处理。Python中用try-except块来处理例外的发生。例外处理的好处是，程序即便遇到error也不会退出，而可以继续运行。
等于是你预见并处理了错误，这和不处理错误是不同的。（虽然结果都是有错误）
```Python
try:
    a = 5/0
except ZeroDivisionError:
    print(a)
```

* 信息存储：json是一种为Javascript开发的文件格式，但是由于其用途广泛，在Python中也有相应的模块

  \`\`\`Python

  import json

## 写入数据

data = {"name":"brian", "age":19} with open\("data.json",'w'\) as file\_object: json.dump\(data, file\_object\)

## 读出数据

with open\("data.json"\) as file\_object: readdata = json.load\(file\_object\)

print\(readdata\)

```text
- 下面这个例子演示了如何提示用户输入一个名字，存入json文件，然后再从文件中读取这个数据
```Python
import json

filename = "name.json"

user_name = input("Enter your name here:")

with open(filename,'w') as file_object:
    json.dump(user_name, file_object)

with open(filename) as file_object:
    name = json.load(file_object)

print(name)
```

* 代码重构：一个函数通常应该有一个单一固定的功能，避免多种功能混用。当发现一段代码的功能较为复杂时，应该尽量拆分。

### 11. Testing your code

