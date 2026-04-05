# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checkSame(node, subRoot):
            if node is None and subRoot is None:
                return True

            if node is None or subRoot is None or node.val != subRoot.val:
                return False
  
            return checkSame(node.left, subRoot.left) and checkSame(node.right, subRoot.right)


        def dfs(node):
            if not node or not subRoot:
                return False
            
            if node.val == subRoot.val and checkSame(node, subRoot):
                    return True

            left = dfs(node.left)
            right = dfs(node.right)

            return left or right

        return dfs(root)
        