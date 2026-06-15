class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n 
        stack = [] 

        for i in range(n):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))

        return res
    