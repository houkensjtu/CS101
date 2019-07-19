## Python type hint :melon:

最初注意到这个话题是因为看到一个很棒的[live coding视频](https://www.youtube.com/watch?v=o64FV-ez6Gw)，从0搭建一个deep learning的library。
作者在编码过程中反复强调了使用Python的新特性type annotation。这个型注释到底是什么东东？

```Python
# 由于Python是动态型语言，变量名本身不和变量类型绑定，变量可以代入任何类型的值
age = 1
print(age) # => 1 
age = "one"
print(age) # => one 
```
```Java
// Java里是不允许这样的代入的，因为Java中变量名和类型有绑定关系
int age = 1;
System.out.println(i);
age = "one";
System.out.println(i); // => Error!
```

Python的动态特性使得编程变得非常自由，也简化了很多编程中不必要的复杂手续。但是缺少型绑定也有很多实际的缺点。类型注释的出现有助于改善这些问题：   
### 1. 代码存在一些潜在的bug危险
```Python
def get_first_name(full_name):
    return full_name.split(" ")[0]

fallback_name = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

raw_name = input("Please enter your name: ")
first_name = get_first_name(raw_name)

# If the user didn't type anything in, use the fallback name
if not first_name:
    first_name = get_first_name(fallback_name)

print(f"Hi, {first_name}!")
```

以上这段代码，**在用户正常输入名字的时候是没有问题的**。但是当用户没有输入任何东西，first_name为空的时候，
程序会试图呼叫get_first_name(fallback_name)这个方法，fallback_name可以看到是一个Dict而不是字符串，所以没有split这个方法，
故这段代码就会崩溃。   
**这个小bug的恶劣性在于，由于Python没有任何事先的类型检查机制，在运行时看上去是没有问题的**。甚至哪怕你尝试测试这个程序千百遍，
但是由于你没有想到用户会不输入任何名字，所以你没有检查到get_first_name(fallback_name)这段代码。   
```Python
# 现在有了类型注释
# 所有基本变量类型以外的复合类型可以从typing中引入
from typing import Dict

def get_first_name(full_name: str) -> str:
    return full_name.split(" ")[0]

fallback_name: Dict[str, str] = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

raw_name: str = input("Please enter your name: ")
first_name: str = get_first_name(raw_name)

# If the user didn't type anything in, use the fallback name
if not first_name:
    first_name = get_first_name(fallback_name)

print(f"Hi, {first_name}!")
```
现在给代码添加了注释以后，从运行上来说是没有任何影响的。但是在运行前我们就可以用mypy这个小工具来检查类型的一致性：

```
$ mypy typing_test.py

test.py:16: error: Argument 1 to "get_first_name" has incompatible type Dict[str, str]; expected "str"
```

其他关于复杂复合数据类型的注释方法，可以在官方文档中找到。   

### 2. 代码可读性

试想你看到如下一段简单到不能再简单的代码。可是这个函数到底是要干嘛？事实上你得寻找其他的上下文来寻找，因为a, b, times这些
输入即可能是数字，也可以是字符或者字符串，且程序都能正常运行，只是结果全然不同。   
在一个这样简单的问题中你也许并不需要花太多时间就能找到答案，但是当你阅读非常庞大的代码库的时候，来回寻找一段代码的含义
会非常耗费时间和精力。
```Python
# Our original function
def mystery_combine(a, b, times):
    return (a + b) * times
```
相比之下如果你使用了类型注释：
```Python
# Our original function
def mystery_combine(a:str, b:str, times:int)->str:
    return (a + b) * times
```
代码的意图和调用方法在你看到代码的时候就明确了很多，甚至这样的注释比用语言写comment更加有效简洁。

### 3. IDE的补全功能
没有型注释的时候，IDE对变量的类型没有任何概念，这使得代码补全有时候无法很好的工作。就比如上面的a和b，如果添加了型注释，
IDE就可以知道这些是str类型的变量，从而在你输入"a."的瞬间，提示你str类型可以用的方法有哪些。这算是一个比较小的点，
但是也是型注释的好处之一。


参考文章：
- [How to Use Static Type Checking in Python 3.6](https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b)
- [Using Python's Type Annotations](https://dev.to/dstarner/using-pythons-type-annotations-4cfe)
- [The other (great) benefit of Python type annotations](https://medium.com/@shamir.stav_83310/the-other-great-benefit-of-python-type-annotations-896c7d077c6b)
