class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        memo = {}

        def check(start):
            if start >= last_index:
                return True

            if start in memo:
                return memo[start]
            
            for i in range(nums[start], 0, -1):
                if check(start + i):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False

        return check(0)
        