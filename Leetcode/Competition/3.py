from typing import List
from collections import deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = deque()
        q.append(headID)
        ans = 0
        while q:
            tmp = list()
            length = len(q)
            for _ in range(length):
                head_id = q.popleft()
                xiashu_ids = []
                for index, head in enumerate(manager):
                    if head== head_id:
                        xiashu_ids.append(index)
                        q.append(index)
                tmp.append(informTime[head_id])
            ans += max(tmp)

        return ans

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # naive dfs will exceed time limitation.
        def dfs(n, headID, manager_dict, informTime):
            if headID not in manager_dict:
                return informTime[headID]
            tmp = []
            for index in manager_dict[headID]:
                tmp.append(dfs(n, index, manager_dict, informTime))
            return max(tmp)+informTime[headID]
        
        manager_dict = {}
        for index, head in enumerate(manager):
            if head not in manager_dict:
                manager_dict[head] = [index]
            else:
                manager_dict[head].append(index)
        return dfs(n, headID, manager_dict, informTime)


print(Solution().numOfMinutes(11, 4, [5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337]))
print(Solution().numOfMinutes(1, 0, [-1], [0]))
print(Solution().numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
print(Solution().numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]))
print(Solution().numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(Solution().numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914]))

