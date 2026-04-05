class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # use union and find to solve this problem

        parents = [i for i in range(1, len(edges)+1)]

        def find(node):
            while parents[node - 1] != node:
                node = parents[node - 1]
            return node

        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return 0
            else:
                parents[par1 - 1] = par2
                return 1

        for edge in edges:
            node1, node2 = edge
            if union(node1, node2):
                continue
            else:
                return edge
        
        return []


        