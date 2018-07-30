# Practice-of-Algorithm-diagram

> 主要用于存放自己在学习算法的过程中，练习的代码，以供今后 review，并继续优化改进。

## 《算法图解》练习：

​	是我在看[《算法图解》](https://book.douban.com/subject/26979890/)的时候，根据书本上的例子，所练习的代码，基本与书本上的所给的示例代码相差不大。

---

## Divide and Conquer Algorithms

​	是我在Coursera上，学习Stanford 的算法专题课程中的第一个课程。里面是上课过程中所涉及的练习。

1. MergeSort.py 是根据 WEEK1 老师所给算法实现的归并排序。IntegerMultiply.py 同样是第一周的内容，利用 Karatsuda 算法来计算两个大整数的积。
2. CountInversion.py 是根据老师的算法自己实现的程序，CountInversionForExam.py 是针对于 WEEK 2 的测试的代码，其数据集是 IntegerArray.txt（数据范围[1,100000]）
3. QuickSort.py 是第三周的内容，大家所熟悉的快速排序这个算法里面用了三种不同的方式来选择 pivot. (1) 总是以列表的第一个元素作为 pivot；（2）总是以列表的最后一个元素作为 pivot；（3）从列表的头元素，尾元素，以及中间的元素，三个元素中选择**其值**刚好排在中间的元素。该代码主要是计算在排序过程中，元素之间进行比较的次数（该问题就是第三周的 Program Problem)，数据集是 QuickSort.txt
4. RandomizedContraction.py 是第四周的内容，第四周主要介绍了随机选择算法，和图的表示，以及求解图的最小割集（通过 Random Contraction Algorithm)。该算法能成功求得最小割集的概率是$2/n(n-1)$，虽然看起来是小概率，但是已经算不错的结果，对于 Program Problem 中的问题（规模200个顶点），重复运行了十几次后能得到正确答案。数据集是kargerTestcase.txt（小规模），kargerTestcase2.txt（小规模），kargerMinCut.txt（Program Problem的数据集）。

---

## Leetcode

主要存放了，我在[LeetCode](https://leetcode.com/)上练习所写的代码。

文件命名格式：自己的编号.题目名称(网站上对应的编号)[网站上对应难度]