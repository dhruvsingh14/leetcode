class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)  
        self.head.next = self.tail
        self.size = 0         

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next # iteration starts at first real node
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr is None or curr == self.tail: # if index is out of bounds, or curr lands at tail
            return -1
        else:
            return curr.val                

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next # pointing newnode.next to first real node
        self.head.next = newNode # pointing head to newnode
        self.size += 1 # each time method is called

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.tail # newnode.next points to tail
        curr = self.head # want to access last real node without prev pointer
        while curr.next != self.tail: # instantly breaks if empty
            curr = curr.next # stops at last real node
        curr.next = newNode 
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: # invalid
            return None # exit, no addition
        if index == self.size: 
            self.addAtTail(val)
            return None # exit to prevent double addition

        newNode = ListNode(val)
        i = -1 # starting before index 0, in case index = 0
        curr = self.head # iterating from before index 0, in case index = 0
        while i < (index - 1) and curr: # want to stop at node before index
            i += 1
            curr = curr.next   
        newNode.next = curr.next # pointing newnode.next to node presetly at index being shifted right
        curr.next = newNode # point node before index to newnode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if (index < 0) or (index >= self.size): # index validation, handles edge cases eg. when deleting from an empty list, or curr.next = self.tail
            return None # exit, no deletion        
        i = -1 
        curr = self.head 
        while i < (index - 1) and curr: 
            i += 1
            curr = curr.next   
        curr.next = curr.next.next 
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)