import time
class Solution():
    def table(self, arrLen, steps):
        # Time exceeded : 33.4s
        # create table
        result_table = [[0 for _ in range(arrLen)] for _ in range(steps+1)] 
        result_table[0][0] = 1
        MOD = 10**9 + 7
        
        for i in range(1, steps+1):
            for j in range(arrLen):
                if j-1 < 0 and j+1 < arrLen:
                    result_table[i][j] = result_table[i-1][j] + result_table[i-1][j+1]
                elif j-1 >= 0 and j+1 >= arrLen:
                    result_table[i][j] = result_table[i-1][j-1] + result_table[i-1][j]
                elif j-1 < 0 and j+1 >= arrLen:
                    result_table[i][j] = result_table[i-1][j] 
                else:
                    result_table[i][j] = result_table[i-1][j-1] + result_table[i-1][j] + \
                        result_table[i-1][j+1]

        return result_table[-1][0] % MOD


    def table_v2(self, arrLen, steps):
        # create table
        # Time : 0.085m
        j_max = min(steps, arrLen)
        result_table = [[0 for _ in range(j_max)] for _ in range(steps+1)] 
        result_table[0][0] = 1
        MOD = 10**9 + 7
        
        for i in range(1, steps+1):
            result_table[i][0] = (result_table[i-1][0] + result_table[i-1][1]) % MOD
            for j in range(1, j_max-1):
                result_table[i][j] = (result_table[i-1][j-1] + result_table[i-1][j] + \
                    result_table[i-1][j+1]) % MOD
            result_table[i][j_max-1] = (result_table[i-1][j_max-2] + result_table[i-1][j_max-1]) % MOD
                
        return result_table[-1][0]

    
    def table_v3(self, arrLen, steps):
        j_max = min(steps, arrLen)
        result_table = [[0] * min(j_max, steps-i+1) for i in range(steps+1)]
        result_table[0][0] = 1
        MOD = 10**9 + 7
        
        for i in range(1, steps+1):
            result_table[i][0] = (result_table[i-1][0] + result_table[i-1][1]) % MOD
            for j in range(1, len(result_table[i])-1):
                result_table[i][j] = (result_table[i-1][j-1] + result_table[i-1][j] + \
                    result_table[i-1][j+1]) % MOD
            result_table[i][-1] = (result_table[i-1][-2] + result_table[i-1][-1]) % MOD
                
        return result_table[-1][0]


# arrLen = 7
# steps = 27
# arrLen = 4
# steps = 2
arrLen = 148488
steps = 430
# arrLen = 2
# steps = 3
s = time.time()
print(Solution().table_v3(arrLen, steps))
print(time.time()-s)