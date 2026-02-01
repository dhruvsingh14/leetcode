'''
Approach: 
If we use a doubly linked list. 
nodes can store url's as value.
.next can navigate forward
and .prev can navigate back
we will also need a pointer to track which webpage we are on
'''

class ListNode:
    def __init__(self, url: str):
        self.val = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.curr = ListNode(homepage)

        self.head.next = self.curr
        self.curr.prev = self.head

        self.curr.next = self.tail
        self.tail.prev = self.curr      

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.curr.next = newNode
        newNode.prev = self.curr

        newNode.next = self.tail
        self.tail.prev = newNode   

        self.curr = newNode


    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.prev != self.head:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val      

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.next != self.tail:
            self.curr = self.curr.next
            i += 1
        return self.curr.val      
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)