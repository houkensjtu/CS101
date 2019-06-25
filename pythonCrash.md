## Python crash course 

整本书分为两大部分，Part I介绍了Python从基本语法，到函数以及类的基本概念，Part II包含三个Projects，第一个是射击游戏，第二个是数据可视化，第三个是
Web application。虽然内容不是很高深，但是循序渐进使得内容比较多，希望可以持之以恒，一步一步看完敲完。

### Part I : BASICS

### 1. Getting started
- 安装Python，使用Python3。
- 写一个Hello world程序，并用解释器或者脚本模式运行。
- Python3和Python2的3个明显区别，print语句，除法运算和用户输入。
```Python
# Python2中导入__future__这个特殊模块，就可以像3一样使用print和除法运算
from __future__ import print_function, division

# Python3中的input语句会将用户输入变成一个字符串
s_number = input("Input a number and hit [Enter]:")
```

### 2. Variables and simple data types
- 变量命名规则，不要使用Python关键字
- 如果打错字导致变量名没有声明过，Python会给出NameError
```Python
message = "Hello"
print(messg)
# => NameError : name 'messg' is not defined.
```
- String型
  - 在Python中用双引号和单引号都可以表示string，没有区别
  - .upper(), .lower()和.title()用来转换string的大小写
  - 用+运算符来组合string
  - 在String中用"\n" "\t"表示换行和tab，用"\'"在字符串中表示引号
  - 用.strip()来除去字符串中的空格
- int型 : Python3中的除法会自动将1/2的结果转换成0.5
- float型 : 指数运算在python中是两个星号**

- 在解释器中输入import this可以查看Then Zen of Python

### 3. Introducing lists
- List在Python中方括号定义，List中的元素不需要同类型
- 取用List元素时也用方括号表示index，注意List的元素都是从0而不是1开始;-1代表的是List中最后一个元素。
```Python
motorcycles = ["honda","yamaha","suzuki"]
```
- List是可以动态加减的，也就是说，可以在程序运行过程中增减元素。例如，在一个游戏中你用List存储alien的个体。画面中显示的
alien需要不断增加或者删除，这个时候就需要动态修改List的元素。
```Python
# 在List末尾添加元素
motorcycle.append("ducati")

# 插入元素
motorcycle.insert(0,"ducati")

# 删除一个元素
del motorcycle[1]

# 推出一个元素
popped = motorcycle.pop()
# pop()之后motorcycle就少了一个元素，而这个元素被保存到了popped变量中

# pop也可以接收参数，推出list中任意位置的元素
# 这里是pop出第一个元素
popped = motorcycle.pop(0)

# 移除一个特定值的元素; 注意remove只移除list中首次出现的值，如果要移除全部重复出现的元素，需要用循环来实现
motorcycle.remove("ducati")
```

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

- List的长度,len()
```Python
len(car)
```

### 4. Working with lists
- 循环遍历List的每个元素是对List的一种普遍操作。
```Python
# 一个简单的遍历例子
# 注意for循环格式，末尾要有冒号; 另外，magician只是一个暂时的变量名，可以随便取
magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician)
```

- Python的for循环语句，需要一个冒号结尾，循环体则用indent来标识。

- 生成数字序列用的是range这个函数（numpy里用的则是numpy.arange这个函数，生成的就是矩阵而不是List了）
```Python
for i in range(1,5):
    print(i)
# 注意这里只会打印出1,2,3,4
```
- **注意range()返回的并不是list，而是一个range**，可以用list(range())来将其转换成List
```Python
numbers = list(range(1,6))
print(numbers)
# [1,2,3,4,5]

# range的第三个参数是调整间隔用
evenNumbers = list(range(1,10,2))
print(evenNumbers)
```

- 数字list可以使用min，max等简单函数来处理
```Python
>>> digits = [0,1,2,3,4,5]
>>> min(digits)
0
>>> sum(digits)
15
```

- **高级概念：List comprehension**
```Python
# 普通的生成方法
square = []
for i in range(1,5):
    square.append(i**2)
    
# List comprehension大法，一行解决从声明，循环到添加元素
square = [i**2 for i in range(1,5)]
```

- List的切片(slicing);同样用的是方括号，括号中用冒号隔开起始与终止元素。
```Python
# 注意这里的0:3切出的是第一，第二和第三个元素（0,1,2）
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# 切片也可以组合for循环使用;省略第一个元素的写法表示从0开始
for player in players[:3]:
    print(player)
```
- List的复制
```Python
my_foods = ["pizza", "falafel", "cake"]
friend_foods = my_foods[:]
# 这样就复制了一个list，从而使两个list互相独立

friend_foods = my_foods
# 这是复制了地址，这两个名字将指向同一个list
```

- 元组Tuple;定义时用括号而不是方括号，但是取元素时是一样的
```Python
dimensions = (200,30)
dimensions[0]
```

- PEP8代码风格指南
    - indent推荐使用4个空格，不使用tab
    - 一行推荐不超过80个字符

### 5. If statement

- Python的if语句不需要括号条件，语句后面需要加冒号，与for保持一致
```Python
cars = ["bmw","subaru","toyota","audi"]

for car in cars:
# 这里注意的是if文的条件，不需要用括号
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
 
 >>> BMW
     Subaru
     Toyota
     Audi
```

- 复合多个逻辑条件,Python中用的是and和or关键字
```Python
>>> age_0 = 18
>>> age_1 = 21
>>> age_0 >= 22 and age_1 >= 22
False
```

- 检查一个元素是否在list中: in关键字;反之，检查是否不在list中，用not in关键字
```Python
>>> requested_toppings = ["mushroom","onions","pineapple"]
>>> "mushroom" in requested_toppings
True
>>> "pepperoni" in requested_toppings
False
>>> "pepperoni" not in requested_toppings
True
```
