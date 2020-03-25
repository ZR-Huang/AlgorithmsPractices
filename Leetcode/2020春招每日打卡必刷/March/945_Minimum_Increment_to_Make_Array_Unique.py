'''
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
Return the least number of moves to make every value in A unique.

Example 1:
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Note:
0 <= A.length <= 40000
0 <= A[i] < 40000
'''
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # sort A
        A.sort()
        move = 0
        # increase the element from the start to the end
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                A[i] += 1
                move += 1
            elif A[i] < A[i-1]:
                move += (A[i-1] + 1 - A[i])
                A[i] = A[i-1] + 1
        return move
    

    def minIncrementForUnique(self, A: List[int]) -> int:
        # https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/ji-shu-onxian-xing-tan-ce-fa-onpai-xu-onlogn-yi-ya/
        def find_pos(a, pos):
            b = pos[a]
            if b == -1: # 如果该位置为空，则返回该位置
                pos[a] = a
                return a
            
            b = find_pos(b+1, pos) # 从b+1开始探测下一个空位置即可
            pos[a] = b # 寻址后的新空位要赋值给pos[a]，路径压缩
            return b
        
        pos = [-1] * 80000
        move = 0
        for num in A:
            b = find_pos(num, pos)
            move += b-num
        return move