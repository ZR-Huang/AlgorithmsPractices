class Solution:
    def isValidSudoku(self, board):
        '''
        the simplest way to iterate the matrix, according to the 
        rules.
        Time cost: 160ms
        '''
        for row in board:
            d = {}
            for elem in row:
                if elem in d and elem != '.':
                    return False
                else:
                    d[elem] = 1
        
        for j in range(0, 9):
            d = {}
            for i in range(0, 9):
                if board[i][j] in d and board[i][j] != '.':
                    return False
                else:
                    d[board[i][j]] = 1
        
        for block_No in range(9):
            d = {}
            # compute the start index of column
            if block_No / 3 < 1:
                    start = 0
            elif block_No / 3 < 2:
                start = 3
            else:
                start = 6
            for i in range(block_No%3*3, block_No%3*3+3):
                for j in range(start, start+3):
                    if board[i][j] in d and board[i][j] != '.':
                        return False
                    else:
                        d[board[i][j]] = 1

        return True

    def isValidSudoku_v2(self, board):
        '''
        Official algorithm, one time iteration
        Time cost: 120ms
        '''
        # init data
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                box_No = (i // 3)*3 + j //3
                if board[i][j] in boxes[box_No] or board[i][j] in columns[j] or board[i][j] in rows[i]:
                    return False
                else:
                    boxes[box_No][board[i][j]], columns[j][board[i][j]], rows[i][board[i][j]] = 1,1,1
        
        return True

    def isValidSudoku_v3(self, board):
        '''
        Bit Operation
        https://leetcode-cn.com/problems/valid-sudoku/solution/java-wei-yun-suan-xiang-jie-miao-dong-zuo-biao-bia/
        Time cost: 164ms
        '''
            
        for i in range(9):
            # 10 bits variable to store the accessed values in 
            # rows, columns, and boxes respectively
            row, col, box = 0, 0, 0
            for j in range(9):
                r = int(board[i][j]) if board[i][j] != '.' else -1
                # the symmetric relationship between row and column
                c = int(board[j][i]) if board[j][i] != '.' else -1
                b = int(board[3*(i//3)+j//3][3*(i%3)+j%3]) if board[3*(i//3)+j//3][3*(i%3)+j%3] != '.' else -1
                if r>0:
                    row = self.validate(r, row)
                if c>0:
                    col = self.validate(c, col)
                if b>0:
                    box = self.validate(b, box)

                if row == -1 or col == -1 or box == -1:
                    return False
        
        return True

    def validate(self, n, val):
        return -1 if (val >> n) & 1 == 1 else val ^ (1 << n)
        


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku_v3(board))
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku_v3(board))