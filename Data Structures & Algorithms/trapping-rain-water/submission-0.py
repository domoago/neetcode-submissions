class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        leftMax, rightMax = height[0], height[-1]
        res = 0
        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                res += max(leftMax - height[L], 0)
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                res += max(rightMax - height[R], 0)
        return res