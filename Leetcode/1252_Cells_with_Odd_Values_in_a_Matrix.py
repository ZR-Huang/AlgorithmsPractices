class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = {} 
        columns = {}
        # for (i, j) in 