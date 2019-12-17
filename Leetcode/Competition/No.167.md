# No. 167 Weekly Competition

- [Solved] stands for that the problems are solved in the competition。
- [Unsolved] stands for that I failed to solve them in the competition。

## [Solved] 1290. Convert Binary Number in a Linked List to Integer

### Description：

Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the `decimal` value of the number in the linked list.

### Example 1:
![](https://assets.leetcode.com/uploads/2019/12/05/graph-1.png)
```
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
```

### Example 2:
```
Input: head = [0]
Output: 0
```

### Example 3:
```
Input: head = [1]
Output: 1
```

### Example 4:
```
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
```

### Example 5:
```
Input: head = [0,0]
Output: 0
```

### Constraints:
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.


### Idea：
We can use the bit operation to solve this question.


```python
'''
Time: O(n), n is the length of the linked list
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans << 1
            ans ^= head.val
            head = head.next
        
        return ans
```

## [Solved] 1291. Sequential Digits


### Description:

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range [`low`, `high`] inclusive that have sequential digits.

### Example 1:

```
Input: low = 100, high = 300
Output: [123,234]
```

### Example 2:
```
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
```

### Constraints:
- `10 <= low <= high <= 10^9`


### Idea:
It is a trick because the range of `low` and `high` are not
too large. I store all the valid sequential digits in a list and then append 
it into the answer if it is in the [`low`, `high`].



```python
# Time Complexity : O(33)
# Space Complexity : O(33)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        all_ = [
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789, 
            1234, 2345, 3456, 4567, 5678, 6789, 
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789,
        ]
        ans = []
        for num in all_:
            if low <= num <= high:
                ans.append(num)
            if num > high:
                break
        
        return ans
```

## [Unsolved] 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

### Description:

Given a `m x n` matrix `mat` and an integer `threshold`. Return the maximum side-length of a square with a sum less than or equal to `threshold` or return 0 if there is no such square.

### Example 1:
![](https://assets.leetcode.com/uploads/2019/12/05/e1.png)
```
Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
```

### Example 2:
```
Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
```

### Example 3:
```
Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
```

### Example 4:
```
Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
```

### Constraints:
- `1 <= m, n <= 300`
- `m == mat.length`
- `n == mat[i].length`
- `0 <= mat[i][j] <= 10000`
- `0 <= threshold <= 10^5`

### Idea:
This question we use the prefix sum algorithm to reduce the time of querying 
the sum of the sub-matrix.

The sum of the sub-matrix with (i,j) as the bottom right vertex can be 
calculated as follow:

`sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + matrix[i][j]`

Thus, if we want to query the sum of the sub-matrix with (i,j) as the bottom 
right vertex and (m, n) as the top left vertex, we can calculate it in O(1).

`tmp = sum[i][j]-sum[m][j]-sum[i][n]+sum[m][n]`

Besides, we leverage the **binary search** to speed the process of searching 
the maximum side-length.


```python
# Time Complexity : T(m*n+log(min(m,n))*m*n)
# Space Complexity : O(mn)
class Solution:
    def maxSideLength(self, mat, threshold: int) -> int:
        '''
        Adopt the prefix sum algorithm
        '''
        m, n = len(mat), len(mat[0])
        _sum = [[0]* (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                _sum[i][j] = _sum[i-1][j] + _sum[i][j-1] - _sum[i-1][j-1] + mat[i-1][j-1]

        # exceeded the time limitation
        # use the binary search
        ans = 0
        l = 1
        r = min(m,n) + 1
        while l <= r:
            mid = (l+r) >> 1
            if self.helper(mid, m, n, _sum, threshold):
                l = mid + 1
                ans = max(ans, mid)
            else:
                r = mid - 1
        
        return ans

    def helper(self, k, m, n, _sum, threshold):
        # for k in range(1, min(m,n)+1):
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i-k < 0 or j-k < 0:
                    continue
                tmp = _sum[i][j] - _sum[i-k][j] - _sum[i][j-k] + _sum[i-k][j-k]
                if tmp <= threshold:
                    return True
        
        return False
```

## [Unsolved] 1293. Shortest Path in a Grid with Obstacles Elimination

### Description:

Given a `m * n` grid, where each cell is either `0` (empty) or `1` (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner `(0, 0)` to the lower right corner `(m-1, n-1)` given that you can eliminate **at most** `k` obstacles. If it is not possible to find such walk return `-1`.


### Example 1:

```
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position **(3,2)** is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> **(3,2)** -> (4,2).
```

### Example 2:
```
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
```

### Constraints:
- `grid.length == m`
- `grid[0].length == n`
- `1 <= m, n <= 40`
- `1 <= k <= m*n`
- `grid[i][j] == 0 or 1`
- `grid[0][0] == grid[m-1][n-1] == 0`

### Idea:
Use the breadth first search algorithm to search all the possible path.
The key point is to store the 3-D states (i, j, k) in the `visited` set and
the `state` which first reaches the target has the shortest path.

```python
# Time complexity : O(nmk)
# Space complexity : O(nmk)
from collections import deque
class Solution:
    def shortestPath(self, grid, k: int) -> int:
        m, n = len(grid), len(grid[0])
        step = 0 
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        visited = set()
        q.append((0, 0, k))
        visited.add((0, 0, k))

        # Breadth First Search
        while(q):
            size = len(q)
            for _ in range(size):
                i, j, k = q.popleft()
                # visited.add((i,j,k))
                if i == m-1 and j == n-1:
                    return step
                
                for di, dj in direct:
                    ni, nj = i+di, j+dj
                    if ni < 0 or nj < 0 or ni > m-1 or nj > n-1 or (grid[ni][nj]==1 and k<=0):
                        continue
                    
                    if grid[ni][nj] == 1 and (ni,nj,k-1) not in visited:
                        q.append((ni, nj, k-1))
                        visited.add((ni, nj, k-1))
                    elif grid[ni][nj] == 0 and (ni,nj,k) not in visited:
                        q.append((ni, nj, k))
                        visited.add((ni, nj, k))
            step += 1
        
        return -1
```