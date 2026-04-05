class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1.0 / x
            n = -n

        def solve(k):
            if k == 0:
                return 1.0
            half = solve(k // 2)
            if k % 2 == 0:
                return half * half
            else:
                return half * half * x

        return solve(n)