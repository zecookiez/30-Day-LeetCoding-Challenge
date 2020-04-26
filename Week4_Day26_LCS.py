class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        # Optimized O(NM), runs in 160ms with O(M) memory
        
        dp = [0] * (len(text2) + 1)
        for ch1 in text1:
            prev = new_prev = 0
            for j, ch2 in enumerate(text2):
                new_prev = dp[j]
                if ch1 != ch2:
                    if dp[j - 1] > dp[j]:
                        dp[j] = dp[j - 1]
                else:
                    dp[j] = 1 + prev
                prev = new_prev
        return dp[-2]
