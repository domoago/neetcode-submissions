# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            lastValInLevel = None
            for i in range(len(queue)):
                currNode = queue.popleft()
                lastValInLevel = currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(lastValInLevel)
        return res
