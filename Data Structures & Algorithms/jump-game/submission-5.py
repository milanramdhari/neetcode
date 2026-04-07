class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # try larger jump first and then smaller jumps
        # this can be solved with greedy too
        
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
        