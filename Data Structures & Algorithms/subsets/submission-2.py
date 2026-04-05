class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for loop backtracking

        res, subset = [], []

        def backtrack(i):
            res.append(subset.copy())
            for i in range(i, len(nums)):
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return res
        