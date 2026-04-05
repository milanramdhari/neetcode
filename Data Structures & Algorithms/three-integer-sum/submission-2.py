class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums 
        # three pointer approach: left, start and end
        nums.sort()
        res = [] 

        def sortedTwoSum(target, start, end):
            target = -target
            result2 = []

            while start < end:
                if nums[start] + nums[end] == target:
                    result2.append([-target, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1

            return result2


        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = nums[i]
            start, end = i+1, len(nums) - 1
            result = sortedTwoSum(left, start, end)
            if result:
                for res2 in result:
                    res.append(res2)
            
        return res
        