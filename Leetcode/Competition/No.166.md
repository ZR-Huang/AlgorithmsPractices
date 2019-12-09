# 第166场周赛

> Rank: 350/1675。

- [Solved] stands for that the problems are solved in the competition。
- [Unsolved] stands for that I failed to solve them in the competition。

## [Solved] 1281. Subtract the Product and Sum of Digits of an Integer

### Description：

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

### Example 1:

```
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
```

### Example 2:
```
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
```

### Constraints:
- `1 <= n <= 10^5`



### Idea：
The straight idea is that compute the product and sum of the integer respectively and then 
get the answer.


```python
# Time complexity : O(N), N is the number of the digits
# Space complexity : O(N)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        prod = 1
        while n != 0 :
            tmp = n%10
            digits.append(tmp)
            prod *= tmp
            n = n // 10
        
        return prod - sum(digits)

'''
The space can be optimized to O(1). The product and the sum can be computed in each 
loop without the list.
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # digits = []
        prod = 1
        _sum = 0
        while n != 0 :
            tmp = n%10
            # digits.append(tmp)
            _sum += tmp
            prod *= tmp
            n = n // 10
        
        return prod - _sum
```

## [Solved] 1282. Group the People Given the Group Size They Belong To


### Description:

There are n people whose **IDs** go from 0 to n - 1 and each person belongs **exactly** to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's **IDs** each group includes.

You can return any solution in any order and the same applies for **IDs**. Also, it is guaranteed that there exists at least one solution. 

### Example 1:

```
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
```

### Example 2:
```
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
```

### Constraints:
- `groupSizes.length == n`
- `1 <= n <= 500`
- `1 <= groupSizes[i] <= n`


### Idea:
Here is a simple rule which can be easily found, when we try to 
figure out the calculation process of the example 1. We allocate the **groupSize** space to store the **IDs**, if there is no corresponding group, and put the ID in it when iterate the array. If any group is filled up, we append it into the result and then allocate a new group. Thus, it is the **greedy** algorithm.


```python
# Time Complexity : O(N)
# Space Complexity : O(N)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        d = {}
        for ID, group_size in enumerate(groupSizes):
            if not group_size in d:
                d[group_size] = [ID]
            else:
                if len(d[group_size]) == group_size:
                    result.append(d.pop(group_size))
                    d[group_size] = [ID]
                else:
                    d[group_size] += [ID]

        
        for key in d.keys():
            result.append(d[key])
        
        return result
```

## [Solved] 1283. Find the Smallest Divisor Given a Threshold

### Description:

Given an array of integers **nums** and an integer **threshold**, we will choose a **positive integer** divisor and divide all the array by it and sum the result of the division. Find the **smallest** divisor such that the result mentioned above is less than or equal to **threshold**.

Each result of division is rounded to **the nearest integer greater than or equal to that element**. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

### Example 1:

```
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
```

### Example 2:
```
Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
```

### Example 3:
```
Input: nums = [19], threshold = 5
Output: 4
```

### Constraints:
- `1 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^6`
- `nums.length <= threshold <= 10^6`

### Idea:
At the beginning, I try to iterate the divisor from 1 to the max(nums). The time complexity of this algorithm is O(N**2) and the program exceeded the time limitation.

Then, I try to use the **binary search** algorithm and actually it is a easy way to pass all the test cases.


```python
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_muminum = max(nums)
        result = max_muminum

        l, r = 1, max_muminum
        while l <= r:
            mid = (l+r) >> 1
            _sum = [ceil(num / mid) for num in nums]
            if sum(_sum) <= threshold:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return result
```

## [Unsolved] 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

### Description:

Given a `m x n` binary matrix `mat`. In one step, you can choose one cell and flip it and all the four neighbours of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.

Return the minimum number of steps required to convert `mat` to a zero matrix or **-1** if you cannot.

Binary matrix is a matrix with all cells equal to 0 or 1 only.

Zero matrix is a matrix with all cells equal to 0.

### Example 1:
![](https://assets.leetcode.com/uploads/2019/11/28/matrix.png)

```
Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
```

### Example 2:
```
Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We don't need to change it.
```

### Example 3:
```
Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
Output: 6
```

### Example 4:
```
Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix can't be a zero matrix
```

### Constraints:
- `m == mat.length`
- `n == mat[0].length`
- `1 <= m <= 3`
- `1 <= n <= 3`
- `mat[i][j] is 0 or 1`

### Idea:
> We store the states which are visited in a hashmap, and use the breadth first searching algorithm to enumerate all the flipping states. If the states are not visited before, we append them into the queue.
> ——"[bfs 枚举，并记录矩阵状态](https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/solution/bfs-mei-ju-by-tfboy96/)"

```python
# Time complexity : O(2**(nm))
# Space complexity : O(2**(nm))
from collections import deque
from copy import deepcopy

class Solution:
    def minFlips(self, mat):
        m = len(mat)
        n = len(mat[0])
        visited = set()
        
        # bfs
        q = deque()
        q.append(mat)
        visited.add(str(mat))
        target = [[0]*n for _ in range(m)]

        result = 0
        while q:
            for _ in range(len(q)):
                current_state = q.popleft()
                if current_state == target:
                    return result
                
                for i in range(m):
                    for j in range(n):
                        current_copy = deepcopy(current_state)
                        current_copy[i][j] = 1-current_copy[i][j]

                        if 0 <= i-1 <= m-1 and 0<= j <= n-1:
                            current_copy[i-1][j] = 1-current_copy[i-1][j]
                        if 0 <= i+1 <= m-1 and 0<= j <= n-1:
                            current_copy[i+1][j] = 1-current_copy[i+1][j]
                        if 0 <= i <= m-1 and 0 <= j+1 <= n-1:
                            current_copy[i][j+1] = 1- current_copy[i][j+1]
                        if 0 <= i <= m-1 and 0 <= j-1 <= n-1:
                            current_copy[i][j-1] = 1-current_copy[i][j-1]

                        _str = str(current_copy)
                        if _str not in visited:
                            visited.add(_str)
                            q.append(current_copy)
            result += 1
        return -1
```