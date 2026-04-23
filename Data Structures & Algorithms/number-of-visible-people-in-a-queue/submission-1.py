class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # a person can see next, other then last one
        # maintain curr_tallest, if next is smaller then stop counting
        n = len(heights)
        res = []
        
        for i in range(n):
            count = 0
            curr_tallest = 0
            for j in range(i + 1, n):
                if min(heights[i], heights[j]) > curr_tallest:
                    count += 1
                curr_tallest = max(curr_tallest, heights[j])
            res.append(count)
        return res
