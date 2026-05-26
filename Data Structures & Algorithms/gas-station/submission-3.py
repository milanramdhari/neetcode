class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start with highest gas
        n = len(gas)
        surplus = [gas[i] - cost[i] for i in range(n)]
        start = 0
        total = 0

        if sum(surplus) < 0:
            return -1

        for i in range(n):
            total += surplus[i]
            if total < 0:
                start = i + 1
                total = 0
        
        return start


            



        