class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # min heap
        # dict to store curr min times 
        # graph 

        # graph
        graph = {i: [] for i in range(1, n+1)}
        for time in times:
            u,v,w = time
            graph[u].append([v, w])
        
        # (dist, node)
        min_heap = [(0,k)]
        dist = {}

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            if node in dist:
                continue
            
            dist[node] = curr_dist

            for nei,w in graph[node]:
                if nei not in  dist:
                    heapq.heappush(min_heap, (w + curr_dist, nei))
            
        if len(dist) != n:
            return -1
        else:
            return max(dist.values())



        
        
            


        



        