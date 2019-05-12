## Javascript １日で基本が身につく！

### Chapter 1 环境搭建

#### Section 1 Javacript概要

Javascript诞生于90年代。最早的Javascript的应用非常局限，主要就是控制一些弹出窗口，以及在用户输入栏对输入格式进行一些简单的格式检查。随后在2000年后
Html5格式发布，推出了很多和Javascript结合的协议，使得Javascript可以实现更多交互的功能，才引发了现在Javascript的流行。

#### Section 2 开发环境

用于学习的开发环境主要包括三大元素：
- 浏览器（如果是开发Node.js程序的话，需要安装Node）
- 编辑器（传统的有Vim和Emacs，新兴IDE的话有Sublime,Atom,VS Code等等;2019年现在VS Code非常流行）
- 服务器（用于模拟真实的Web server）

**服务器**的选择比较多，可以想到的选择有：
- Apache
- Python
  在Python3中开启服务器的命令是：
  ```Shell
  # Python2
  $ python -m SimpleHTTPServer
  
  # Python3
  $ python3 -m http.server
  ```
- Node.js   
  Node需要安装一个http-server的包来执行服务器的功能。
  ```Shell
  $ npm install -g http-server
  $ http-server
  ```
- VS Code自带的服务器功能   
  VS Code中有一个叫做Live Server的插件，安装以后只要在编辑的网页文件右下方点击Go live就能直接把文件送上服务器。
  
**浏览器**选择Google Chrome，Chrome中有一个Developer tool是开发必备的调试工具。打开Developer tool有多种方法，可以在菜单中选择More tools...
-> Developer tools，或者使用快捷键Ctrl+Shift+I。

### Chapter 2 Javascript基础语法

#### Section 1 Javascript基本规则

Javascript的代码可以写在html文件里面，也可以建立一个js源文件从html里面引用。引用源文件的方法更加规范，便于管理。

```html
<script> 
在这里直接写Javascript也不是不可以...
</script>

// 这样做就规范多了
<script src="source.js"></script>
```

顺便复习一下，html的最简单结构是这样的：
```html
<!DOCTYPE html>
<html>

<head>
<script src="source.js"></script>
</head>

<body>
<h1>Hello world!</h1>
</body>

</html>

```

#### Section 2 命名变量

变量的命名可以使用var或者let关键字。（顺带一提，Javascript中语句**可以也可以不使用分号结尾**，只有多个语句并列一行时必须使用分号隔开）
```Javascript
var i = 42;
let j = 21;
```
var和let基本是同样的功能，**但是var有一些旧Javascript固有的奇特属性**，因而导致很多bug问题，故现代的Javascript更推荐使用let关键字。
var的奇特属性主要有两个：
- 隶属于function但可以穿透block。在下面的例子可以看出，if文的block结束之后，test依然可以从外部访问。
```Javascript
if (true) {
  var test = true; // use "var" instead of "let"
}

alert(test); // true, the variable lives after if
```
- 定义提升。一般的编程语言都要求变量先定义，再使用。但是如同下面的例子，var声明的变量可以写在后面，在运行时系统会自动先寻找var所以执行不会出错。
```Javascript
function sayHi() {
  phrase = "Hello";

  alert(phrase);

  var phrase;
}
```

定义数组和对象时，同样使用let关键字。
```Javascript
let myList = [1,2,3,4];
let myObject = {name:"houken", hobby:"programming"};
```
访问数组对象时使用方括号，访问对象成员时，可以用方括号，也可以用dot标记。
```Javascript
myList[0]; //=>1
myObject["name"]; //=>houken
myObject.hobby; //=>programming
```
