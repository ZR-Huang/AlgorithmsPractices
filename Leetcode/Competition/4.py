from typing import List
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[0]*(n+1) for _ in range(n+1)]
        for from_, to_ in edges:
            graph[from_][to_], graph[to_][from_] = 1, 1
        
        visited = set()
        def dfs(graph, t, curr_vertex, target, visited):
            visited.add(curr_vertex)
            tmp = []
            for to, exist_edge in enumerate(graph[curr_vertex]):
                if (exist_edge) and (to not in visited) and (t > 0):
                    res = dfs(graph, t-1, to, target, visited)
                    tmp.append(res)
                    visited.remove(to)
            
            if curr_vertex == target and t == 0:
                return 1
            elif tmp:
                return max(tmp) * (1 / sum(graph[curr_vertex][curr_vertex:]))
            elif curr_vertex == target and t > 0:
                return 1
            else:
                return 0
        
        return dfs(graph, t, 1, target, visited)
        
print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7))
print(Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))
print(Solution().frogPosition(3, [[3,2],[2,1]], 1, 2))
print(Solution().frogPosition(8, [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]],7,7))