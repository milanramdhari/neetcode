class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        
        pac_matrix = [[False] * cols for i in range(rows)]
        atl_matrix = [[False] * cols for i in range(rows)]

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, matrix):

            if (i < 0 or j < 0 or i >= rows or j >= cols or matrix[i][j]):
                return
           
            matrix[i][j] = True
            
            for a, b in dirs:
                new_i, new_j = i + a, j + b
                if (0 <= new_i < rows and 0 <= new_j < cols and not matrix[new_i][new_j] and heights[new_i][new_j] >= heights[i][j]):
                    dfs(new_i, new_j, matrix)

        
        for i in range(rows):
            dfs(i, 0, pac_matrix)
            dfs(i, cols - 1, atl_matrix)

        for i in range(cols):
            dfs(0, i, pac_matrix)
            dfs(rows - 1, i, atl_matrix)

        print(pac_matrix)
        print(atl_matrix)

        res = []

        for i in range(rows):
            for j in range(cols):
                if pac_matrix[i][j] and atl_matrix[i][j]:
                    res.append([i, j])

        return res
        
            