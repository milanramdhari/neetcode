class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min = 1
        curr_max = 1

        for num in nums:
            temp = curr_max
            curr_max = max(num*curr_max, num*curr_min, num)
            curr_min = min(num*temp, num*curr_min, num)
            res = max(res, curr_max)
        
        return res




        