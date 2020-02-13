'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directs = [(-1,0), (1,0), (0,-1), (0,1)]
        def dfs(word, m, n, i, j, marked):
            nonlocal board, directs
            if not word:
                return True
            
            if board[i][j] == word[0]:
                marked[i][j] = True
                for dx, dy in directs:
                    if (0<=i+dx<m) and (0<=j+dy<n) and (not marked[i+dx][j+dy]) \
                            and dfs(word[1:], m, n, i+dx, j+dy, marked):
                        return True
                marked[i][j] = False
            return False
        
        m, n = len(board), len(board[0])
        marked = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(word, m, n, i, j, marked):
                    return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        visted = set()

        def dfs(i, j, cur):
            if (i, j) in visted:
                return False
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[cur]:
                return False
            if cur == len(word) - 1:
                return True
            visted.add((i, j))
            res = dfs(i + 1, j, cur + 1) \
                or dfs(i - 1, j, cur + 1) \
                or dfs(i, j + 1, cur + 1) \
                or dfs(i, j - 1, cur + 1)
            visted.remove((i, j))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

print(Solution().exist([["a","a"]], "aaa"))