
## :hatching_chick:HTML Basics
HTML和CSS是最基本的网页构成元素。HTML负责记述网页结构和内容，CSS则负责记述这些结构和内容的大小，字体，排版及风格。

### 1. HTML的原子
HTML的构成原子，是一个一个的tag语句。这些语句的基本构成元素是：
1. 起始tag
2. 结束tag
3. 内容
4. 属性（optional）
```html
<p class="myMotto"> Be real. </p> 
```
注意属性在起始tag之内，与tag名用空格隔开，属性的值最好用引号包括起来。

#### Tag的嵌套
```html
<p class="myMotto"> Be <strong>real</strong>. </p> 
```

#### 没有内容的tag
有些tag并不需要内容，比如img图片tag，只需要在属性中指定图片的路径即可。（alt属性是在图片载入失败时显示的文字，作为一种最坏情况的安全手段）
```html
<img src="images/firefox-icon.png" alt="My test image">
```

### 2. HTML文件整体结构
1. !DOCTYPE html ： 一个默认的文件头，告诉浏览器这是html。
2. html : 包括整个文件的内容。
3. head : 文件的编码，网页在浏览器中显示的标题。
4. body : 网页的内容。

head和body是平行处于html之下的。

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```
小技巧：在现代文本编辑器(Sublime Text, Atom, VS code等)中键入html并用tab补全，大多会用自动填入如上模板的片段，无需自己一字一字打印。

### 3. 基础Tag们

#### 1. 标题

从h1到h6，自动带有上下左右的空padding。包括字体，大小和padding都可以在CSS中制定。
```html
<h1>My main title       </h1>
<h2>My top level heading</h2>
<h3>My subheading       </h3>
<h4>My sub-subheading   </h4>
```

#### 2. 段落

```html
<p> "When someone seeks," said Siddhartha, "then it easily happens that his eyes see only the thing that he seeks,
and he is able to find nothing, to take in nothing because he always thinks only about the thing he is seeking, 
because he has one goal, because he is obsessed with his goal. 
Seeking means: having a goal. But finding means: being free, being open, having no goal."
― Herman Hesse, Siddhartha </p>
```

#### 3. 列表

无序列表ul，有序列表ol，列表条目li。
```html
<ul> 
  <li>HTML      </li>
  <li>CSS       </li>
  <li>Javascript</li>
</ul>

<ol> 
  <li>Data structure  </li>
  <li>Algorithm       </li>
  <li>Operating system</li>
</ol>
```

#### 4. 链接

在a tag的属性中添加href属性，注意链接地址最好包含http://。
```html
<a href="http://newgame-anime.com/">New Game!!</a>
```

### 4. Table的写法
Table即是表格，用来显示格式化的数据。这里值得一提的是，曾经有用Table来进行HTML页面规划的方法，但是这种方法缺乏柔软性，且在写HTML时需要引入大量的Table Tag，修改起来也很麻烦。更为现代的方法是使用CSS来处理页面的空间设计，用表格进行规划的方法已经过时且应尽量被避免。
所有的表格内容都用table tag包括起来，其中每一行用tr(table row），每个元素用td（table data）表示。
```html
<table>
  <tr>
    <td>Breed</td>
    <td>Jack Russell</td>
    <td>Poodle</td>
    <td>Streetdog</td>
    <td>Cocker Spaniel</td>
  </tr>
  <tr>
    <td>Eating Habits</td>
    <td>Eats everyone's leftovers</td>
    <td>Nibbles at food</td>
    <td>Hearty eater</td>
    <td>Will eat till he explodes</td>
  </tr>
</table>
```

### 5. Form的写法
与上述的HTML元素不同，Form的目的是由用户向服务器方发送信息。其方式可以多种多样，比如文本输入区域，下拉列表，选择按钮等。

## :koala:CSS Basics
CSS与HTML一样并不是编程语言，而是一种用来进行对网页格式和风格进行管理的语言。CSS的基本工作原理就是对HTML中的元素进行指定性地定制。比如，将HTML中所有的p元素（段落）变成红色的CSS写法是
```css
p {
  color: red;
}
```
可以观察到这种语法多少有点类似于c，每个元素用{}包括，每个语句都用；进行断句。
利用CSS时，需要将CSS代码保存到文件中，并在HTML的head中进行如下的指定。
```html
<link href="styles/style.css" rel="stylesheet" type="text/css">
```

### 1. CSS的原子
CSS的最基本组成元素就是一个一个的rule set。每个rule都有一个selector来指定其作用的对象，至少一个属性名称和一个属性值。属性名称和属性值用:隔开。你也可以同时在一个rule set中指定复数个对象，比如
```css
p, li, h1 {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```
注意复数个对象之间，用逗号隔开。
#### Selector的种类
Selector并不一定是HTML中的tag名，也可以是属性或者其他值，而且这些条件都可以进行叠加，以方便对特定的元素进行定点的定制。比如
```css
table td{
  color : red;
}
```
这样的句式就是对所有table中的td元素进行指定(注意这里table和td之间是空格，不是逗号)。当然CSS还有很多很多可以指定的Selector，具体可以参考[MDN开发者档案](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors)。

### 2. 字体
为了使用一种新的字体，我们首先需要在html文件中链接这些字体。比如说，添加如下链接到index.html的head段就可以利用Google的免费字体OpenSans。
```html
<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
```

然后，我们就可以在css中指定使用这种字体，比如：
```css
html {
  font-size: 10px; /* px means 'pixels': the base font size is now 10 pixels high  */
  font-family: 'Open Sans', sans-serif; /* this should be the rest of the output you got from Google fonts */
  }
  
  h1 {
  font-size: 60px;
  text-align: center;
  }

  p, li {
  font-size: 16px;    
  line-height: 2;
  letter-spacing: 1px;
  }
```

### 3.Box的概念
就像前面提到的，现在html网页的布局不再使用以往的table来实现，而是通过在css中划分box来实现。Box具有属性包括：
- padding : 周围的空间大小（从文字到border）
- border : 边界线
- margin ： border外面的空间  
![alt text](https://mdn.mozillademos.org/files/9443/box-model.png "css box")

首先我们尝试给整个html页面加上一个背景颜色：
```css
html {
  background-color: #00539F;
}
```

我们可以这样定制我们的body，使其居中并具有固定的宽度600px，一定的边界，以及5px宽的黑色边界框：
```css
body {
  width: 600px;
  margin: 0 auto;
  background-color: #FF9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}
```
你还可以这样定制图片的布局，使得所有图片都自动居中：
```css
img {
  display: block;
  margin: 0 auto;
}
```
上述格式中margin后面有一个0一个auto的意味是，元素上方及下方取0，而左右侧取自动空余（也就是居中了）。

## :alien:Javascript Basics

Javascript是一种运行在浏览器中的程序语言，也就是说，只要你有安装浏览器，就可以运行Javascript，这使得编写运行Javascript程序比绝大多数其他语言都要容易。同时，由于今天的软件运行环境比以往都要更加的多样化(Windows，Mac，Linux，Smartphone，Tablet...)，而所有这些平台都拥有基本的浏览器，这使得Javascript先天更加容易接触到更多的用户。虽然在语言设计上Javascript受到很多诟病，但是需求驱动发展，Javascript近年迅速的发展使其已然成为程序员需要掌握的语言中不可或缺的一门。

### 1. 如何Hello World
首先我们需要在存放网页的文件夹中新建一个叫做scripts的文件夹，并新建一个main.js的代码文件来存放Javascript代码。然后，我们在html文件的body中最下方加入如下的指示，告诉浏览器寻找到我们的代码文件：
```html
<script src="scripts/main.js"></script>
```
这里把这条指示放到body最下面的理由是，html也像一般的程序代码一样，一般会被从上向下执行。试想如果我们将JS的命令放在body内容出现之前，那么代码中如果用到html body中的元素，浏览器就有可能找不到而出现奇怪的错误。  
在代码文件中我们填入下面的代码，其意义是选中html中的h1标题，并将内容替换成Hello World!
```Javascript
var myHeading = document.querySelector('h1');
myHeading.textContent = 'Hello world!';
```
![alt text](https://mdn.mozillademos.org/files/9543/hello-world.png "JS hello world")

### 2. Javascript佛脚语法
- 变量   
Javascript中存在数据类型(data type)的概念，但是变量是没有严格型定义的，变量可以存储整数，而后被改成字符或者任何。
```Javascript
// 语句后面的分号并不是必须的
var myVar;
myVar = "Hello";

// 声明和赋值也可以放到一起
var myVar = "Hello";
```

- 条件分歧
```Javascript
var iceCream = 'chocolate';
if(iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```

- 函数   
Javascript的函数定义使用关键字**function**，返回值使用return表示。
```Javascript
function multiply(num1,num2) {
  var result = num1 * num2;
  return result;
}
```

- 事件(event)   
交互式网页的核心就是可以相应各种事件。侦测用户的点击可能是最简单最常见的一种事件了：
```Javascript
document.querySelector('html').onclick = function() {
    alert('Ouch! Stop poking me!');
}

// 上述写法省略了声明html对象的步骤，也可以如下展开
var myHTML = document.querySelector('html');
myHTML.onclick = function() {};
```

- 一个交互式网页的简单例子   
下面这段代码抓取了网页中的图片元素，并侦测用户点击事件，在被点击时实现交换图片的效果。
```Javascript
var myImage = document.querySelector('img');

myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/firefox-icon.png') {
      myImage.setAttribute ('src','images/firefox2.png');
    } else {
      myImage.setAttribute ('src','images/firefox-icon.png');
    }
}
```
