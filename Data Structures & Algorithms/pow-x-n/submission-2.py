class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        initial_x = x
        ab = abs(n)
        for i in range(ab - 1):
            x = x*initial_x
        
        if n < 0:
            x = 1/x
        return x

# 2^5 
# x = 4
# i = 1