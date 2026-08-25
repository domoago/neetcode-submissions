# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not len(lists):
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                listOne = lists[i]
                listTwo = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(listOne, listTwo))
            lists = mergedLists
        return lists[0]

    def mergeLists(self, listOne, listTwo):
        preHead = ListNode()
        curr = preHead
        while listOne and listTwo:
            if listOne.val < listTwo.val:
                curr.next = listOne
                listOne = listOne.next
            else:
                curr.next = listTwo
                listTwo = listTwo.next
            curr = curr.next
        curr.next = listOne or listTwo
        return preHead.next