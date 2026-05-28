"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        visited_node = {}

        def dfs(node):
            if node in visited_node:
                return visited_node[node]
            new_cpy = Node(node.val)
            visited_node[node] = new_cpy
            for neig in node.neighbors:
                new_cpy.neighbors.append(dfs(neig))
            return new_cpy

        return dfs(node) 
        