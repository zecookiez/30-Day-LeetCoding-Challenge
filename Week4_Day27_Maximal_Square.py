class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if len(matrix) == 0:
            return 0
        
        # Helper function I've written a long time ago
        #     Solves the following problem:
        #         "Given N histogram bars with heights arr[i], find the maximal square/rectangle area within the bars"
        #
        # We can convert this problem into the problem above 
        # bonus: it's O(N) memory as well :)
        
        def histogram(arr):
            n = len(arr)
            stack = []
            best = pos = 0
            while pos < n:
                if not stack or arr[stack[-1]] <= arr[pos]:
                    stack.append(pos)
                    pos += 1
                else:
                    top = stack.pop()
                    if stack: area = min(arr[top], pos - stack[-1] - 1) #area = arr[top] * (pos - stack[-1] - 1)
                    else: area = min(arr[top], pos) #area = arr[top] * pos
                    best = max(best, area)
            while stack:
                top = stack.pop()
                if stack: area = min(arr[top], pos - stack[-1] - 1)  # area = arr[top] * (pos - stack[-1] - 1)
                else: area = min(arr[top], pos)  # area = arr[top] * pos
                best = max(best, area)
            return best * best
        
        best = 0
        cnt = [0] * len(matrix[0]) # Maintain the histogram bars' heights
        for row in matrix:
            for j, ch in enumerate(row):
                if ch == "1":
                    cnt[j] += 1 # Increase if it's a 1
                else:
                    cnt[j] = 0  # The 0 cuts off the histogram bar, so we reset to 0
            best = max(best, histogram(cnt)) # Solve for current histogram
        return best
