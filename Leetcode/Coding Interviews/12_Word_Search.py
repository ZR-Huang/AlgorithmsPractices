'''
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/ (../Intermediate/Bachtracking/79)

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(board, word, visited, i, j): 
            visited.add((i,j))
            if len(word)==1 and board[i][j]==word[0]:
                return True
            if board[i][j]==word[0]:
                if 0<=i-1 and ((i-1,j) not in visited) and backtrack(board, word[1:], visited, i-1, j):
                    return True
                elif i+1<len(board) and ((i+1,j) not in visited) and backtrack(board, word[1:], visited, i+1,j):
                    return True
                elif 0<=j-1 and ((i, j-1) not in visited) and backtrack(board, word[1:], visited, i, j-1):
                    return True
                elif j+1<len(board[0]) and ((i,j+1) not in visited) and backtrack(board, word[1:], visited, i, j+1):
                    return True
            visited.remove((i,j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and backtrack(board, word, set(), i, j):
                    return True
        return False

print(Solution().exist([["a","b"],["c","d"]], "abcd"))