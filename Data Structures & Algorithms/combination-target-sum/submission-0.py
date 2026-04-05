class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, remaining - nums[i])
                subset.pop()
            
        backtrack(0, target)
        return res

        