## Learn Julia!

> [Julia Tutorial from University of Pennsylvania](https://www.sas.upenn.edu/~jesusfv/Chapter_HPC_8_Julia.pdf)

### Section 1 : Install
- Julia遵循目前流行的软件发行模式：其核心语言和周边package模块分开，而周边package有一个专用的ecosystem进行管理。
- 在Linux或者Windows上，Julia都可以直接从官网下载二进制运行程序。也可以通过Atom的IDE(Juno)来安装。
- 在Julia的REPL中，键盘的]键代表进入pkg管理模式，;代表进入系统shell模式
    - 在pkg管理模式
        - st : 显示当前所有的包包的状态
        - add xxx : 导入一个新的包包
        - rm xxx : 删除一个包包
        - up xxx : 更新一个包包
     - 安装包包后退出到正常的REPL中，使用using xxx命令来使用这个包包。初次引用会需要一些时间来编译处理这个包包。
     - 安装Julia notebook的简单流程：
         - 在pkg管理模式中add IJulia
         - 在REPL中using IJulia
         - 启动: notebook()
 - 变量类型:Julia是一门动态型语言，也就是说，变量不需要在声明时给定类型，也可以在运行时改变其类型。但是Julia是一门强类型语言，就是说不同类型的变量
   相互间的操作一般是不允许的。
```Julia
a = 2.0
b = "Hello"
a + b # Error!

# 确认a的类型
typeof(a)
```
### Section 2 : Fundamental commands

```Julia
# 一些基本变量定义
a = 2
a = 3.14
a = "Hello!"
a = true

# Julia中内置了检查变量的2进制表达式的方法
bitstring(a）

# 基础数学运算
x = 2
# "+" 的两种写法
2 + x
+(2,x)

# *乘号在一些情况下可以省略成更人性化的形式
3*x
3x # 新写法

# 一些基本的数学函数
sin(x)
abs(x)
sqrt(x)
log(x)
```

### Section 3 : Arrays
