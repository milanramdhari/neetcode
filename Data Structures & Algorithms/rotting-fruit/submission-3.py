class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.count = -1
        has_rotten = False
        q = q = deque()
        

        for row in grid:
            if 2 in row:
                has_rotten = True

        def solve():
            while q:
                level_len = len(q)
                for i in range(level_len):
                    curr_i, curr_j = q.popleft()                    
                    if curr_i + 1 >= 0 and curr_i + 1 < rows and grid[curr_i + 1][curr_j] == 1:
                        grid[curr_i + 1][curr_j] = 2
                        q.append([curr_i+1, curr_j])
                    if curr_i - 1 >= 0 and curr_i - 1 < rows and grid[curr_i - 1][curr_j] == 1:
                        grid[curr_i - 1][curr_j] = 2
                        q.append([curr_i - 1, curr_j])
                    if curr_j - 1 >= 0 and curr_j - 1 < cols and grid[curr_i][curr_j - 1] == 1:
                        grid[curr_i][curr_j - 1] = 2
                        q.append([curr_i, curr_j - 1])
                    if curr_j + 1 >= 0 and curr_j + 1 < cols and grid[curr_i][curr_j + 1] == 1:
                        grid[curr_i][curr_j + 1] = 2
                        q.append([curr_i, curr_j + 1])
                self.count += 1

        def find_rot_fruits():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        q.append((i, j))

        
        find_rot_fruits()
        solve()

        for row in grid:
            if 1 in row:
                return -1
    
        return self.count if has_rotten else 0
                        

            
            
                
        