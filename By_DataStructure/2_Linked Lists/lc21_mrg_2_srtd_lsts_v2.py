"""
Merge Two Sorted Linked Lists

Problem: LeetCode 21 - Merge Two Sorted Lists
Pattern: Two Pointers + Linked List + Dummy Head

Key Insights:
- Both lists are already sorted in non-decreasing order
- Use merge algorithm from merge sort (but on linked lists, not arrays)
- Compare front elements of both lists, attach smaller one to result
- Use dummy head to simplify edge cases (empty lists, first node)
- When one list exhausted, attach remainder of other list

Why Dummy Head:
- Eliminates special case for first node (no "if result is empty" checks)
- Simplifies pointer manipulation throughout the merge
- Final result is dummy.next (first real merged node)

Algorithm (Two Pointer Approach):
1. Create dummy node and curr pointer
2. While both lists have nodes:
   - Compare front values
   - Attach smaller node to curr
   - Advance pointer in the list we took from
   - Move curr forward
3. Attach remaining nodes from whichever list has leftovers
4. Return dummy.next

Visual Example:
    list1: 1 -> 2 -> 4 -> None
    list2: 1 -> 3 -> 4 -> None
    
    Step 1: Compare 1 vs 1 (equal, take list1)
    merged: dummy -> 1, list1 advances to 2
    
    Step 2: Compare 2 vs 1
    merged: dummy -> 1 -> 1, list2 advances to 3
    
    Step 3: Compare 2 vs 3
    merged: dummy -> 1 -> 1 -> 2, list1 advances to 4
    
    Step 4: Compare 4 vs 3
    merged: dummy -> 1 -> 1 -> 2 -> 3, list2 advances to 4
    
    Step 5: Compare 4 vs 4 (equal, take list1)
    merged: dummy -> 1 -> 1 -> 2 -> 3 -> 4, list1 becomes None
    
    Step 6: list1 is None, attach rest of list2
    merged: dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

Time Complexity: O(n + m) where n, m are lengths of list1, list2
- We visit each node exactly once

Space Complexity: O(1)
- Only use a few pointers (dummy, curr)
- Reuse existing nodes, don't create new ones
- Note: We're rearranging existing nodes, not creating a new list

Common Follow-ups:
- Merge K sorted lists (use heap/priority queue)
- Merge sorted arrays instead of linked lists
- Sort a linked list (can use merge sort with this as subroutine)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.
        
        Time Complexity: O(n + m) - visit each node once
        Space Complexity: O(1) - only use constant extra space
        
        Args:
            list1: Optional[ListNode] - head of first sorted linked list
            list2: Optional[ListNode] - head of second sorted linked list
            
        Returns:
            Optional[ListNode] - head of merged sorted linked list
            
        Strategy:
            1. Use dummy head to simplify edge cases
            2. Compare front nodes of both lists
            3. Attach smaller node to result, advance that list's pointer
            4. When one list exhausted, attach remainder of other list
            5. Return dummy.next (skip the dummy node)
            
        Edge Cases:
            - Both lists empty: return None (dummy.next = None)
            - One list empty: return the other list
            - Lists of different lengths: attach remainder after main loop
            - Equal values: arbitrarily take from list1 (using <=)
        """
        dummy = ListNode()  # Dummy head to simplify pointer manipulation
        curr = dummy  # Pointer to build the merged list

        # While both lists have nodes remaining
        while list1 and list2:
            # Compare front values and attach the smaller one
            if list1.val <= list2.val:  # Take from list1 (handles equal case too)
                curr.next = list1  # Attach list1's current node to result
                list1 = list1.next  # Advance list1 pointer
            else:  # Take from list2
                curr.next = list2  # Attach list2's current node to result
                list2 = list2.next  # Advance list2 pointer
            curr = curr.next  # Move curr forward to the newly attached node
            
        # At this point, at least one list is exhausted
        # Attach the remainder of whichever list still has nodes
        if list1:  # list1 has remaining nodes
            curr.next = list1  # Attach rest of list1
        else:  # list2 has remaining nodes (or both are None)
            curr.next = list2  # Attach rest of list2 (or None if both empty)

        return dummy.next  # Return first real node (skip dummy)



if __name__ == "__main__":
    # Test case 1: Both lists have multiple elements
    solver = Solution()
    list11 = [1,2,4]
    list12 = [1,3,4]
    output1 = solver.mergeTwoLists(list1=list11, list2=list12)
    print(output1)  # Expected: [1,1,2,3,4,4]
    
    # Test case 2: Both lists are empty
    solver = Solution()
    list21 = []
    list22 = []
    output1 = solver.mergeTwoLists(list1=list21, list2=list22)
    print(output1)  # Expected: [] (None)

    # Test case 3: One list is empty
    solver = Solution()
    list31 = []
    list32 = [0]
    output1 = solver.mergeTwoLists(list1=list31, list2=list32)
    print(output1)  # Expected: [0]