
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

### 4. Table
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

### 5. Form
与上述的HTML元素不同，Form的目的是由用户向服务器方发送信息。其方式可以多种多样，比如文本输入区域，下拉列表，选择按钮等。

## :koala:CSS Basics
## :alien:Javascript Basics
