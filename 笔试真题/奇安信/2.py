class Solution:
    def dfs(self, n, mem):
        if n in mem:
            return mem[n]
        res = 0
        for i in range(1, n+1):
            res += self.dfs(n-i, mem)
        mem[n] = res
        return mem[n]
    def CalulateMethodCount(self , num_money ):
        # write code here
        mem = {}
        mem[0], mem[1] = 1, 1
        self.dfs(num_money, mem)
        return mem[num_money]

if __name__ == '__main__':
    print(Solution().CalulateMethodCount(10000))