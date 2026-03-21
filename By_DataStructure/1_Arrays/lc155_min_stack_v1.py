from typing import List

class MinStack:
    """
    A stack data structure that supports O(1) retrieval of the minimum element.
    
    Problem: LeetCode 155 - Min Stack
    Pattern: Stack + Auxiliary Data (tracking extra state)
    
    Approach:
    - Store each element as a tuple: (value, minimum_at_this_point)
    - When pushing a new value, calculate and store the minimum up to that point
    - Each stack entry knows the minimum of all elements below it (and itself)
    - This allows O(1) getMin() by just checking the top element's minimum
    
    Key Insight:
    - Rather than searching the entire stack for minimum (O(n)), we pre-compute
      and store the minimum at each level as we build the stack
    - When we pop, the new top already has the correct minimum stored
    - Trade-off: O(n) extra space for O(1) getMin() time
    
    Time Complexity:
    - push(): O(1) - append to list and min of two values
    - pop(): O(1) - remove from end of list
    - top(): O(1) - access last element
    - getMin(): O(1) - access stored minimum in last element
    
    Space Complexity: O(n) - storing tuples instead of just values (2n space)
    
    Example state progression:
    push(-2): stack = [(-2, -2)]           # min so far is -2
    push(0):  stack = [(-2, -2), (0, -2)]  # min so far is still -2
    push(-3): stack = [(-2, -2), (0, -2), (-3, -3)]  # new min is -3
    pop():    stack = [(-2, -2), (0, -2)]  # back to min of -2
    """

    def __init__(self):
        """
        Initialize the MinStack with an empty stack.
        
        Each element in self.stack will be a tuple: (value, min_at_this_level)
        """
        self.stack = []  # Stack stores tuples of (value, current_minimum)

    def push(self, val: int) -> None:
        """
        Push a value onto the stack along with the current minimum.
        
        Args:
            val: int - value to push onto the stack
            
        Strategy:
        - If stack is empty, this value is the minimum
        - Otherwise, minimum is the smaller of: new value vs. previous minimum
        - Store both the value and the minimum as a tuple
        """
        if not self.stack: # Stack is empty, this is the first element
            curr_min = val # The only element is the minimum
        else: # Stack has elements, compare new value with previous minimum
            curr_min = min(val, self.stack[-1][1]) # stack[-1][1] is previous minimum
        self.stack.append((val, curr_min)) # Store tuple: (value, minimum_at_this_level)

    def pop(self) -> None:
        """
        Remove the top element from the stack.
        
        No need to update minimum since each remaining element already
        has the correct minimum stored in its tuple.
        """
        self.stack.pop() # Remove the top element (tuple)

    def top(self) -> int:
        """
        Get the top element's value without removing it.
        
        Returns:
            int - the value (not the minimum) at the top of the stack
        """
        return self.stack[-1][0] # Return first element of tuple (the value)

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack in O(1) time.
        
        Returns:
            int - the minimum value among all elements currently in the stack
        """
        return self.stack[-1][1] # Return second element of tuple (the minimum)


if __name__ == "__main__":
    # Test case from problem description
    obj = MinStack()

    val = -2
    obj.push(val) # Stack: [(-2, -2)]

    val = 0
    obj.push(val) # Stack: [(-2, -2), (0, -2)]

    val = -3
    obj.push(val) # Stack: [(-2, -2), (0, -2), (-3, -3)]

    print(obj.getMin()) # Expected: -3

    obj.pop() # Stack: [(-2, -2), (0, -2)]

    print(obj.top()) # Expected: 0

    print(obj.getMin()) # Expected: -2