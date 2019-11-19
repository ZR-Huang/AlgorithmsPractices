# Practice-of-Algorithm

> This repository is used to store the code I implemented when I learn about algorithm. 

## Source code of Grokking Algorithms：

    The practiced source code when I read [<Grokking Algorithms>](https://book.douban.com/subject/26979890/), which are almost similar to the examples presented in the book.



## Divide and Conquer Algorithms

​	是我在Coursera上，学习Stanford 的算法专题课程中的第一个课程。里面是上课过程中所涉及的练习。

1. MergeSort.py 是根据 WEEK1 老师所给算法实现的归并排序。IntegerMultiply.py 同样是第一周的内容，利用 Karatsuda 算法来计算两个大整数的积。
2. CountInversion.py 是根据老师的算法自己实现的程序，CountInversionForExam.py 是针对于 WEEK 2 的测试的代码，其数据集是 IntegerArray.txt（数据范围[1,100000]）
3. QuickSort.py 是第三周的内容，大家所熟悉的快速排序这个算法里面用了三种不同的方式来选择 pivot. (1) 总是以列表的第一个元素作为 pivot；（2）总是以列表的最后一个元素作为 pivot；（3）从列表的头元素，尾元素，以及中间的元素，三个元素中选择**其值**刚好排在中间的元素。该代码主要是计算在排序过程中，元素之间进行比较的次数（该问题就是第三周的 Program Problem)，数据集是 QuickSort.txt
4. RandomizedContraction.py 是第四周的内容，第四周主要介绍了随机选择算法，和图的表示，以及求解图的最小割集（通过 Random Contraction Algorithm)。该算法能成功求得最小割集的概率是$2/n(n-1)$，虽然看起来是小概率，但是已经算不错的结果，对于 Program Problem 中的问题（规模200个顶点），重复运行了十几次后能得到正确答案。数据集是kargerTestcase.txt（小规模），kargerTestcase2.txt（小规模），kargerMinCut.txt（Program Problem的数据集）。



## Leetcode

This folder keeps all the resolution code of [LeetCode](https://leetcode.com/) I wrote, which includes the comprehension of the problems.

The format of file names：The number of the problem in website_the name of problem
