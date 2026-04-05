class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # flyd's algo 
        # run slow and fast until they meet, keep slow at the same place
        # add a new slow pointer a begining and keep them moving by one until they meet, that's the answer

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        new_slow = 0 
        while True:
            slow = nums[slow]
            new_slow = nums[new_slow]
            if slow == new_slow:
                return slow
        

        