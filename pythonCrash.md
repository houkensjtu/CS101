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
