class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>mini:
                profit+=prices[i]-mini
                mini=prices[i]
                continue
            mini=min(mini,prices[i])
        return profit