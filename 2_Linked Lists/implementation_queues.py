"""
Queue Implementation Using Singly Linked List

Pattern: Queue (FIFO - First In First Out)
Concept: Queue Data Structure

Key Characteristics of Queues:
- FIFO ordering: First element added is first one removed
- Add to back (enqueue/push), remove from front (dequeue/pop)
- Two access points: front (left) and back (right)
- No random access - can't access middle elements directly

Real-World Analogies:
- Line at a store: first person in line is served first
- Print queue: documents print in order they were sent
- Task scheduling: process tasks in the order they arrive
- Breadth-First Search (BFS): process nodes level by level

Why Queues Matter in Interviews:
- BFS graph/tree traversal (most common use!)
- Level-order tree traversal
- Cache implementation (LRU with queue + hash map)
- Task scheduling problems
- Sliding window problems (sometimes use deque)

Queue vs Stack:
- Queue: FIFO (first in, first out) - like a line
- Stack: LIFO (last in, first out) - like a stack of plates
- Queue: add at back, remove from front
- Stack: add and remove from same end (top)

Implementation Note:
- Uses singly linked list (left = front, right = back)
- No dummy nodes in this implementation (more edge cases to handle)
- Comment notes dummy nodes would make this easier!
- Must handle empty queue carefully for both enqueue and dequeue

Operations Time Complexity:
- enqueue(): O(1) - append to right (back)
- dequeue(): O(1) - remove from left (front)
- peek/front: O(1) - access left.val (not shown)

Space Complexity: O(n) where n is number of elements in queue

Why Linked List for Queue:
- Need O(1) operations at BOTH ends (front and back)
- Array-based queue needs circular buffer or is inefficient
- Linked list naturally supports O(1) add at back, O(1) remove from front
"""


class ListNode:
    """
    A node in the queue's singly linked list.
    
    Each node represents one element in the queue.
    """
    
    def __init__(self, val):
        """
        Initialize a queue node with a value.
        
        Args:
            val: int - the data value stored in this node
        """
        self.val = val  # Data stored in this node
        self.next = None  # Pointer to next node in queue


class Queue:
    """
    Queue implementation using singly linked list without dummy nodes.
    
    Maintains pointers to both front (left) and back (right) of queue.
    Must handle empty queue edge cases carefully.
    """
    
    def __init__(self):
        """
        Initialize an empty queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Structure when empty:
            left = None, right = None
            
        Structure with elements:
            left -> node1 -> node2 -> node3 <- right
            ^                          ^
            (dequeue here)            (enqueue here)
        """
        # Implementing this with dummy nodes would be easier!
        self.left = self.right = None  # Both pointers start as None (empty queue)
    
    def enqueue(self, val):
        """
        Add an element to the back of the queue.
        
        Time Complexity: O(1) - constant pointer updates
        Space Complexity: O(1) - creating one new node
        
        Args:
            val: int - value to add to the back of queue
            
        Strategy:
            Case 1 - Non-empty queue:
                1. Create new node
                2. Link current right node to new node
                3. Move right pointer to new node
                
            Case 2 - Empty queue:
                1. Create new node
                2. Set both left and right to new node
                
        Example:
            Empty queue: left=None, right=None
            enqueue(1): left -> 1 <- right
            enqueue(2): left -> 1 -> 2 <- right
            enqueue(3): left -> 1 -> 2 -> 3 <- right
        """
        newNode = ListNode(val)  # Create new node with value

        # Queue is non-empty
        if self.right:
            self.right.next = newNode  # Link current back to new node
            self.right = self.right.next  # Move right pointer to new node
        # Queue is empty
        else:
            self.left = self.right = newNode  # Both pointers point to the only node

    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        
        Time Complexity: O(1) - constant pointer updates
        Space Complexity: O(1) - no additional space
        
        Returns:
            The value from the front of the queue, or None if queue is empty
            
        Strategy:
            1. Check if queue is empty (return None)
            2. Save value from left node
            3. Move left pointer to next node
            4. If left becomes None, also set right to None (queue is now empty)
            5. Return saved value
            
        Example:
            Queue: left -> 1 -> 2 -> 3 <- right
            dequeue(): returns 1, queue becomes: left -> 2 -> 3 <- right
            dequeue(): returns 2, queue becomes: left -> 3 <- right
            dequeue(): returns 3, queue becomes: left=None, right=None
            
        Edge Cases:
            - Empty queue: return None
            - Single element: after dequeue, both left and right become None
            - Multiple elements: move left forward
        """
        # Queue is empty
        if not self.left:
            return None  # Cannot dequeue from empty queue
        
        # Remove left node and return value
        val = self.left.val  # Save value to return
        self.left = self.left.next  # Move left pointer forward (remove front node)
        
        # If queue is now empty, update right pointer too
        if not self.left:
            self.right = None  # Both pointers should be None when empty
            
        return val  # Return the value that was at the front

    def print(self):
        """
        Print all elements in the queue from front to back.
        
        Time Complexity: O(n) - must visit every node
        Space Complexity: O(1) - no additional space
        
        Format: val1 -> val2 -> val3 ->
        
        Note:
            Traverses from left (front) to right (back).
            Does not modify the queue structure.
        """
        cur = self.left  # Start at front of queue
        while cur:  # Traverse until end
            print(cur.val, ' -> ', end="")  # Print value with arrow
            cur = cur.next  # Move to next node
        print()  # new line