'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):
    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board 
given its current state. The next state is created by applying the above rules 
simultaneously to every cell in the current state, where births and deaths 
occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
- Could you solve it in-place? Remember that the board needs to be updated at the same time: 
    You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, 
    which would cause problems when the active area encroaches the border of the array. 
    How would you address these problems?
'''

from typing import List
from copy import deepcopy, copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        old_board = deepcopy(board)
        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                num_live_neighbors = 0
                for di, dj in neighbors:
                    if 0<=i+di<m and 0<=j+dj<n:
                        num_live_neighbors = num_live_neighbors + 1 if old_board[i+di][j+dj] else num_live_neighbors
                if old_board[i][j] and num_live_neighbors < 2:
                    board[i][j] = 0
                elif old_board[i][j] and num_live_neighbors > 3:
                    board[i][j] = 0
                elif (not old_board[i][j]) and num_live_neighbors == 3:
                    board[i][j] = 1

    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                num_live_neighbors = 0
                for di, dj in neighbors:
                    if 0<=i+di<m and 0<=j+dj<n:
                        num_live_neighbors = num_live_neighbors + 1 if abs(board[i+di][j+dj])==1 else num_live_neighbors
                if board[i][j] and num_live_neighbors < 2:
                    board[i][j] = -1
                elif board[i][j] and num_live_neighbors > 3:
                    board[i][j] = -1
                elif (not board[i][j]) and num_live_neighbors == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)