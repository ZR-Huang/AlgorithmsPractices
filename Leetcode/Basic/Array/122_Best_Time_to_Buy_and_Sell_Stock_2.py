class Solution:
    def maxProfit(self, prices) -> int:
        '''
        Notice that we can complete as many transactions as we like.
        Therefore, a greedy rule are easily came out, that we buy it 
        on the low price day which compares with the next day and 
        sell it on the high price day which compares with next day.
        '''
        last_buy_day=0
        is_buy = False
        profit = 0

        for i in range(len(prices)):
            if i == len(prices)-1:
                if is_buy:
                    profit += prices[i] - prices[last_buy_day]
                
            elif prices[i] < prices[i+1] and not is_buy:
                last_buy_day = i
                is_buy = True
            elif prices[i] > prices[i+1] and is_buy:
                profit += prices[i] - prices[last_buy_day]
                is_buy = False

        return profit

print(Solution().maxProfit([1,2,3,4,5]))
            
