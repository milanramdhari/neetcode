class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []

        if not tickets:
             return path
        
        graph = {}
        for depart, arrival in tickets:
            if depart not in graph:
                graph[depart] = []
            if arrival not in graph:
                graph[arrival] = []
            
            graph[depart].append(arrival)

        for arr in graph.values():
            arr.sort()

        def dfs(start):
            while graph[start]:
                next_stop = graph[start].pop(0)
                dfs(next_stop)
            path.insert(0, start)
        
        dfs("JFK")
        return path