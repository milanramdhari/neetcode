class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        map[nums[0]] = 0

        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
            
        return [-1, -1]
        