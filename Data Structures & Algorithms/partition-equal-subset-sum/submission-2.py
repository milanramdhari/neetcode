class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        half = sum(nums)/2

        dp = {}

        def findHalf(i, sum):
            if i >= len(nums) or  sum > half:
                return False
            if sum == half:
                return True

            if (i,sum) in dp:
                return dp[(i,sum)]

            res1 = findHalf(i+1, sum + nums[i])
            res2 = findHalf(i+1, sum)

            dp[(i,sum)] = res1 or res2
            return dp[(i,sum)]

        return findHalf(0, 0)
        