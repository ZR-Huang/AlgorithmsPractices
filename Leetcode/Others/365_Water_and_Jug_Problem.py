'''
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. 
You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within 
one or both buckets by the end.

Operations allowed:
- Fill any of the jugs completely with water.
- Empty any of the jugs.
- Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)
Input: x = 3, y = 5, z = 4
Output: True

Example 2:
Input: x = 2, y = 6, z = 5
Output: False
'''
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return self.dfs(0, x, 0, y, z, set())

    def dfs(self, curr_x, x, curr_y, y, z, visited):
        visited.add((curr_x, curr_y))
        if curr_x == z or curr_y == z or curr_x+curr_y==z:
            return True
        if curr_x != x and (x, curr_y) not in visited and self.dfs(x, x, curr_y, y, z, visited):
            return True
        if curr_y != y and (curr_x, y) not in visited and self.dfs(curr_x, x, y, y, z, visited):
            return True
        if curr_x != 0 and (0, curr_y) not in visited and self.dfs(0, x, curr_y, y, z, visited):
            return True
        if curr_y != 0 and (curr_x, 0) not in visited and self.dfs(curr_x, x, 0, y, z, visited):
            return True
        if curr_x != 0:
            if curr_x+curr_y <= y and (0, curr_x+curr_y) not in visited and self.dfs(0, x, curr_x+curr_y, y, z, visited):
                return True
            elif curr_x+curr_y > y and (curr_x-(y-curr_y), y) not in visited and self.dfs(curr_x-(y-curr_y), x, y, y, z, visited):
                return True
        if curr_y != 0:
            if curr_x+curr_y <= x and (curr_x+curr_y, 0) not in visited and self.dfs(curr_x+curr_y, x, 0, y, z, visited):
                return True
            elif curr_x+curr_y > x and (x, curr_y-(x-curr_x)) not in visited and self.dfs(x, x, curr_y-(x-curr_x), y, z, visited):
                return True
        return False

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 需要搜索的解空间太大，超出默认的递归层数
        # 该用栈模拟
        stack = [(0, 0)]
        visited = set()
        while stack:
            curr_x, curr_y = stack.pop()
            if curr_x == z or curr_y == z or curr_x+curr_y == z:
                return True
            if (curr_x, curr_y) in visited:
                continue
            visited.add((curr_x, curr_y))
            stack.append((x, curr_y)) # 把x壶装满
            stack.append((curr_x, y)) # 把y壶装满
            stack.append((0, curr_y)) # empty x
            stack.append((curr_x, 0)) # empty y
            stack.append((curr_x - min(curr_x, y-curr_y), curr_y+min(curr_x, y-curr_y))) # 往y壶倒水
            stack.append((curr_x + min(curr_y, x-curr_x), curr_y-min(curr_y, x-curr_x))) # 往x壶倒水
        return False

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # analysis: https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % self.gcd(x, y) == 0

    def gcd(self, x, y):
        small = min(x, y)
        large= max(x, y)
        while small:
            tmp = large % small
            large, small = small, tmp
        return large

print(Solution().canMeasureWater(22003,31237,1))
print(Solution().canMeasureWater(0,0,0))
print(Solution().canMeasureWater(1,2,3))
print(Solution().canMeasureWater(34,5,6))
