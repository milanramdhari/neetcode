# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use BFS to solve 
        # add all the node of a level 
        # increment depth and remove all the node of that 
        # level while adding their childrens
        if root is None:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            level = len(queue)
            for _ in range(level):
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            depth += 1
        return depth 



        