# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return "#"
        
        res = []

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")

        if values[0] == "#":
            return None
        
        root = TreeNode(int(values[0]))
        q = deque([root])
        index = 1

        while q:
            node = q.popleft()
            if values[index] != "#":
                node.left = TreeNode(int(values[index]))
                q.append(node.left)
            index += 1
            
            if values[index] != "#":
                node.right = TreeNode(int(values[index]))
                q.append(node.right)
            index += 1
        
        return root


