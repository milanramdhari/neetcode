class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through the matrix, if 1 found then increase island counter and
        # mark all the land with the island as 0, so wont double count the island

        rows = len(grid)
        cols = len(grid[0])
        count = 0 

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1":
                    count += 1
                    self.mark_island(grid, i, j, rows, cols)
        
        return count


    def mark_island(self, grid: List[List[str]], i: int, j: int, rows: int, cols: int):
        # use bfs to expand from i and j and mark the whole island to "0"
        if i == -1 or j == -1 or i == rows or j == cols:
            return
        
        if (grid[i][j] == "0"):
            return
        
        grid[i][j] = "0" 
        self.mark_island(grid, i + 1, j, rows, cols) # down
        self.mark_island(grid, i - 1, j, rows, cols) # up
        self.mark_island(grid, i, j + 1, rows, cols) # right
        self.mark_island(grid, i, j - 1, rows, cols) # left

            
        
        

        