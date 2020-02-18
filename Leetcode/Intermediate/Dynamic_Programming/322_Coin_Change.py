'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
'''
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        ans = 10**10
        for coin in coins:
            if amount - coin < 0:
                continue
            subpro = self.coinChange(coins, amount-coin)
            if subpro == -1:
                continue
            else:
                ans = min(ans, subpro+1)
        return ans if ans != 10**10 else -1

    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        # use hashmap
        dp = {}
        def helper(coins, amount, dp):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            ans = 10**10
            for coin in coins:
                if amount - coin < 0:
                    continue
                subpro = helper(coins, amount-coin, dp)
                if subpro == -1:
                    continue
                else:
                    ans = min(ans, subpro+1)
            dp[amount] = ans if ans != 10**10 else -1
            return dp[amount]
        return helper(coins, amount, dp)
            

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange_v2([186,419,83,408],6249))
