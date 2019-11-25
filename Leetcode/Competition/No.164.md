# 第164场周赛

> 这是第一次参加LeetCode的周赛，全国排名为762/1675。在比赛中只解出了前两题。

- [Solved] 表示在比赛中解出。
- [Unsolved] 表示在比赛中未能解出。

## [Solved] 1266.访问所有点的最小时间

### 题目描述：

平面上有`n`个点，点的位置用整数坐标表示`points[i] = [xi, yi]`。请你计算访问所有这些点需要的最小时间（以秒为单位）。

你可以按照下面的规则在平面上移动：

- 每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
- 必须按照数组中出现的顺序来访问这些点。

### 示例1:
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/1626_example_1.png)

```
输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
从 [1,1] 到 [3,4] 需要 3 秒 
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒
```

### 示例2:
```
输入：points = [[3,2],[-2,2]]
输出：5
```

### 约束条件：
- `points.length == n`
- `1 <= n <= 100`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`


### 解题思路：
这道题在进行对角线移动时，可以在单位时间内同时进行X轴和Y轴的移动。因此，在计算两个点的距离时，只需要计算这两点在Y轴和X轴上距离的最大值即可。
设平面上两点坐标`p0=(x0, y0),p1=(x1,y1)`，则他们的
横坐标距离差为`dx=|x0-x1|`，纵坐标距离差为`dy=|y0-y1|`。分三种情况来计算从`p0`移动到`p1`的最少移动次数。
- `dx < dy`：沿对角线移动`dx`次，再竖直移动`dy-dx`次，总计`dx+(dy-dx)=dy`
- `dx = dy`：沿对角线移动`dx`次
- `dx > dy`：沿对角线移动`dy`次，再竖直移动`dx-dy`次，总计`dy+(dx-dy)=dx`

对于任意一种情况，从`p0`移动到`p1`的最少次数为`dx`和 `dy`中的较大值`max(dx, dy)`，这也被称作`p0`和`p1`之间的切比雪夫距离。

参考：

[LeetCode官方题解](https://leetcode-cn.com/problems/minimum-time-visiting-all-points/solution/fang-wen-suo-you-dian-de-zui-xiao-shi-jian-by-leet/)

```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            time += max(abs(points[i+1][0] - points[i][0]),abs(points[i+1][1] - points[i][1]))
        
        return time
```

## [Solved] 1267.统计参与通信的服务器


### 题目描述：

这里有一幅服务器分布图，服务器的位置标识在 `m * n` 的整数矩阵网格 `grid` 中，1 表示单元格上有服务器，0 表示没有。

如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。

请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

### 示例1:
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-6.jpg)

```
输入：grid = [[1,0],[0,1]]
输出：0
解释：没有一台服务器能与其他服务器进行通信。
```

### 示例2:
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-4-1.jpg)
```
输入：grid = [[1,0],[1,1]]
输出：3
解释：所有这些服务器都至少可以与一台别的服务器进行通信。
```

### 示例3:
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-1-3.jpg)

```
输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
输出：4
解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。
```

### 约束条件：
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 250`
- `1 <= n <= 250`
- `grid[i][j] == 0 or 1`


### 解题思路：
方法一：

是我自己在比赛中想的方法。首先创建两个数组`row,col`，来统计每行每列都有几个设备，若第0行有2个设备，则`row[0]=2`，若第1列有3个设备，则`col[1]=3`。在`row,col`中，只要设备数量大于2，则满足条件。以示例2为例子，统计得到`row=[1,2], col=[2,1]`。
分别对`row,col`统计能够通信的设备总数时，会存在重复统计的情况，如示例2中`row[1]+col[0]=4`，`[1,0]`的设备被重复计算了一次，因此需要统计被重复计算的设备数量。

我们在对`row`进行统计的时候，如果`row[i]>=2`，则检查当`col[j]>=2`时，`grid[i][j]`是否为1，如果是则统计为重复的设备。

最后，能互相通信的设备总数为:
```python
sum([elem for elem in row if elem >=2 ]) + 
sum([elem for elem in col if elem >=2 ]) - 
duplicated_num
```
时间复杂度为：`O(MN+MN+N)=O(MN)`


```python
class Solution:
    def countServers(self, grid) -> int:
        row = [0] * len(grid)
        col = [0] * len(grid[0])

        for i in range(len(row)):
            for j in range(len(col)):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        duplicated = 0
        sum_of_row = 0
        for i, num in enumerate(row):
            if num >=2:
                sum_of_row += num
                for j, num_j in enumerate(col):
                    if num_j >= 2 and grid[i][j] == 1:
                        duplicated += 1

        sum_of_col = 0
        for num_j in col:
            if num_j >= 2:
                sum_of_col += num_j
        
        result = sum_of_col + sum_of_row - duplicated

        return result
```

## [Unsolved] 1268.统计参与通信的服务器


### 题目描述：

给你一个产品数组 `products` 和一个字符串 `searchWord` ，`products`  数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 `searchWord` 的每一个字母后，推荐 `products` 数组中前缀与 `searchWord` 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 `searchWord` 每个字母后相应的推荐产品的列表。

### 示例1:

```
输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]
```

### 示例2:
```
输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```

### 示例3:

```
输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
```

### 示例4:
```
输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]
```

### 约束条件：
- `1 <= products.length <= 1000`
- `1 <= Σ products[i].length <= 2 * 10^4`
- `products[i] 中所有的字符都是小写英文字母。`
- `1 <= searchWord.length <= 1000`
- `searchWord 中所有字符都是小写英文字母。`

### 解题思路：



```python

```
