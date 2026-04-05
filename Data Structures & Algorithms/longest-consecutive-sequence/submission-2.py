class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        values = set()
        maxSoFar = 1

        for num in nums:
            values.add(num)
        
        for num in nums:
            curr = num

            if num - 1 in values:
                continue
            
            count = 1
            while (curr + 1) in values:
                count += 1
                curr = curr + 1
            
            if count > maxSoFar:
                maxSoFar = count
        
        return maxSoFar
        