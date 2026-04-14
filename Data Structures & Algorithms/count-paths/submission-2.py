class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = {(0,0): 1}

        def backtrack(i, j):            
            if i < 0 or j < 0:
                return 0
            
            if (i,j) in self.dp:
                return self.dp[(i, j)]
            
            self.dp[(i, j)] = backtrack(i-1, j) + backtrack(i, j-1)
            return self.dp[(i, j)]
            
        backtrack(m-1,n-1)
        return self.dp[(m-1, n-1)]
        