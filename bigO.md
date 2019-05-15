## :snail: The Big-O notation

以下是一些我从不同的资源获得的关于Big-O的学习资料汇总。

### 1. [All you need to know about big-o notation](https://medium.freecodecamp.org/all-you-need-to-know-about-big-o-notation-to-crack-your-next-coding-interview-9d575e7eec4) 
- 这篇文章比较粗略，作为背景入门阅读不错。
- Software is heavily based on data. 
- Big O notation, sometimes also called [“asymptotic analysis (渐进分析)”](https://en.wikipedia.org/wiki/Asymptotic_analysis), 
primarily looks at how many operations a sorting algorithm takes to completely sort a very large collection of data. 
(这个解释严格说太过笼统了)
- It does this with regard to “O” and “n”, ( example: “O(log n)” ), where
    - O refers to the **order of the function, or its growth rate**, and
    - n is **the length of the array** to be sorted.
- Example : f(n) = 6n^4 - 2n^3 + 5. When **n grows to infinity, 6n^4 is the only one that matters**. 
So the lesser terms, 2n^3 and 5, are actually just omitted because they are insignificant. 
Same goes for the “6” in 6n^4, actually. Therefore, this function would have an order growth rate, or a “big O” rating, of **O(n^4)**.
- The rating of **O(n log n) in general is the best** that can be achieved. 
Algorithms that run at this rating include **Quick Sort, Heap Sort, and Merge Sort**. Quick Sort is the standard
- Bubble / Insertion / Selection Sort run at O(n²). ([这个网站](http://bigocheatsheet.com/)收集了一些最常见算法的时间复杂度并可视化成了图表.)

### 2. [Problem Solving with Algorithms and Data Structures using Python](https://interactivepython.org/courselib/static/pythonds/index.html)

### 3. [Algorithm - Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms)   
Khan Academy在美国的人气挺高，亲眼看见过学生妹在Starbucks抱着Khan Academy在复习生物。于是抱着试试看的想法学习了Khan Academy的算法course
（不你这是哪门子的逻辑。。。）。学习了几章以后感觉课程的内容编排很合理，从介绍算法的背景，到简单算法的分析，从中引出了Big-O表示。
Let's get right INTO IT!(又来了。。）
