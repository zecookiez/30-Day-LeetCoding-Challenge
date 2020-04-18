class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # Empty grid check
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                best = 1e9
                if i != 0: # Move down
                    best = min(best, grid[i - 1][j])
                if j != 0: # Move right
                    best = min(best, row[j - 1])
                grid[i][j] = val + (best if best < 1e9 else 0)
        
        return grid[-1][-1]
