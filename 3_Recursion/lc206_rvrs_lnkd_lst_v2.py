"""
Reverse Linked List (Recursive Approach)

Problem: LeetCode 206 - Reverse Linked List (Recursive Solution)
Pattern: Recursion + Linked List Manipulation

Key Concept:
- Recursively reverse the rest of the list first
- Then fix the current node's pointers on the way back up
- The deepest recursion (tail of original list) becomes the new head

Why This Is Tricky:
- Hard to visualize what happens during recursion unwinding
- Must understand that recursion processes nodes in REVERSE order
- The "magic" happens as the call stack unwinds, not on the way down
- new_head is set at the deepest level and passed back up unchanged

Algorithm (Recursive Approach):
1. Base case: if head is None or single node, return it (already reversed)
2. Recursively reverse the rest of the list (head.next onwards)
3. Save the new_head returned from recursion (this never changes)
4. On the way back up, fix pointers:
   - Make head.next point back to head (reverse the link)
   - Set head.next to None (break forward link, will be updated by caller)
5. Return new_head back up the call stack

Visual Walkthrough for [1,2,3]:
    
    Call Stack (going down):
    reverseList(1) calls reverseList(2) calls reverseList(3)
    
    At deepest level (3):
    - head = 3, head.next = None
    - Base case: return 3
    - new_head = 3 (this becomes the final answer)
    
    Unwinding (coming back up):
    
    Back at reverseList(2):
    - head = 2, new_head = 3 (from recursion)
    - head.next = 3 (currently)
    - head.next.next = head → 3.next = 2 (reverse the link)
    - head.next = None → 2.next = None (break forward link)
    - State: 3 -> 2 -> None
    - Return new_head (3)
    
    Back at reverseList(1):
    - head = 1, new_head = 3 (from recursion)
    - head.next = 2 (currently, but 2 now points back)
    - head.next.next = head → 2.next = 1 (reverse the link)
    - head.next = None → 1.next = None (break forward link)
    - State: 3 -> 2 -> 1 -> None
    - Return new_head (3)
    
    Final result: 3 -> 2 -> 1 -> None

Key Insight - "head.next.next = head":
    Before: head -> head.next -> ...
    After:  head <- head.next -> ...
    
    Example with nodes 1 and 2:
    Before: 1 -> 2 -> (rest of reversed list)
    Execute: 1.next.next = 1  (same as 2.next = 1)
    After:  1 <- 2 -> (rest)
    Then:   1.next = None to complete the reversal

Why new_head Never Changes:
- new_head is set at the deepest recursion (original tail)
- It represents the new head of the fully reversed list
- We just pass it back up unchanged through all recursive calls
- It's like a "message" being passed back to the top

Time Complexity: O(n) - visit each node exactly once during recursion
Space Complexity: O(n) - recursion call stack goes n levels deep

Recursive vs Iterative:
- Recursive: O(n) space, elegant, harder to understand
- Iterative: O(1) space, more efficient, easier to debug
- Recursive: risk of stack overflow for very long lists (n > ~10,000)
- Iterative: no such risk

Interview Considerations:
- Interviewers often ask for BOTH solutions
- Recursive solution tests understanding of recursion mechanics
- Must explain what happens during unwinding phase
- Good follow-up: "Can you do it iteratively to save space?"
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list using recursion.
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(n) - recursion call stack depth
        
        Args:
            head: Optional[ListNode] - head of the original linked list
            
        Returns:
            Optional[ListNode] - head of the reversed linked list
            
        Strategy (Recursive):
            1. Base case: if empty or single node, return it
            2. Recursively reverse everything after head
            3. Save new_head (tail of original, head of reversed)
            4. Reverse current node's link on the way back up
            5. Break forward link (set head.next = None)
            6. Pass new_head back up
            
        Example Execution for [1,2,3]:
            reverseList(1):
                reverseList(2):
                    reverseList(3):
                        return 3  # base case
                    new_head = 3
                    2.next.next = 2  # 3.next = 2
                    2.next = None
                    return 3
                new_head = 3
                1.next.next = 1  # 2.next = 1
                1.next = None
                return 3
            Result: 3 -> 2 -> 1 -> None
            
        Edge Cases:
            - Empty list (head = None): return None
            - Single node (head.next = None): return head
            - Two nodes: reverse them
        """
        # Base case: empty list or single node
        # If we're at the end of the list, or list is empty, just return it
        # A single node or empty list is already "reversed"
        if head is None or head.next is None:
            return head

        # Recursive step: reverse the rest of the list first
        # This goes all the way to the end before doing anything
        new_head = self.reverseList(head.next)  # recurse first, save the new head
        
        # Now we're unwinding: fix pointers for current node
        # At this point, everything after head is already reversed
        # We need to make the next node point back to us
        head.next.next = head  # make next node point back to me
        
        # Break the forward link to complete the reversal at this level
        # This node now points to None (will be updated by caller if not tail)
        head.next = None  # break the forward pointer
        
        # Pass the new head back up the call stack
        # new_head was set at the deepest recursion and never changes
        return new_head  # pass the new head back up