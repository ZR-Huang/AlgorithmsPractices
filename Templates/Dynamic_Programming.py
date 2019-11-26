'''
This is the implementation of Section 5.11 in <漫画算法>
'''

class Solution():
    def recursion(self, w, n, p, g):
        '''
        w : 工人数量
        n : 可选金矿数量
        p : 金矿开采所需的工人数量
        g : 金矿储量

        time cost : O(2**n)
        '''
        if w == 0 or n == 0:
            return 0
        if w < p[n-1]:
            return self.recursion(w, n-1, p, g)
        
        return max(self.recursion(w, n-1, p, g), self.recursion(w-p[n-1], n-1, p, g)+g[n-1])


    def table(self, w, p, g):
        # create table
        result_table = [[0 for _ in range(w+1)] for _ in range(len(g)+1)] 

        for i in range(1, len(g)+1):
            for j in range(1, w+1):
                if j<p[i-1]:
                    result_table[i][j] = result_table[i-1][j]
                else:
                    result_table[i][j] = max(result_table[i-1][j], result_table[i-1][j-p[i-1]] + g[i-1])
        
        return result_table[-1][-1]

    
    def array(self, w, p, g):
        results = [0 for _ in range(w+1)]
        for i in range(1, len(g)+1):
            for j in range(w, 0, -1):
                if j >= p[i-1]:
                    results[j] = max(results[j], results[j-p[i-1]]+g[i-1])
        
        return results[-1]

p = [5,5,3,4,3]
g = [400,500,200,300,350]
w = 10
print(Solution().recursion(w, len(g), p, g))
print(Solution().table(w, p, g))
print(Solution().array(w, p, g))