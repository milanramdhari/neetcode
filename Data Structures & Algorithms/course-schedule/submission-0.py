class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # adjacent graph 
        graph = {}
        for j in range(numCourses):
            graph[j] = []

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        visited = set()
        rec_stack = set()
        
        # check if cycle exists in graph
        def checkCycle(i, visited, rec_stack):
            if i in rec_stack:
                return True

            if i in visited:
                return False
            
            visited.add(i)
            rec_stack.add(i)

            for neig in graph[i]:
                if checkCycle(neig, visited, rec_stack):
                    return True
            
            rec_stack.remove(i)
            return False
        
        for i in range(numCourses): 
            if i not in visited and checkCycle(i, visited, rec_stack):
                return False
        return True
        