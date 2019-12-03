# 第165场周赛

> 全国排名为786/1659。在比赛中只解出了第一题。

- [Solved] 表示在比赛中解出。
- [Unsolved] 表示在比赛中未能解出。

## [Solved] 1275.访问所有点的最小时间

### 题目描述：

A 和 B 在一个 3 x 3 的网格上玩井字棋。

井字棋游戏的规则如下：

- 玩家轮流将棋子放在空方格 (" ") 上。
- 第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
- "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
- 只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
- 如果所有方块都放满棋子（不为空），游戏也会结束。
- 游戏结束后，棋子无法再进行任何移动。
给你一个数组 `moves`，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。

如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

你可以假设 `moves` 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。

### 示例1:

```
输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
输出："A"
解释："A" 获胜，他总是先走。
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
```

### 示例2:
```
输入：moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
输出："B"
解释："B" 获胜。
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
```

### 示例3:
```
输入：moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
输出："Draw"
输出：由于没有办法再行动，游戏以平局结束。
"XXO"
"OOX"
"XOX"
```

### 示例4:
```
输入：moves = [[0,0],[1,1]]
输出："Pending"
解释：游戏还没有结束。
"X  "
" O "
"   "
```

### 约束条件：
- `1 <= moves.length <= 9`
- `moves[i].length == 2`
- `0 <= moves[i][j] <= 2`
- `moves` 里没有重复的元素。
- `moves` 遵循井字棋的规则。



### 解题思路：
这个题目的难点在于怎么对四种结果进行判断。因为A胜和B胜两种结果对判断方法相同，所以从以下三种情况来说明。
- A（或B）胜：在行，列或对角线上三个棋子连成直线则获胜。由于棋盘固定为3 x 3，因此可以借助两个长度为3的数组`row, col`来统计A的棋子在每行每列的个数。若`row[i]==3`或`col[j]==3`，则A胜。同理，对于对角线棋子的判断，可以利用固定规则判断，即在A所下的棋子中，是否同时存在`[0,0],[1,1],[2,2]`（或`[0,2],[1,1],[2,0]`）。
- 当A和B均没有获胜，且`len(moves)==9`则结果为"Draw"。
- 排除以上三种情况，则游戏未结束，"Pending"。


```python
# Time complexity : O(N**2+N+3)*2 = O(N**2)
# Space complexity : O(2N+N**2/2) = O(N**2)
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def is_win(moves, player_start):
            row = [0,0,0]
            col = [0,0,0]
            x_move = {}
            for i in range(player_start, len(moves), 2):
                x_move[tuple(moves[i])] = 1
            
            for move in x_move.keys():
                row[move[0]] += 1
                col[move[1]] += 1
            
            for n, m in zip(row, col):
                if n ==3 or m == 3:
                    return True
            
            if (0, 0) in x_move and (1,1) in x_move and (2,2) in x_move:
                return True
            elif (0,2) in x_move and (1,1) in x_move and (2,0) in x_move:
                return True
            else:
                return False

        A_result = is_win(moves, 0)
        B_result = is_win(moves, 1)
        if A_result:
            return "A"
        elif B_result:
            return "B"
        elif not A_result and not B_result and len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
```

## [Unsolved] 1276. 不浪费原料的汉堡制作方案


### 题目描述：

圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。

给你两个整数 `tomatoSlices` 和 `cheeseSlices`，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：

巨无霸汉堡：4 片番茄和 1 片奶酪
小皇堡：2 片番茄和 1 片奶酪
请你以 `[total_jumbo, total_small]`（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片 `tomatoSlices` 和奶酪片 `cheeseSlices` 的数量都是 0。

如果无法使剩下的番茄片 `tomatoSlices` 和奶酪片 `cheeseSlices` 的数量为 0，就请返回 []。


### 示例1:

```
输入：tomatoSlices = 16, cheeseSlices = 7
输出：[1,6]
解释：制作 1 个巨无霸汉堡和 6 个小皇堡需要 4*1 + 2*6 = 16 片番茄和 1 + 6 = 7 片奶酪。不会剩下原料。
```

### 示例2:
```
输入：tomatoSlices = 17, cheeseSlices = 4
输出：[]
解释：只制作小皇堡和巨无霸汉堡无法用光全部原料。
```

### 示例3:

```
输入：tomatoSlices = 4, cheeseSlices = 17
输出：[]
解释：制作 1 个巨无霸汉堡会剩下 16 片奶酪，制作 2 个小皇堡会剩下 15 片奶酪。
```

### 示例4:
```
输入：tomatoSlices = 0, cheeseSlices = 0
输出：[0,0]
```

### 示例5:
```
输入：tomatoSlices = 2, cheeseSlices = 1
输出：[0,1]
```

### 约束条件：
- `0 <= tomatoSlices <= 10^7`
- `0 <= cheeseSlices <= 10^7`


### 解题思路：
当时看到这道题的第一反应是线性规划，但是想到线性规划不好求解。就是着用动态规划，结果在表格上纠结了半天也没写出合适的状态转移方程。看到题解是直接求解二元一次方程的时候我就傻了，还是练的不够多。

设巨无霸有x个，皇堡有y个。可以得到下面的二元一次方程组：

`4x + 2y = tomatoSlices`

`x + y = cheeseSlices`

解得：

`x = 0.5 * tomatoSlices - cheeseSlices`

`y = 2 * cheeseSlices - 0.5 * tomatoSlices`

根据题意，`x, y > 0 and x, y为整数`，有以下约束条件：

- `tomatoSlices` 为偶数
- `tomatoSlices >= 2 * cheeseSlices`
- `4 * cheeseSlices >= tomatoSlices`

不满足则无解。


```python
# Time Complexity : O(1)
# Space Complexity : O(1)
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices & 1 != 0 or tomatoSlices < 2*cheeseSlices or 4*cheeseSlices < tomatoSlices:
            return []
        else:
            return [tomatoSlices // 2 - cheeseSlices, 2*cheeseSlices - tomatoSlices//2]
```

## [Unsolved] 1277.统计全为1的正方形子矩阵


### 题目描述：

给你一个 `m * n` 的矩阵，矩阵中的元素不是 `0` 就是 `1`，请你统计并返回其中完全由 `1` 组成的 `正方形`子矩阵的个数。

### 示例1:

```
输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释： 
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.
```

### 示例2:
```
输入：matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。 
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.
```

### 约束条件：
- `1 <= arr.length <= 300`
- `1 <= arr[0].length <= 300`
- `0 <= arr[i][j] <= 1`

### 解题思路：
参考[官方解答](https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-b/)，该题目与[221.最大正方形](https://leetcode-cn.com/problems/maximal-square/)相似，解题方法也类似。


```python
class Solution:
    def countSquares(self, matrix):
        cols = len(matrix[0])
        rows = len(matrix)
        dp = [[0] * cols for _ in range(rows)]
        result = 0
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
                result += dp[i][j]
        return result
```

## [Unsolved] 1278.分割回文串 III

### 题目描述：
给你一个由小写字母组成的字符串 `s`，和一个整数 `k`。

请你按下面的要求分割字符串：

- 首先，你可以将 `s` 中的部分字符修改为其他的小写英文字母。
- 接着，你需要把 `s` 分割成 `k` 个非空且不相交的子串，并且每个子串都是回文串。

请返回以这种方式分割字符串所需修改的最少字符数。


### 示例1:

```
输入：s = "abc", k = 2
输出：1
解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
```

### 示例2:

```
输入：s = "aabbc", k = 3
输出：0
解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。
```

### 示例3:

```
输入：s = "leetcode", k = 8
输出：0
```

### 约束条件：
- `1 <= k <= s.length <= 100`
- `s` 中只含有小写英文字母。

### 解题思路：
参考[官方题解](https://leetcode-cn.com/problems/palindrome-partitioning-iii/solution/fen-ge-hui-wen-chuan-iii-by-leetcode/)。在考虑字符串的动态规划问题时（特别时分割和拼接的问题），注意是否需要对字符串进行重复的枚举。

```python
def palindromePartition(self, s, k):
        def cost(l, r):
            changes = 0
            while l < r:
                changes += (0 if s[l-1]==s[r-1] else 1)
                l += 1
                r -= 1
            return changes

        n = len(s)
        dp = [[10**8] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, min(i, k)+1):
                if j == 1:
                    dp[i][j] = cost(1, i)
                else:
                    for i0 in range(j-1, i):
                        dp[i][j] = min(dp[i][j], dp[i0][j-1]+cost(i0+1, i))

        return dp[n][k]
```
