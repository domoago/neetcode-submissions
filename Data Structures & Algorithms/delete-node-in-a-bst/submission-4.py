# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root):
        if not root:
            return root
        while root and root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        curr = root
        while curr:
            if key < curr.val:
                curr.left = self.deleteNode(curr.left, key)
            elif key > curr.val:
                curr.right = self.deleteNode(curr.right, key)
            else:
                if not curr.left:
                    return curr.right
                elif not curr.right:
                    return curr.left
                else:
                    minVal = self.findMinNode(curr.right).val
                    curr.val = minVal
                    curr.right = self.deleteNode(curr.right, minVal)
            return root