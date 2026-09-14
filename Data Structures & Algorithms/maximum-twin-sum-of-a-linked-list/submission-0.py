# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        prev = None
        while fast and fast.next:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            fast = fast.next.next
        secondHalf = slow.next
        slow.next = prev
        res = 0
        while slow and secondHalf:
            res = max(slow.val + secondHalf.val, res)
            slow = slow.next
            secondHalf = secondHalf.next
        return res