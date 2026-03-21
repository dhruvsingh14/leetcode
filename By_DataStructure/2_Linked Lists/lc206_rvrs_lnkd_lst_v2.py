"""
Reverse Linked List (Iterative Approach)

Problem: LeetCode 206 - Reverse Linked List
Pattern: Linked List Manipulation + Two/Three Pointers

Key Concept:
- Reverse the direction of all 'next' pointers in the list
- Original: 1 -> 2 -> 3 -> 4 -> 5 -> None
- Reversed: None <- 1 <- 2 <- 3 <- 4 <- 5

Why This Is Tricky:
- When you reverse curr.next, you lose access to the rest of the list
- Need to save the next node BEFORE reversing the pointer
- Need three pointers: prev (before curr), curr (current), temp (after curr)

Algorithm (Iterative - Three Pointer Technique):
1. Initialize prev = None (will become new tail)
2. Initialize curr = head (start at beginning)
3. While curr is not None:
   a. Save curr.next in temp (don't lose rest of list)
   b. Reverse pointer: curr.next = prev
   c. Move prev forward to curr
   d. Move curr forward to temp
4. Return prev (new head of reversed list)

Visual Walkthrough for [1,2,3]:
    Initial:
    prev = None, curr = 1
    1 -> 2 -> 3 -> None
    
    Step 1: temp = 2, curr.next = None, prev = 1, curr = 2
    None <- 1    2 -> 3 -> None
            ^    ^
            prev curr
    
    Step 2: temp = 3, curr.next = 1, prev = 2, curr = 3
    None <- 1 <- 2    3 -> None
                 ^    ^
                 prev curr
    
    Step 3: temp = None, curr.next = 2, prev = 3, curr = None
    None <- 1 <- 2 <- 3    None
                      ^    ^
                      prev curr
    
    Return prev (which is 3, the new head)

Why prev Ends Up As New Head:
- prev always trails one step behind curr
- When curr becomes None (past end of list), prev is at the last node
- The last node of the original list becomes the first node of reversed list

Time Complexity: O(n) - visit each node exactly once
Space Complexity: O(1) - only use three pointers, no recursion stack

Iterative vs Recursive:
- Iterative: O(1) space, easier to understand for most people
- Recursive: O(n) space (call stack), more elegant but risk stack overflow
- This solution uses iterative approach

Common Interview Follow-ups:
- Reverse linked list II (reverse between positions m and n)
- Reverse nodes in k-groups
- Palindrome linked list (reverse second half and compare)
- Implement both iterative and recursive versions
"""


# Definition for singly-linked list.
class ListNode:
    """
    A node in a singly linked list.
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a list node.
        
        Args:
            val: int - value stored in the node
            next: ListNode - pointer to next node (None by default)
        """
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list iteratively.
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(1) - only use constant extra space
        
        Args:
            head: Optional[ListNode] - head of the original linked list
            
        Returns:
            Optional[ListNode] - head of the reversed linked list
            
        Strategy (Three Pointer Technique):
            1. prev tracks the node before curr (starts as None)
            2. curr tracks the current node being processed
            3. temp saves the next node before we break the link
            4. Reverse curr's pointer to point to prev
            5. Move prev and curr forward
            6. Return prev when done (it's the new head)
            
        Example:
            Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
            Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
            
        Edge Cases:
            - Empty list (head = None): return None
            - Single node: return same node (no reversal needed)
            - Two nodes: swap them
        """
        prev = None  # Will become the new tail (None at the end)
        curr = head  # Start at the head of the original list
        
        # Traverse the entire list
        while curr is not None:
            # Step 1: Save the next node (don't lose the rest of the list)
            temp = curr.next  # Store next node before we break the link
            
            # Step 2: Reverse the current node's pointer
            curr.next = prev  # Point curr backwards to prev
            
            # Step 3: Move prev and curr forward
            prev = curr  # Move prev one step forward
            curr = temp  # Move curr one step forward (to saved next node)
            
        # When loop ends, curr is None (past the end)
        # prev is at the last node of original list (first node of reversed list)
        return prev  # Return new head of reversed list


if __name__ == "__main__":
    # Test case 1: List with multiple nodes
    solver = Solution()
    head1 = [1,2,3,4,5]
    output1 = solver.reverseList(head=head1)
    print(output1)  # Expected: [5,4,3,2,1]
    
    # Test case 2: List with two nodes
    solver = Solution()
    head2 = [1,2]
    output2 = solver.reverseList(head=head2)
    print(output2)  # Expected: [2,1]

    # Test case 3: Empty list
    solver = Solution()
    head3 = []
    output3 = solver.reverseList(head=head3)
    print(output3)  # Expected: [] (None)