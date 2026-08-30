class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next
    
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        lruNode = self.cache[key]
        self.remove(lruNode)
        self.insert(lruNode)
        return lruNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
