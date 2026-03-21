"""
Doubly Linked List Implementation

Pattern: Doubly Linked List (Bidirectional Node-based Data Structure)
Concept: Doubly Linked List with Dummy Head and Tail

Key Characteristics of Doubly Linked Lists:
- Each node has TWO pointers: next (forward) and prev (backward)
- Can traverse in both directions (forward and backward)
- More memory overhead: 2 pointers per node vs 1 in singly linked list
- Easier deletion: can delete node in O(1) if you have pointer to it
- More complex to maintain: must update both next and prev pointers

Doubly Linked List vs Singly Linked List:
- Singly: One direction, less memory, simpler operations
- Doubly: Both directions, more memory, easier deletions
- Singly: Can't traverse backwards
- Doubly: Can traverse backwards (useful for many algorithms)

Dummy Head AND Tail Pattern:
- Start with two dummy nodes: head (at beginning) and tail (at end)
- Real list exists between head and tail
- Simplifies ALL edge cases: empty list, single element, operations at ends
- No special handling needed for first or last element operations
- Always guaranteed: head.next exists, tail.prev exists

Initial Structure (empty list):
    head (-1) <-> tail (-1)
    ^             ^
    dummy         dummy

After inserting A, B:
    head (-1) <-> A <-> B <-> tail (-1)
    ^                         ^
    dummy                     dummy

Operations Time Complexity:
- insertFront(): O(1) - insert after dummy head
- insertEnd(): O(1) - insert before dummy tail
- removeFront(): O(1) - remove first real node
- removeEnd(): O(1) - remove last real node
- Access by position: O(n) - still need to traverse

Space Complexity: O(n) - each node needs 2 pointers (next + prev)

Common Doubly Linked List Interview Problems:
- LRU Cache implementation (very common!)
- Browser history (forward/back navigation)
- Undo/redo functionality
- Music playlist navigation
"""


class ListNode:
    """
    A single node in a doubly linked list.
    
    Each node stores a value and references to both next and previous nodes.
    """
    
    def __init__(self, val):
        """
        Initialize a doubly linked list node with a value.
        
        Args:
            val: int - the data stored in this node
            
        Attributes:
            val: int - the data value
            next: ListNode - pointer to next node (None initially)
            prev: ListNode - pointer to previous node (None initially)
        """
        self.val = val  # Data stored in this node
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node


class LinkedList:
    """
    A doubly linked list implementation using dummy head and tail sentinels.
    
    The dummy nodes bookend the list, making all operations uniform
    with no special cases for empty lists or boundary operations.
    """
    
    def __init__(self):
        """
        Initialize an empty doubly linked list with dummy head and tail.
        
        Structure after initialization:
            head (-1) <-> tail (-1)
            
        Both dummies are connected to each other.
        Real data will be inserted between them.
        """
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)  # Dummy head sentinel
        self.tail = ListNode(-1)  # Dummy tail sentinel
        self.head.next = self.tail  # Head points forward to tail
        self.tail.prev = self.head  # Tail points backward to head
    
    def insertFront(self, val):
        """
        Insert a new node at the front of the list (after dummy head).
        
        Time Complexity: O(1) - constant time pointer updates
        Space Complexity: O(1) - creating one new node
        
        Args:
            val: int - value to insert at the front
            
        Strategy (4 pointer updates required):
            1. Create new node
            2. Set newNode.prev = head
            3. Set newNode.next = head.next (first real node or tail)
            4. Update old first node's prev to point to newNode
            5. Update head.next to point to newNode
            
        Example:
            Before: head <-> A <-> tail
            After:  head <-> newNode <-> A <-> tail
        """
        newNode = ListNode(val)  # Create new node with value
        newNode.prev = self.head  # New node's prev points to dummy head
        newNode.next = self.head.next  # New node's next points to old first node

        self.head.next.prev = newNode  # Old first node's prev points back to new node
        self.head.next = newNode  # Head's next points forward to new node

    def insertEnd(self, val):
        """
        Insert a new node at the end of the list (before dummy tail).
        
        Time Complexity: O(1) - constant time pointer updates
        Space Complexity: O(1) - creating one new node
        
        Args:
            val: int - value to insert at the end
            
        Strategy (4 pointer updates required):
            1. Create new node
            2. Set newNode.next = tail
            3. Set newNode.prev = tail.prev (last real node or head)
            4. Update old last node's next to point to newNode
            5. Update tail.prev to point to newNode
            
        Example:
            Before: head <-> A <-> tail
            After:  head <-> A <-> newNode <-> tail
        """
        newNode = ListNode(val)  # Create new node with value
        newNode.next = self.tail  # New node's next points to dummy tail
        newNode.prev = self.tail.prev  # New node's prev points to old last node

        self.tail.prev.next = newNode  # Old last node's next points forward to new node
        self.tail.prev = newNode  # Tail's prev points backward to new node

    def removeFront(self):
        """
        Remove the first real node (after dummy head).
        
        Time Complexity: O(1) - constant time pointer updates
        Space Complexity: O(1) - no additional space needed
        
        Strategy (2 pointer updates required):
            1. Make head.next.next (second node) point back to head
            2. Make head point forward to head.next.next (second node)
            
        Example:
            Before: head <-> A <-> B <-> tail
            After:  head <-> B <-> tail (A is orphaned and garbage collected)
            
        Assumption:
            Assumes at least one real node exists (list is not empty).
            No bounds checking in this implementation.
        """
        # Remove first node after dummy head (assume it exists)
        self.head.next.next.prev = self.head  # Second node's prev points to head
        self.head.next = self.head.next.next  # Head's next skips first node

    def removeEnd(self):
        """
        Remove the last real node (before dummy tail).
        
        Time Complexity: O(1) - constant time pointer updates
        Space Complexity: O(1) - no additional space needed
        
        Strategy (2 pointer updates required):
            1. Make tail.prev.prev (second-to-last node) point forward to tail
            2. Make tail point backward to tail.prev.prev (second-to-last node)
            
        Example:
            Before: head <-> A <-> B <-> tail
            After:  head <-> A <-> tail (B is orphaned and garbage collected)
            
        Assumption:
            Assumes at least one real node exists (list is not empty).
            No bounds checking in this implementation.
        """
        # Remove last node before dummy tail (assume it exists)
        self.tail.prev.prev.next = self.tail  # Second-to-last node's next points to tail
        self.tail.prev = self.tail.prev.prev  # Tail's prev skips last node

    def print(self):
        """
        Print all values in the list in order (forward direction).
        
        Time Complexity: O(n) - must visit every node
        Space Complexity: O(1) - no additional space needed
        
        Format: val1 -> val2 -> val3 ->
        
        Note:
            Starts at head.next (skip dummy head)
            Stops when reaching tail (skip dummy tail)
            Only prints real data nodes
        """
        curr = self.head.next  # Start at first real node (skip dummy head)
        while curr != self.tail:  # Stop before reaching dummy tail
            print(curr.val, " -> ")  # Print value with arrow
            curr = curr.next  # Move to next node
        print()  # Newline at end