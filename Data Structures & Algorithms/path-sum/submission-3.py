# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backTrack(root, currSum):
            if not root:
                return False
            currSum += root.val
            if not root.left and not root.right:
                return True if currSum == targetSum else False
            return backTrack(root.left, currSum) or backTrack(root.right, currSum)
        return backTrack(root, 0)
