"""
Static Array Implementation - Fundamental Data Structure Operations

Pattern: Array Manipulation
Concept: Static Arrays (Fixed-Size Arrays)

Key Characteristics of Static Arrays:
- Fixed size allocated upfront (capacity)
- Contiguous memory allocation
- O(1) random access by index
- Cannot grow or shrink - size is predetermined
- Must track both 'capacity' (total size) and 'length' (elements in use)

Important Distinction:
- capacity: Total allocated memory/slots in the array
- length: Number of actual elements currently stored

Why This Matters:
- Understanding static arrays is fundamental to understanding dynamic arrays (lists)
- Many languages (C, Java) use static arrays by default
- Python lists are dynamic arrays built on top of this concept
- Interview questions often test understanding of these operations' complexities

Operations Time Complexity:
- insertEnd(): O(1) - constant time if space available
- removeEnd(): O(1) - constant time
- insertMiddle(): O(n) - must shift n elements
- removeMiddle(): O(n) - must shift n elements
- Access by index: O(1) - not shown but fundamental property
"""


def insertEnd(arr, n, length, capacity):
    """
    Insert an element at the next available position (end of array).
    
    Time Complexity: O(1) - constant time operation
    Space Complexity: O(1) - no additional space needed
    
    Args:
        arr: list - the static array
        n: int - value to insert
        length: int - current number of elements in use
        capacity: int - total size of the array
        
    Note:
        Only inserts if there's available space (length < capacity).
        Does nothing if array is full - a real implementation might raise an error.
    """
    if length < capacity:  # Check if there's space available
        arr[length] = n  # Insert at the next available position


def removeEnd(arr, length):
    """
    Remove the last element from the array.
    
    Time Complexity: O(1) - constant time operation
    Space Complexity: O(1) - no additional space needed
    
    Args:
        arr: list - the static array
        length: int - current number of elements in use
        
    Note:
        Sets the last element to 0 (default value).
        In practice, we would also decrement length to reflect removal.
        Does nothing if array is empty (length == 0).
    """
    if length > 0:  # Check if array is not empty
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0  # Reset to default value (could be any sentinel)


def insertMiddle(arr, i, n, length):
    """
    Insert an element at a specific index by shifting elements to the right.
    
    Time Complexity: O(n) - must shift up to n elements in worst case
    Space Complexity: O(1) - no additional space needed
    
    Args:
        arr: list - the static array
        i: int - index where element should be inserted
        n: int - value to insert
        length: int - current number of elements in use
        
    Strategy:
        1. Start from the end of the array (length - 1)
        2. Shift each element one position to the right
        3. Stop when we reach index i
        4. Insert the new value at index i
        
    Note:
        Assumes i is a valid index (0 <= i < length) and array has space.
        This is why insertMiddle is expensive - requires O(n) shifts.
    """
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):  # Iterate backwards from end to i to avoid overwriting
        arr[index + 1] = arr[index]  # Move each element one position right
    
    # Insert at i
    arr[i] = n  # Place the new value at the target index


def removeMiddle(arr, i, length):
    """
    Remove an element at a specific index by shifting elements to the left.
    
    Time Complexity: O(n) - must shift up to n elements in worst case
    Space Complexity: O(1) - no additional space needed
    
    Args:
        arr: list - the static array
        i: int - index of element to remove
        length: int - current number of elements in use
        
    Strategy:
        1. Start from index i + 1
        2. Shift each element one position to the left
        3. Continue until end of array
        4. Element at i is overwritten by element at i + 1
        
    Note:
        Assumes i is a valid index (0 <= i < length).
        No need to explicitly 'clear' arr[i] since it gets overwritten.
        This is why removeMiddle is expensive - requires O(n) shifts.
    """
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):  # Start from element after removal point
        arr[index - 1] = arr[index]  # Move each element one position left
    # No need to 'remove' arr[i], since we already shifted


def printArr(arr, capacity):
    """
    Print all elements in the array up to capacity.
    
    Time Complexity: O(n) - must print n elements
    Space Complexity: O(1) - no additional space needed
    
    Args:
        arr: list - the static array
        capacity: int - total size of array to print
        
    Note:
        Prints entire capacity, not just length.
        Will show both real values and default values (like 0s).
    """
    for i in range(capacity):  # Iterate through entire capacity
        print(arr[i])  # Print each element