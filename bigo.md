# :snail: The Big-O notation

以下是一些我从不同的资源获得的关于Big-O的学习资料汇总。

## 1. [All you need to know about big-o notation](https://medium.freecodecamp.org/all-you-need-to-know-about-big-o-notation-to-crack-your-next-coding-interview-9d575e7eec4)

这篇文章比较粗略，作为背景入门阅读不错。号称all you need to know绝逼是诈骗:sweat:。

* Software is heavily based on data. 
* Big O notation, sometimes also called [“asymptotic analysis \(渐进分析\)”](https://en.wikipedia.org/wiki/Asymptotic_analysis), 

  primarily looks at how many operations a sorting algorithm takes to completely sort a very large collection of data. 

  \(这个解释严格说太过笼统了\)

* It does this with regard to “O” and “n”, \( example: “O\(log n\)” \), where
  * O refers to the **order of the function, or its growth rate**, and
  * n is **the length of the array** to be sorted.
* Example : f\(n\) = 6n^4 - 2n^3 + 5. When **n grows to infinity, 6n^4 is the only one that matters**. 

  So the lesser terms, 2n^3 and 5, are actually just omitted because they are insignificant. 

  Same goes for the “6” in 6n^4, actually. Therefore, this function would have an order growth rate, or a “big O” rating, of **O\(n^4\)**.

* The rating of **O\(n log n\) in general is the best** that can be achieved. 

  Algorithms that run at this rating include **Quick Sort, Heap Sort, and Merge Sort**. Quick Sort is the standard

* Bubble / Insertion / Selection Sort run at O\(n²\). \([这个网站](http://bigocheatsheet.com/)收集了一些最常见算法的时间复杂度并可视化成了图表.\)

## 2. [Problem Solving with Algorithms and Data Structures using Python](https://interactivepython.org/courselib/static/pythonds/index.html)

## 3. [Algorithm - Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms)

Khan Academy在美国的人气挺高，亲眼看见过学生妹在Starbucks抱着Khan Academy在复习生物。于是抱着试试看的想法学习了Khan Academy的算法course （不你这是哪门子的逻辑。。。）。学习了几章以后感觉课程的内容编排很合理，从介绍算法的背景，到简单算法的分析，从中引出了Big-O表示。 Let's get right INTO IT!\(又来了。。）

### Lesson 1 :smile: : Intro to algorithms

1. What is algorithm and why should you care?
   * Real world examples: Image compression for video chat; fastest route finding calculation in Google map; solar panel adjustment at NASA...
   * What makes a good algorithm : correctness vs. efficiency.
   * Tool for analyzing the efficiency: Actual runtime depends on machine -&gt; **asymptotic analysis \(渐进分析\)**
2. A guessing game
   * Computer will pick a number between 1-16. You guess the number. \(Computer will tell you too high or too low.\)
   * Linear search : Guess from 1 all the way to 16. Takes 16 guesses at most and 1 at least, 8 on average.
   * Binary search : Guess 8 at first, then shrink the range every step. Should take 4 steps at most.
   * How many steps does it take to guess 1-300? A: No more than 9. Because 2^8 = 256, 2^9 = 512.
3. Route finding
   * Route finding can be found in many very different-sounding problems:
     * How is the current Prince William related to King William III?
     * What path should a ghost follow to get to Pac-Man as quickly as possible?
     * What's the best way to drive from Dallas, Texas to Orlando, Florida?
     * Exploring a maze : how to navigate to the goal?   

       ![](https://cdn.kastatic.org/ka-perseus-images/7585425942be2a347bdab70bf68ef8dafe7bae02.png)      

       ![](https://cdn.kastatic.org/ka-perseus-images/1448249c9f4972b72248d899406a7f0c92fc5f3b.jpg)     

        A possible strategy: compute the distance from the goal for every cell, starting from the goal.
   * The implementation of this algorithm will be discussed in later chapter \(Javascript\).  
4. Discuss: Algorithms in your life
   * Find problem-solving algorithm in your life.

### Lesson 2 :laughing: : Binary search

补充一些关于binary search模型所隐含的，但是初学者可能不曾多想的模型假设：

* 所谓binary search指的是在一个**已知**的集合中\(在这里这个集合还必须是已经排序的\)，寻找一个**未知**的目标。比如猜一个1-100之间的数，集合本身有多少数，有什么数都是已经知道的，但是目标数字是多少？这是需要寻找的答案。
* 如果把情况反过来，集合是未知的，而目标数是已知的，比如我有一个数字的集合，但是我并不知道这里面有什么数字，然后我要寻找其中有没有53，此时binary search仍然可用，但是和第一种情况还是有微妙的不同。
* 如果**集合和目标都是已知的**，那就不存在binary search的问题了。比如我知道集合是1-100的自然数，我要查找的数是53，那直接去取第53个数就是了。

1. Describing binary search
   * The key is to **keep track of the current range** of reasonable guess.
   * At each turn, choose a guess that **divides the range into 2 equal size parts**. Then, update the max/min bound according to the result.   
   * For example, suppose the current range is \(26,80\). Take the guess as \(26+80\)/2=53. If the result says 53 is too high, you assign max = 53. Thus, the size of the problem is reduced to half.   

     ![](https://cdn.kastatic.org/ka-perseus-images/91981c0666c061815dd0e9b473ad0570a1803a45.png)   

     ![](https://cdn.kastatic.org/ka-perseus-images/a376ce2d2746fc126293571121a818f395a97354.png)
2. Pseudocode
   * Let min = 0 and max = n-1.
   * Compute guess as the average of max and min, rounded down \(so that it is an integer\).
   * If array\[guess\] equals target, then stop. You found it! Return guess.
   * If the guess was too low, that is, array\[guess\] &lt; target, then set min = guess + 1.
   * Otherwise, the guess was too high. Set max = guess - 1.
   * Go back to step 2.
3. Implementation
   * Use Javascript; other language should be equally possible.
   * Input : an array of numbers and the target. Output : the index of the location where the value is found.
4. Running time of binary search
   * Every time the size of the problem will be halfed.
   * For an array of n numbers, the number of guesses would be log2\(n\). \(&lt;-the worst case\)
   * log grows much slower than linear function.

### Lesson 3 :dizzy\_face: : Asymptotic notation

1. What is Asymptotic notation
2. Running time of the algorithm is a function of the **size of its input**.
3. We must focus on how fast a function grows with the input size. We call this **the rate of growth of the running time.**
4. Drop the constant coefficient and lower order terms.
   * For example, for 6n^2 + 10n + 300, We would say that **the running time of this algorithm grows as n^2.**
5. There are 3 forms of asymptotic notation: big-O, big-Omega and big-Theta
6. Big-Theta notation

   ```javascript
   // Linear search example
   var doLinearSearch = function(array, targetValue) {
   for (var guess = 0; guess < array.length; guess++) {
    if (array[guess] === targetValue) { 
        return guess;  // found it!
    }
   }
   return -1;  // didn't find it
   };
   ```

7. Each time of the for-loop, it has to do several things:
   * compare guess with array.length
   * compare array\[guess\] with targetValue
   * possibly return the value of guess
   * increment guess.
8. When we say that a particular running time is \Theta\(n\) Θ\(n\), we're saying that once n nn gets large enough, the running time is at least k1  _n and at most k2_  n for some constant k1 and k2.
9. When we use big-Θ notation, we're saying that we have **an asymptotically tight bound** on the running time. "Tight bound" because we've nailed the running time to **within a constant factor above and below.**
10. Big-O notation \(一个算法growth rate的上限\)
11. It would be convenient to have a form of asymptotic notation that means "the running time grows **at most this much, but it could grow more slowly."** We use **"big-O" notation** for just such occasions.
12. We can make a stronger statement about **the worst-case running time** of binary search: it's Theta\(log2\(n\)\). But for a blanket statement that covers all cases, the strongest statement we can make is that binary search runs in O\(log2\(n\)\).
13. If we say that a running time is Theta\(f\(n\)\), then **it's also O\(f\(n\)\).**
14. Because big-O notation gives only an asymptotic upper bound, and not an asymptotically tight bound, we can make statements that at first glance seem incorrect, but are technically correct. For example, **it is absolutely correct to say that binary search runs is O\(n\).**
15. Big-Omega notation \(一个算法growth rate的下限\)
16. If a running time is Omega\(f\(n\)\), then for large enough n, the running time is at least kf\(n\).
17. We say that the running time is "big-Omega of f\(n\)". **We use big-Omega notation for asymptotic lower bounds.**
18. We can also make correct, but imprecise, statements using big-Omega notation. 
19. we can correctly but imprecisely say that the worst-case running time of binary search is Omega\(1\), because we know that it takes at least constant time.

