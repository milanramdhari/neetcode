class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start with highest gas
        n = len(gas)
        surplus = [gas[i] - cost[i] for i in range(n)]

        for i in range(n):
            total = surplus[i]
            j = (i + 1) % n

            while total >= 0 and j != i:
                total += surplus[j]
                j = (j + 1) % n

            if j == i and total >= 0:
                return i
        
        return -1


            



        