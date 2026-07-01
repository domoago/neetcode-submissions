# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return [True, 0]
        left, right = self.dfs(root.left), self.dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, max(1 + left[1], 1 + right[1])]