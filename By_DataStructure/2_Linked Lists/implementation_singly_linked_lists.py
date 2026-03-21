"""
Singly Linked List Implementation

Pattern: Linked List (Node-based Data Structure)
Concept: Singly Linked List with Dummy Head

Key Characteristics of Singly Linked Lists:
- Non-contiguous memory: nodes can be scattered in memory
- Each node contains: data (val) + pointer to next node (next)
- Only traverse in one direction (forward)
- Dynamic size: grows/shrinks easily without reallocation
- No random access: must traverse from head to reach any position

Singly Linked List vs Array:
- Array: O(1) access, O(n) insert/delete (except at end)
- Linked List: O(n) access, O(1) insert/delete (if you have the node)
- Array: contiguous memory, better cache locality
- Linked List: scattered memory, more overhead per element (extra pointer)

Dummy Head Pattern:
- Start with a dummy node that doesn't hold real data
- Real list begins at head.next
- Simplifies edge cases (empty list, removing first element)
- No special handling needed for operations at the beginning

Operations Time Complexity:
- insertEnd(): O(1) - we maintain a tail pointer
- remove(index): O(n) - must traverse to index
- Access by index: O(n) - must traverse from head
- insertBeginning(): O(1) - insert after dummy head (not shown)

Space Complexity: O(n) - each node needs extra space for 'next' pointer

Common Linked List Interview Problems:
- Reverse linked list
- Detect cycle (Floyd's algorithm)
- Merge two sorted lists
- Find middle element (fast/slow pointers)
- Remove nth node from end
"""


class ListNode:
    """
    A single node in a singly linked list.
    
    Each node stores a value and a reference to the next node.
    The last node in the list has next = None.
    """
    
    def __init__(self, val):
        """
        Initialize a list node with a value.
        
        Args:
            val: int - the data stored in this node
            
        Attributes:
            val: int - the data value
            next: ListNode - pointer to the next node (None if this is the last node)
        """
        self.val = val  # Data stored in this node
        self.next = None  # Pointer to next node (initially None)


class LinkedList:
    """
    A singly linked list implementation using the dummy head pattern.
    
    The dummy head simplifies operations by ensuring head is never None,
    eliminating special cases for empty lists and operations at the beginning.
    """
    
    def __init__(self):
        """
        Initialize an empty linked list with a dummy head node.
        
        Structure:
            dummy (-1) -> None
            ^             ^
            head          tail
            
        The dummy node's value (-1) is arbitrary and never accessed.
        Both head and tail initially point to the dummy node.
        Real data starts at head.next.
        """
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)  # Dummy head node (sentinel)
        self.tail = self.head  # Tail also points to dummy (list is empty)
    
    def insertEnd(self, val):
        """
        Insert a new node with value 'val' at the end of the list.
        
        Time Complexity: O(1) - we maintain a tail pointer
        Space Complexity: O(1) - creating one new node
        
        Args:
            val: int - value to insert at the end
            
        Strategy:
            1. Create new node
            2. Link current tail to new node
            3. Update tail to point to new node
            
        Example progression:
            Before: dummy -> A -> B -> None (tail = B)
            After:  dummy -> A -> B -> C -> None (tail = C)
        """
        self.tail.next = ListNode(val)  # Link current tail to new node
        self.tail = self.tail.next  # Move tail pointer to the new last node

    def remove(self, index):
        """
        Remove the node at the specified index (0-indexed).
        
        Time Complexity: O(n) - must traverse to find the node before index
        Space Complexity: O(1) - no additional space needed
        
        Args:
            index: int - position of node to remove (0 = first real node)
            
        Strategy:
            1. Traverse to the node BEFORE the one we want to remove
            2. Skip over the target node by updating pointers
            3. Update tail if we're removing the last node
            
        Example:
            Remove index 1 from: dummy -> A -> B -> C -> None
            1. Traverse to A (i=0, then i=1, curr stops at A)
            2. Set A.next = B.next (which is C)
            3. Result: dummy -> A -> C -> None
            
        Note:
            Index 0 is the first real node (head.next).
            The dummy node is not counted in indexing.
        """
        i = 0  # Counter for traversal
        curr = self.head  # Start at dummy head
                            # pointer for traversing, accessing, modifying
        
        # Traverse to the node BEFORE the one we want to remove
        while i < index and curr: # curr = None => end of list
            i += 1
            curr = curr.next  # Move to next node
        
        # Remove the node ahead of curr
        if curr and curr.next:  # Check both curr and the node to remove exist
            if curr.next == self.tail:  # Special case: removing the last node
                self.tail = curr  # Update tail to point to the new last node
            curr.next = curr.next.next  # Skip over the node (removes it from list)

    def print(self):
        """
        Print all values in the list in order.
        
        Time Complexity: O(n) - must visit every node
        Space Complexity: O(1) - no additional space needed
        
        Format: val1 -> val2 -> val3 ->
        
        Note:
            Starts at head.next to skip the dummy node.
            Only prints real data nodes.
        """
        curr = self.head.next  # Start at first real node (skip dummy)
        while curr:  # Traverse until we reach None
            print(curr.val, " -> ", end="")  # Print value with arrow
            curr = curr.next  # Move to next node
        print()  # Newline at end