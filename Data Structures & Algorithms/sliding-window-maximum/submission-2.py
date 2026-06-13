class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, -nums[i])

        
        i = 0
        j = k - 1
        res = []
        while j < len(nums):
            res.append(-max_heap[0])
            max_heap.remove(-nums[i])
            heapq.heapify(max_heap)
            i += 1
            j += 1

            if j < len(nums):
                heapq.heappush(max_heap, -nums[j])
        
        return res
            



        