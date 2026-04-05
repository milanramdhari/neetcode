class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        def count(i):
            res = 0
            while i > 0:
                res += 1
                i = i & i-1
            return res

        for i in range(n+1):
            result.append(count(i))
        return result
        