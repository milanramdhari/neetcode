class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # find and union the edges given to us

        parents = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while parents[node] != node:
                node = parents[node]
            return node
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parents[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parents[p1] = p2
                    rank[p2] += rank[p1]
                return 1
            return 0

        for edge in edges:
            node1, node2 = edge
            if union(node1, node2):
                n -= 1
            
        return n
        
        