class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        
        memo = [-1] * (n+1)
        memo[0], memo[1], memo[2] = 0, 1, 2
        
        def solve(n):
            
            if memo[n] != -1:
                return memo[n]

            memo[n] = solve(n-1) + solve(n-2)
            return memo[n]
        
        return solve(n)
        