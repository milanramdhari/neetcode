# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.sorted_tree = [] 

        if not root:
            return -1 
        
        def visitTreeInOrder(root):
            if not root:
                return
            
            left = visitTreeInOrder(root.left)

            if left: 
                self.sorted_tree.append(left.val)
            
            self.sorted_tree.append(root.val)

            right = visitTreeInOrder(root.right)
            if right:
                self.sorted_tree.append(right.val)

            return


        
        visitTreeInOrder(root)

        return self.sorted_tree[k-1]
        