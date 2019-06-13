## Polyglot cheatsheet :monkey:

### 1. 基本程序结构

#### C
```C
// 文件命名为xxx.c;编译时用gcc xxx.c生成a.out
#include <stdio.h>

int main(int argc, char* argv[]){
  printf("Hello world!\n");
}
```
#### Java
```Java
// 文件命名为xxx.java，注意xxx要和class名字一致;编译时用javac xxx.java，然后用java xxx执行
public class Hello{
   public static void main(String[] args){
      System.out.println("Hello world!\n");
   }
}
```
#### Python

```Python
# 单纯import的话，程序中可以用xxx.yyy来访问module中的函数
import xxx
import xxx as X

# 用了from特定某个函数以后，就可以直接用yyy来呼叫函数
from xxx import yyy

# 用wildcard导入所有函数，这样容易导入自己并不知道的函数，导致很多问题，不推荐
from xxx import *

# __future__是个特殊模块
from __future__ import division, print_function

# 导入多个模块时不推荐用逗号，同个模块多个函数可以使用逗号
import xxx
import yyy
from xxx import yyy, zzz
```
#### Javascript

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

source.js里就是Javascript本人了:

```Javascript
// Javascript的字符串也是不区分单双引号，和Python一样
console.log("Hello world!")
```
