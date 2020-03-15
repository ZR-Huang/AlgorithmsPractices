from typing import List
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        def search(curr,n,speed, efficiency, k, select_spd, select_eff):
            if k == 0 or (k>0 and curr==n-1):
                sum_spd = sum(select_spd)
                min_eff = min(select_eff)
                perf = sum_spd * min_eff
                return perf %(10**9+7)
            for i in range(curr+1, n):
                select_res = search(i, n, speed, efficiency, k-1, select_spd + [speed[i]], select_eff + [efficiency[i]])
                unselect_res = search(i, n, speed, efficiency, k, select_spd, select_eff)
                unselect_res = 0 if not unselect_res else unselect_res
                return max([select_res, unselect_res])

        select_spd = [0]
        select_eff = [10**8]
        for i in range(n):
            select_res = search(i, n, speed, efficiency, k-1, select_spd + [speed[i]], select_eff + [efficiency[i]])
            unselect_res = search(i, n, speed, efficiency, k, select_spd, select_eff)
            return max([select_res, unselect_res])

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        import heapq
        d=[]
        for spd, eff in zip(speed, efficiency):
            d.append((eff, spd))
        d = sorted(d, reverse=True)
        heap = []
        heapq.heapify(heap)
        sum_spd = 0
        res = 0
        for eff, spd in d:
            heapq.heappush(heap, spd)
            sum_spd += spd
            if len(heap) > k:
                sum_spd -= heapq.heappop(heap)
            res = max([res, sum_spd * eff])
        return res % (10**9+7)

                
# print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))
# print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))
# print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4))
print(Solution().maxPerformance(7, [1,4,1,9,4,4,4],[8,2,1,7,1,8,4], 6))