
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

### Tag的嵌套
```html
<p class="myMotto"> Be <strong>real</strong>. </p> 
```

### 没有内容的tag
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

1. 标题

从h1到h6，自动带有上下左右的空padding。包括字体，大小和padding都可以在CSS中制定。
```html
<h1>My main title       </h1>
<h2>My top level heading</h2>
<h3>My subheading       </h3>
<h4>My sub-subheading   </h4>
```

2. 段落

```html
<p> "When someone seeks," said Siddhartha, "then it easily happens that his eyes see only the thing that he seeks,
and he is able to find nothing, to take in nothing because he always thinks only about the thing he is seeking, 
because he has one goal, because he is obsessed with his goal. 
Seeking means: having a goal. But finding means: being free, being open, having no goal."
― Herman Hesse, Siddhartha </p>
```

3. 列表

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

4. 链接

在a tag的属性中添加href属性，注意链接地址最好包含http://。
```html
<a href="http://newgame-anime.com/">New Game!!</a>
```

## :koala:CSS Basics
## :alien:Javascript Basics
