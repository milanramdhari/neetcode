class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = [temperatures[n-1]]
        res = []
        res.append(0)

        for i in range(n-2, -1, -1):
            curr = 0
            found = False
            print(stack)
            for j in range(len(stack) - 1, -1, -1):
                curr += 1
                if stack[j] > temperatures[i]:
                    found = True
                    break
            
            if found:
                res.append(curr)
            else:
                res.append(0)
            stack.append(temperatures[i])
        
        res.reverse()
        return res