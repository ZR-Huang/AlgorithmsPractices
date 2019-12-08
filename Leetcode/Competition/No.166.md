# 第166场周赛

> 全国排名为350/1675。

- [Solved] 表示在比赛中解出。
- [Unsolved] 表示在比赛中未能解出。

## [Solved] 5279. Subtract the Product and Sum of Digits of an Integer

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

## [Solved] 5280. Group the People Given the Group Size They Belong To


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

## [Solved] 5281. Find the Smallest Divisor Given a Threshold

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


