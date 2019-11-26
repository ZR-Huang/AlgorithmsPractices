# Practice-of-Algorithm

> This repository is used to store the code I implemented when I learn about algorithm. 

## Source code of Grokking Algorithms

The practiced source code when I read <[Grokking Algorithms](https://book.douban.com/subject/26979890/)>, which are almost similar to the examples presented in the book.



## Divide and Conquer Algorithms

​	This is the first course of [Algorithms Specialization](https://www.coursera.org/specializations/algorithms) offered by Stanford University, which I have studied in the Coursera. The codes in this folder are the practice in the class.

### Week 1
- The implementation of the Merge Sort algorithm. (Code: Week1_MergeSort.py)
- Compute the product of two large integers using the Karatsuda algorithm. (Code: Week1_IntergerMultipy.py)

### Week 2
- The implementation of counting the inverse pairs leveraging the Merge Sort algorithm. (Code : Week2_CountInversion.py)
- The code of weekly quiz. (Code: Week2_CountInversionForExam.py, Input data: Week2_IntegerArray.txt)
    - 1<= array[i] <= 100000

### Week 3
- The implementation of the Quick Sort algorithm, which uses three different methods of choosing the pivot.
    1. Choose the first element as the pivot.
    2. Choose the last element as the pivot.
    3. Choose the median of [the first element, the last element, the median element]

Note: This main function of the code is to compute the number of the comparison between the elements, which also is the quiz of Week 3. (Code: Week3_QuickSort.py, Input data: Week3_QuickSort.txt)

### Week 4

4. RandomizedContraction.py 是第四周的内容，第四周主要介绍了随机选择算法，和图的表示，以及求解图的最小割集（通过 Random Contraction Algorithm)。该算法能成功求得最小割集的概率是$2/n(n-1)$，虽然看起来是小概率，但是已经算不错的结果，对于 Program Problem 中的问题（规模200个顶点），重复运行了十几次后能得到正确答案。数据集是kargerTestcase.txt（小规模），kargerTestcase2.txt（小规模），kargerMinCut.txt（Program Problem的数据集）。


## Leetcode

This folder keeps all the resolution code of [LeetCode](https://leetcode.com/) I wrote, which includes the comprehension of the problems.

The format of file names：The number of the problem in website_the name of problem

- Leetcode
    |
    |- Basic : The Subject of Basic Algorithm in the Leetcode Explore
    |- Competition : The resolutions of the weekly competitions

## Templates

The implementation of the basic functions of different algorithms which can be quickly modified and used in the competitions.