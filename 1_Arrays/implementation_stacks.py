"""
Stack Implementation Using Dynamic Array

Pattern: Stack (LIFO - Last In First Out)
Concept: Stack Data Structure

Key Characteristics of Stacks:
- LIFO ordering: Last element added is first one removed
- Only access the top element (most recently added)
- Three core operations: push (add), pop (remove), peek/top (view)
- No random access - can't access middle elements directly

Real-World Analogies:
- Stack of plates: add/remove from top only
- Browser back button: most recent page first
- Function call stack: most recent function returns first
- Undo/redo functionality

Why Stacks Matter in Interviews:
- Parentheses matching (LeetCode 20)
- Expression evaluation (infix/postfix conversion)
- Backtracking algorithms (DFS, maze solving)
- Min/Max stack problems (LeetCode 155)
- Next greater/smaller element problems

Operations Time Complexity:
- push(): O(1) - append to end of dynamic array
- pop(): O(1) - remove from end of dynamic array
- peek/top(): O(1) - access last element (not shown here)

Space Complexity: O(n) where n is number of elements in stack

Implementation Note:
- Python lists make stack implementation trivial
- We leverage the dynamic array operations we studied earlier
- append() = pushback() from our dynamic array
- pop() removes and returns last element
- This is why stacks are often taught alongside arrays
"""


class Stack:
    """
    A stack implementation using Python's built-in list (dynamic array).
    
    This demonstrates that stacks are a conceptual abstraction built on
    top of arrays, restricting access to LIFO (Last In First Out) operations.
    """
    
    def __init__(self):
        """
        Initialize an empty stack using a Python list.
        
        The list serves as our underlying dynamic array, giving us
        O(1) append and pop operations at the end.
        """
        self.stack = []  # Empty list serves as the stack

    def push(self, n):
        """
        Push an element onto the top of the stack.
        
        Time Complexity: O(1) amortized - uses list.append()
        Space Complexity: O(1) - just adding one element
        
        Args:
            n: int - value to push onto the stack
            
        Note:
            This is equivalent to pushback() from our dynamic array.
            The "top" of the stack is the end of the array (highest index).
        """
        self.stack.append(n)  # Add element to end of list (top of stack)

    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Time Complexity: O(1) - removes from end of list
        Space Complexity: O(1) - no additional space needed
        
        Returns:
            The value that was at the top of the stack
            
        Note:
            list.pop() without arguments removes from the end.
            This operation both removes AND returns the value.
            Will raise IndexError if stack is empty (no bounds checking here).
            
        Important:
            This is equivalent to popback() + get() from our dynamic array.
            Unlike popback() which just decremented length, list.pop()
            actually returns the removed value.
        """
        return self.stack.pop()  # Remove and return last element (top of stack)