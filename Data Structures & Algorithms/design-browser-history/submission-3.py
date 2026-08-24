class Page:
    def __init__(self, page: str):
        self.val = page
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr_page = Page(homepage)

    def visit(self, url: str) -> None:
        self.curr_page.next = Page(url)
        self.curr_page.next.prev = self.curr_page
        self.curr_page = self.curr_page.next

    def back(self, steps: int) -> str:
        prev_page = None
        while self.curr_page and steps:
            prev_page = self.curr_page
            self.curr_page = self.curr_page.prev
            steps -= 1
        if self.curr_page:
            return self.curr_page.val
        else:
            self.curr_page = prev_page
            return prev_page.val

    def forward(self, steps: int) -> str:
        prev_page = None
        while self.curr_page and steps:
            prev_page = self.curr_page
            self.curr_page = self.curr_page.next
            steps -= 1
        if self.curr_page:
            return self.curr_page.val
        else:
            self.curr_page = prev_page
            return prev_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)