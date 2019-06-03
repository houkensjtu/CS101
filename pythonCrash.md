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
