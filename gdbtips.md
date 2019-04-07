## :beetle: My GDB Tips

GDB作为一种原始的debug工具，不受环境限制，且使用得当的情况下具有很高可定制性。

### 启动

GDB启动有几种模式，各有微弱区别：
- 命令行启动
```shell
# 仅仅启动GDB而不读取目标文件
$ gdb

# 启动GDB且读取file.o文件
$ gdb file.o
```

- TUI界面启动
```shell
# 读取文件的同时，显示GDB的图形debug界面，可同时观察文件代码
$ gdb file.o -tui
```

如果在启动时不注明-tui选项，将以命令行模式进入GDB。进入命令行模式后仍可以用组合键C-x C-a进入图形界面模式。
图形界面内类似Emacs的操作习惯，可以用C-x o在源代码和命令行间跳转。在源代码界面，可以用PageDown,PageUp或者方向键滚动观察代码。  
另外，GDB还具有一些不同的图形界面layout，可以在图形界面中用layout next命令调换。一般是添加一个观察函数呼叫堆栈，或者是观察register变量状态的窗口。

### 断点设置

当程序运行到特定代码时将程序停止的功能。除了简单的在某行某函数break，还可以设置条件断点，使得debug威力无穷。
```shell
# 以下命令大多意义自明，不再解释
(gdb) break linum
(gdb) break filename:linum
(gdb) break func
(gdb) break filename:func
(gdb) break ... if cond
```

另外，可以对目前所设置的断点进行观察和管理
```shell
(gdb) info break
```
所有的断点都有一个整数作为其编号，可以用编号对断点进行删除，或者添加条件
```shell
(gdb) delete bnum
```

### 变量观察

在断点时，可以通过以下的命令来观察某个变量
```shell
# 在每次断点时自动显示var的值
(gdb) display var

# 显示目前正在自动显示列表中的所有变量
(gdb) info display

# 仅仅输出一次变量var的值
(gdb) print var

# print和display都可以用多种格式打印变量值
(gdb) p/x var <= 16进制格式
(gdb) p/t var <= binary格式
```
更为强大的是，可以用info命令罗列变量，比如
```
# 列出目前所有的global变量
(gdb) info variables

# 列出目前函数内所有的local变量
(gdb) info locals

# 列出目前函数呼叫时的参数列表
(gdb) info args

```

### 函数操作
对于目前正在被呼叫的函数的堆栈进行观察。
```shell
(gdb) backtrace
(gdb) bt
```
