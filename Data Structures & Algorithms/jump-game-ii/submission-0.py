class Solution:
    def jump(self, nums: List[int]) -> int:
        # greddy algo 

        curr_max = 0
        max_far = 0
        jumps = 0

        for i in range(len(nums) - 1):
            max_far = max(max_far, i + nums[i])

            if i == curr_max:
                jumps += 1
                curr_max = max_far
        
        return jumps
        