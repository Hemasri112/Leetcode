class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices [0]
        maxp=0
        for i in range (len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            profit =prices[i]-minp
            if profit>maxp:
                maxp=profit
        return maxp