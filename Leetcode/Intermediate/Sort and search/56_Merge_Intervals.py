'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda interval: interval[0], reverse=True)
        ans = []
        last = intervals.pop()
        while intervals:
            curr = intervals.pop()
            if curr[0] > last[1]:
                ans.append(last)
                last = curr
            else:
                last = [last[0], max(curr[1],last[1])]
        ans.append(last)
        return ans


print(Solution().merge([[1,4],[1,5]]))
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,3],[2,4],[3,5],[4,6]]))