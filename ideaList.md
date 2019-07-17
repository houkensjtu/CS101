## Personal project ideas

在任何面试过程中，有没有Personal project，以及Personal project的质量如何，都是非常至关重要的因素之一。Personal project的高度直接体现了被面试者的技能
水平和视野宽度深度。在Quora上有Amazon的面试官提出，在简历上写一些Naive的project描述反而是非常减分的red flag。比如说你用Python写了一个网络爬虫，
或者做了一个显示新闻的Android app，这些没有实际意义，也没有太多技术深度的项目是非常让面试官反感的，体现出被面试者在技术上的水平和热情都很平庸，往
往会导致直接在简历阶段被叉。   
可以看到，在建立Personal project的过程中，选择一个有意义的课题本身就是一个很重要的课题。这里记录一些我对于Personal project的点子，如果有同学有什么
意见或者建议都欢迎提出，同时也欢迎借鉴。

### Fizzbuzz
这是一个很常见的filtering面试题，用来看面试者是不是具有最最基础的编程常识。[这位仁兄](https://docs.google.com/presentation/d/16aTSekqJdF-WjxymEnfiNvJI-StY0deCYBWiZxhPbyI/edit#slide=id.g18aab039ee_0_94)受够了这种智商的侮辱以后，决定用Tensorflow来写一个机械学习
版的Fizzbuzz。idea也非常简单，就是让tensorflow学习出一个function，对于input输出正确的fizz，buzz或者fizzbuzz。
感觉这会是一个非线性的logic regression，如果可以摆脱tensorflow，写出一个barebone的版本，是不是更加有趣呢？


### Serial port library 

### AI data reader
在做物理实验的过程中，往往需要记录各种仪器的读数。有些仪器具有remote control端口，可以实现用电脑监控读数的功能，但是有些仪器不具有这些功能，
甚至有些需要机械调节的元件，更无法自动记录数据。于是在实验室中传统的做法就是做一个Laboratory note，手动记录这些部分的数据。长此以往，
手动记录的数据越积越多，很多可能潜在的insight都因为无法用计算机批量处理，而被埋没在了这些笔记中。但是要求实验人员每天都把手动记录的数据都
输入到计算机中，又是一项繁琐而耗时的工作。   
为了解决这样的问题，是否可以设计一个固定的数据表格，然后用AI读取扫描后的手动记录图片，然后把识别出来的数据自动整理成比如json文件归档。

### Windows file browser
Windows目前自带的文件浏览器，只能打开一个窗口且没有tab功能，有时候需要在多个文件夹间移动文件时需要一个一个打开，虽然现在Win10有了屏幕分割
功能，但是一个一个打开文件夹还是非常繁琐，而且这些文件夹一旦关闭，下次如果进行同样的工作时，由于没有记忆，又需要一个一个打开。   
为了解决这样的问题，其实有一个小众软件叫做[Q-dir](https://www.softwareok.com/?seite=Freeware/Q-Dir)，只是年久失修界面比较古老，而且窗口数量也有限制最多只能打开4个，如果能够做出一个可以打开
任意数量窗口，自动排版，且记忆窗口历史的软件，应该会大大提升用户的体验。

### Chrome/Firefox design calculator
在从事工业设计的过程中，需要进行很多有一定复杂程度的设计计算。这些计算虽然不到数值模拟那么复杂，但是旧有的手工计算方法还是显得过于繁琐。
另一方面，用Excel制作的计算sheet虽然可以实现一定的计算功能，但是在文本记述上不够丰富，往往只有一面数据，哪怕是设计计算的人本身，几个月以后
再看自己的计算也会需要一定时间去回忆计算过程。最后，用Python等编程语言编写的程序，虽然可以满足很丰富的计算需求，甚至用Jupyter可以实现丰富的
文本表达，但是受限于运行环境，很多做工程设计的从业者并不一定安装有这些编译器，导致编写的程序最终只能成为自己的一个玩具而无法推广。    
这里，如果可以利用Chrome/Firefox编写一个Javascript的计算程序，不仅可以集成比如Mathjax的公式编写，d3js的可互动图表，更好的是只要电脑上
有浏览器就可以运行，大大提高了程序的可推广程度。    
另外，编写插件也是很好的一个练习类似前端开发的机会。

### Recurse center
[Recurse center](https://www.recurse.com/)是一个坐落于NYC的Brooklyn的程序员活动组织，前身称为The hacker school。Recurse center召集来自全世界的程序员，在一起自发地进行
hack和学习活动。整个组织并没有明确的课程和目标，所有的过程都是由参加者自行发起。目前，加入Recurse center需要[申请面试](https://www.recurse.com/apply)。Recurse center声称他们
看重[申请人如下的特质](https://www.recurse.com/what-we-look-for)：
#### 1. You enjoy programming.
你需要展示你很喜欢编程。你可以给面试官看你的个人blog，或者是你写的代码，证明你在业余时间也做了很多研究和活动。
我现在已经有Github作为自己的portfolio，需要进一步考虑的是，关于每个我正在学习的技术，我有什么样的passion和视野。（<-此处需要进一步思考）
#### 2. You want to get dramatically better.
你不需要在编程上已经处处完美，相反，你完全可以只具有很少的编程经验。但是，你必须要知道自己想要提高什么，以及如何提高。
结合自己以前在hacker school的经验，你所配对到的mentor虽然可能有一定知识，但未必具有高瞻远瞩可以指导你整个方向的进展，很多时候你说你不懂一个方面，
他很可能就会告诉你你可以看这些东西提高这个方面，所以你要对自己真正的方向和视野有一个清晰的认识的基础之上，再去和mentor交谈才会收获最多。
#### 3. You’re self-directed.
这一点比较简单，就是展示你可以自己指导并控制自己进行一个项目的进展。
#### 4. You’re sharp.
你需要展示你具有一定的思考能力。这里所说的sharp并不一定是要关于软件，你可以用任何你在过去生活工作中的经验，证明你是一个善于乐于思考的人。
#### 5. You’re intellectually curious. 
你需要展示你对新知识有好奇和渴求。在申请表中有一个问题是，请描述一个你最近学到的让你激动的新事物。这个事物或者知识并不需要和软件有关，
你只要展示，你对学习新东西具有激情即可。

对于只有一周的mini retreat来说，以上的要求全部都适用，但是会比较严格。面试官会逐一审视你是否清晰地展示了上述所有特质，以保证你在center
会有一个有成效的学习过程。

