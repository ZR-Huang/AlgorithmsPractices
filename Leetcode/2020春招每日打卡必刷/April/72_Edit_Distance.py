'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.search(word1, word2, memo)

    def search(self, word1: str, word2: str, memo: dict) -> int:
        # https://leetcode-cn.com/problems/edit-distance/solution/dong-tai-gui-hua-de-ben-zhi-shi-di-gui-ha-xi-_-by-/
        state = word1 + "," + word2
        if state in memo:
            return memo[state]
        if word1 == word2:
            memo[state] = 0
            return memo[state]
        if not word1 or not word2:
            memo[state] = max(len(word1), len(word2))
            return memo[state]

        if word1[0] == word2[0]:
            d = self.search(word1[1:], word2[1:], memo) # no edit 
        else:
            d = min([
                self.search(word1[1:], word2[:], memo), # delete
                self.search(word1[1:], word2[1:], memo), # replace
                self.search(word1[:], word2[1:], memo), # insert
            ])+1
        
        memo[state] = d
        return memo[state]
    
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j], dp[i-1][j-1], dp[i][j-1]]) + 1
        return dp[-1][-1]

print(Solution().minDistance('horse', 'ros'))