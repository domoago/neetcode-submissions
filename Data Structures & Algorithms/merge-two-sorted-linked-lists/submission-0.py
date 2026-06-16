# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        currNode = mergedList
        currNode1 = list1
        currNode2 = list2
        while currNode1 and currNode2:
            if currNode1.val < currNode2.val:
                currNode.next = currNode1
                currNode1 = currNode1.next
            else:
                currNode.next = currNode2
                currNode2 = currNode2.next
            currNode =currNode.next
        if currNode1:
            currNode.next = currNode1
        if currNode2:
            currNode.next = currNode2
        return mergedList.next
