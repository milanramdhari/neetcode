class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST
        # make a weighted graph : edge[i] = [a,b,w]
        # prim's algo to get MST
        # add first point in the visited set and add all its neigbors

        visited = set()
        minHeap = [[0, 0]]
        res = 0

        # weighted graph
        # graph: point: []
        graph = {i:[] for i in range(len(points))} 
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        while len(visited) < len(points):
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in graph[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return res

            





        