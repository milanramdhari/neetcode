class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # approach 2

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        half = sum(nums)/2

        for i in range(len(nums)):
            if half in dp:
                return True
            nextDP = set()
            for elem in dp:
                nextDP.add(elem)
                nextDP.add(elem + nums[i])
            dp = nextDP
        
        return True if half in dp else False

        