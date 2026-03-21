"""
Custom Linked List Implementation

Problem: LeetCode 707 - Design Linked List
Pattern: Singly Linked List with Dummy Head and Tail

Key Design Decisions:
- Uses singly linked list (only 'next' pointers, no 'prev')
- Dummy head and tail sentinels to simplify edge cases
- Tracks size explicitly for O(1) validation checks
- 0-indexed like arrays

Structure:
    head (-1) -> node0 -> node1 -> ... -> nodeN -> tail (-1)
    ^                                               ^
    dummy                                          dummy

Why Track Size:
- Enables O(1) validation for addAtIndex and deleteAtIndex
- Without it, we'd need to traverse entire list to check bounds
- Trade-off: extra variable to maintain vs faster validation

Operations Time Complexity:
- get(index): O(n) - traverse to index
- addAtHead(val): O(1) - insert after dummy head
- addAtTail(val): O(n) - must traverse to find last real node (no prev pointer)
- addAtIndex(index, val): O(n) - traverse to position
- deleteAtIndex(index): O(n) - traverse to position

Note on addAtTail:
- O(n) because we don't have a 'prev' pointer (singly linked)
- If this were doubly linked, we could do tail.prev to get O(1)
- This is a key tradeoff: singly linked saves memory but slower tail operations

Space Complexity: O(1) per operation (creating/deleting single nodes)
Overall space: O(n) where n is number of elements in list
"""


class ListNode:
    """
    A single node in a singly linked list.
    
    Contains a value and a pointer to the next node.
    """
    
    def __init__(self, val: int):
        """
        Initialize a list node.
        
        Args:
            val: int - the data value stored in this node
        """
        self.val = val  # Data stored in this node
        self.next = None  # Pointer to next node (None initially)
        

class MyLinkedList:
    """
    A singly linked list implementation with dummy head and tail sentinels.
    
    Maintains a size counter for efficient bounds checking.
    All operations are 0-indexed like arrays.
    """

    def __init__(self):
        """
        Initialize an empty linked list with dummy head and tail.
        
        Initial structure:
            head (-1) -> tail (-1)
            
        Size starts at 0 (no real nodes yet).
        """
        self.head = ListNode(-1)  # Dummy head sentinel
        self.tail = ListNode(-1)  # Dummy tail sentinel
        self.head.next = self.tail  # Connect head to tail (empty list)
        self.size = 0  # Track number of real nodes (not including dummies)

    def get(self, index: int) -> int:
        """
        Get the value of the node at the specified index.
        
        Time Complexity: O(n) - must traverse to index
        Space Complexity: O(1) - no additional space
        
        Args:
            index: int - position to retrieve (0-indexed)
            
        Returns:
            int - value at index, or -1 if index is invalid
            
        Strategy:
            1. Traverse from head.next (first real node)
            2. Count up to the target index
            3. Return value if valid, -1 if out of bounds
        """
        i = 0  # Counter for traversal
        curr = self.head.next  # iteration starts at first real node
        
        # Traverse to the target index
        while i < index and curr:
            i += 1
            curr = curr.next
            
        # Check if index is valid
        if curr is None or curr == self.tail:  # if index is out of bounds, or curr lands at tail
            return -1  # Invalid index
        else:
            return curr.val  # Return the value at the index

    def addAtHead(self, val: int) -> None:
        """
        Add a node at the beginning of the list (after dummy head).
        
        Time Complexity: O(1) - constant time pointer updates
        Space Complexity: O(1) - creating one new node
        
        Args:
            val: int - value to insert at head
            
        Strategy (2 pointer updates):
            1. Create new node
            2. Point newNode.next to current first real node
            3. Point head.next to newNode
            4. Increment size
            
        Example:
            Before: head -> A -> tail
            After:  head -> newNode -> A -> tail
        """
        newNode = ListNode(val)  # Create new node
        newNode.next = self.head.next  # pointing newnode.next to first real node
        self.head.next = newNode  # pointing head to newnode
        self.size += 1  # each time method is called

    def addAtTail(self, val: int) -> None:
        """
        Add a node at the end of the list (before dummy tail).
        
        Time Complexity: O(n) - must traverse to find last real node
        Space Complexity: O(1) - creating one new node
        
        Args:
            val: int - value to insert at tail
            
        Strategy:
            1. Create new node and point it to tail
            2. Traverse from head to find last real node
            3. Point last real node to newNode
            4. Increment size
            
        Note:
            O(n) because we lack 'prev' pointer in singly linked list.
            Doubly linked would make this O(1).
            
        Example:
            Before: head -> A -> tail
            After:  head -> A -> newNode -> tail
        """
        newNode = ListNode(val)  # Create new node
        newNode.next = self.tail  # newnode.next points to tail
        curr = self.head  # want to access last real node without prev pointer
        
        # Traverse to find last real node
        while curr.next != self.tail:  # instantly breaks if empty
            curr = curr.next  # stops at last real node
            
        curr.next = newNode  # Link last real node to new node
        self.size += 1  # Increment size

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node before the specified index position.
        
        Time Complexity: O(n) - must traverse to index
        Space Complexity: O(1) - creating one new node
        
        Args:
            index: int - position where new node should be inserted
            val: int - value for the new node
            
        Special Cases:
            - index == size: append to end (call addAtTail)
            - index > size: invalid, do nothing
            - index == 0: insert at head
            
        Strategy:
            1. Validate index (if > size, return)
            2. If index == size, use addAtTail
            3. Traverse to node BEFORE target index
            4. Insert new node between curr and curr.next
            5. Increment size
            
        Example:
            addAtIndex(1, X) on: head -> A -> B -> tail
            Result: head -> A -> X -> B -> tail
        """
        if index > self.size:  # invalid
            return None  # exit, no addition
            
        if index == self.size:  # Special case: append to end
            self.addAtTail(val)
            return None  # exit to prevent double addition

        newNode = ListNode(val)  # Create new node
        i = -1  # starting before index 0, in case index = 0
        curr = self.head  # iterating from before index 0, in case index = 0
        
        # Traverse to node BEFORE target index
        while i < (index - 1) and curr:  # want to stop at node before index
            i += 1
            curr = curr.next
            
        # Insert new node
        newNode.next = curr.next  # pointing newnode.next to node presently at index being shifted right
        curr.next = newNode  # point node before index to newnode
        self.size += 1  # Increment size

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the node at the specified index.
        
        Time Complexity: O(n) - must traverse to index
        Space Complexity: O(1) - no additional space
        
        Args:
            index: int - position of node to delete
            
        Validation:
            - index < 0: invalid
            - index >= size: invalid (out of bounds)
            
        Strategy:
            1. Validate index
            2. Traverse to node BEFORE target index
            3. Skip over the target node (curr.next = curr.next.next)
            4. Decrement size
            
        Example:
            deleteAtIndex(1) on: head -> A -> B -> C -> tail
            Result: head -> A -> C -> tail (B is orphaned)
        """
        if (index < 0) or (index >= self.size):  # index validation, handles edge cases eg. when deleting from an empty list, or curr.next = self.tail
            return None  # exit, no deletion
            
        i = -1  # Start before index 0
        curr = self.head  # Start at dummy head
        
        # Traverse to node BEFORE target index
        while i < (index - 1) and curr:
            i += 1
            curr = curr.next
            
        # Skip over the node at index (delete it)
        curr.next = curr.next.next  # Bypass the node at index
        self.size -= 1  # Decrement size


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)