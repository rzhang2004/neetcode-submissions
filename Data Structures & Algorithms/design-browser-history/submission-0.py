class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        home = ListNode(homepage)
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = home
        self.tail.prev = home
        home.next = self.tail
        home.prev = self.head

        self.currNode = home        

    def visit(self, url: str) -> None:
        new = ListNode(url)
        self.currNode.next = new
        new.prev = self.currNode
        self.tail.prev = new
        new.next = self.tail
        self.currNode = new 
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.currNode.prev is self.head:
                break
            self.currNode = self.currNode.prev
        return self.currNode.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.currNode.next is self.tail:
                break
            self.currNode = self.currNode.next
        return self.currNode.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)