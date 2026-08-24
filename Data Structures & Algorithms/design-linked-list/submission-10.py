class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1
            
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.size:
            new_node = ListNode(val)
            curr = self.head
            for i in range(index):
                curr = curr.next
            new_node.next = curr
            new_node.prev = curr.prev
            new_node.prev.next = new_node
            curr.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        while curr and index:
            curr = curr.next
            index -= 1
        if curr and not index:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                self.head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            else:
                self.tail = curr.prev
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)