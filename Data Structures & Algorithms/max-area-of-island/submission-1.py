class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        size = 0 
        curr_size = 0

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    curr_size = self.mark_island(grid, i, j, rows, cols, 0)
                if (curr_size > size):
                    size = curr_size
        return size
    
    def mark_island(self, grid: List[List[str]], i: int, j: int, rows: int, cols: int, size: int) -> int:
        # use dfs to expand from i and j and mark the whole island to "0"
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return size
    
        if (grid[i][j] == 0):
            return size
        
        grid[i][j] = 0
    
        return (1 + self.mark_island(grid, i + 1, j, rows, cols, size) + self.mark_island(grid, i - 1, j, rows, cols, size) + self.mark_island(grid, i, j + 1, rows, cols, size) + self.mark_island(grid, i, j - 1, rows, cols, size))  