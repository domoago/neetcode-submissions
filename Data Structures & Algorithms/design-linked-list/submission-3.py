class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if 0 <= index <= self.size - 1:
            currNode = self.head
            for i in range(index):
                currNode = currNode.next
            return currNode.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            currNode = self.head
            newNode = ListNode(val)
            for i in range(index):
                currNode = currNode.next
            newNode.prev = currNode.prev
            newNode.next = currNode
            currNode.prev.next = newNode
            currNode.prev = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index <= self.size - 1:
            currNode = self.head
            for i in range(index):
                currNode = currNode.next
            if currNode.prev:
                currNode.prev.next = currNode.next
            else:
                currNode.next = self.head
            if currNode.next:
                currNode.next.prev = currNode.prev
            else:
                self.tail = currNode.prev
            del currNode
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)