class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slowTwo = 0
        while True:
            slowTwo = nums[slowTwo]
            slow = nums[slow]
            if slow == slowTwo:
                break
        return slow
