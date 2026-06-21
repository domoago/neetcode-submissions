class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.tail = self.head
        self.currPage = self.head

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.currPage.next = newNode
        newNode.prev = self.currPage
        self.currPage = newNode
        self.tail = newNode

    def back(self, steps: int) -> str:
        while self.currPage and self.currPage.prev and steps:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.val

    def forward(self, steps: int) -> str:
        while self.currPage and self.currPage.next and steps:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)