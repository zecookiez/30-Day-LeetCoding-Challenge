class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # I was not sure if greedy was sufficient, so I employed a Dynamic Programming approach:
        
        high = -1e18
        best = 0
        for b in prices:
            high = max(high, best - b)
            best = max(best, high + b)
        return best
    
    # My initial O(N^2) submission
    
    def maxProfixQuadratic(prices):
        n = len(prices)
        dp = [0] * (n + 1)
        for b in xrange(n): # b is the sell date
            for a in xrange(b): # a is the buy date, which must be before b
                dp[b] = max(dp[b], dp[b - 1], dp[a - 1] - prices[a] + prices[b]) # subtract prices[a] for buying, add prices[b] for selling
        return max(dp) # best for overall N days
    
    # By isolating variables out of the inner for loop, I came to this:
    
    def maxProfixIsolatedVariables(prices):
        n = len(prices)
        dp = [0] * (n + 1)
        for b in xrange(n): # b is the sell date
            dp[b] = max(0, dp[b - 1])
            high = -1e18
            for a in xrange(b):
                high = max(high, dp[a - 1] - prices[a])
            dp[b] = max(dp[b], high + prices[b])
        return max(dp) # best for overall N days
    
    # Now notice that `high` is recalculated every loop, and only one new item is added every iteration. We can remove the inner loop and turn it O(N) :)
    # This led to my final solution found at the top, AC
    
