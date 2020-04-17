class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # "Flood-fill" problem. An island is a connected component of the 1 tiles.
        #     We can use BFS or DFS to grab  the connected components
        
        # Time complexity is O(N) --> N is the number of cells in the grid
        
        # Empty cases
        if len(grid) == 0: 
            return 0
        elif len(grid[0]) == 0:
            return 0
        
        rows    = len(grid)
        columns = len(grid[0])
        islands = 0
        
        for X in xrange(rows):
            for Y in xrange(columns):
                
                # Look for an unmarked island
                if grid[X][Y] == "0":
                    continue
                grid[X][Y] = "0" # Mark it
                
                # DFS on the grid, mark all connected lands as visited
                queue = [(X, Y)]
                
                while queue:
                    x, y = queue.pop()
                    
                    # Visit neighboring land tiles
                    for new_x, new_y in (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1):
                        
                        # Make sure it is still in the grid
                        if not rows > new_x >= 0 <= new_y < columns:
                            continue
                            
                        # Check if unmarked
                        if grid[new_x][new_y] == "1":
                            grid[new_x][new_y] = "0"
                            queue.append((new_x, new_y)) # Push to queue
                
                # Finished looking for islands
                islands += 1
        
        return islands
