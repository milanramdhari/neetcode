class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = -1 
        n = len(heights)

        for i in range(n):
            for j in range(i, n):
                res = max(res, (j - i)* min(heights[i], heights[j]))
        
        return res
        