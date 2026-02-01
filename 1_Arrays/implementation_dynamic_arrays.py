"""
Dynamic Array Implementation - How Python Lists Work Under the Hood

Pattern: Array Manipulation with Automatic Resizing
Concept: Dynamic Arrays (Resizable Arrays)

Key Characteristics of Dynamic Arrays:
- Start with initial capacity, automatically grow when full
- Double capacity when out of space (amortized O(1) insertions)
- Still contiguous memory, but can "relocate" to larger space
- Track both capacity (allocated space) and length (elements in use)
- This is how Python lists, Java ArrayLists, C++ vectors work internally

Why Doubling Strategy:
- Doubling capacity ensures amortized O(1) pushback operations
- If we only increased by 1 each time, we'd resize on every insert → O(n²)
- Doubling means we resize less frequently as array grows
- Trade-off: May waste up to 50% of allocated space

Operations Time Complexity:
- pushback(): O(1) amortized - O(n) worst case when resizing needed
- popback(): O(1) - just decrement length
- get(): O(1) - direct index access
- insert() [overwrite]: O(1) - direct index access
- resize(): O(n) - must copy all n elements

Space Complexity: O(n) where n is capacity (may be up to 2x length)

This vs Static Array:
- Static: Fixed size, faster, no resize overhead, but inflexible
- Dynamic: Flexible size, slight overhead, more practical for most uses
"""


class Array:
    """
    A dynamic array implementation that automatically resizes when full.
    
    This mimics the behavior of Python's built-in list, demonstrating
    how dynamic arrays grow to accommodate new elements.
    """
    
    def __init__(self):
        """
        Initialize a dynamic array with initial capacity of 2.
        
        Starting small to demonstrate the resizing mechanism.
        In practice, implementations often start with capacity 8-16.
        """
        self.capacity = 2  # Total allocated space
        self.length = 0  # Number of elements currently stored
        self.arr = [0] * 2  # Array of capacity = 2, initialized with zeros

    def pushback(self, n):
        """
        Insert an element at the end of the array (append operation).
        
        Time Complexity: O(1) amortized - O(n) only when resizing
        Space Complexity: O(1) normally, O(n) during resize
        
        Args:
            n: int - value to insert at the end
            
        Strategy:
            1. Check if array is full (length == capacity)
            2. If full, double the capacity by resizing
            3. Insert element at next available position
            4. Increment length
            
        Note:
            Although resize is O(n), it happens infrequently enough that
            the amortized cost per insertion is O(1).
        """
        if self.length == self.capacity:  # Array is full, need more space
            self.resize()  # Double the capacity
            
        # insert at next empty position
        self.arr[self.length] = n  # Place element at end
        self.length += 1  # Increment count of elements

    def resize(self):
        """
        Double the array's capacity by creating a new larger array.
        
        Time Complexity: O(n) - must copy all n elements
        Space Complexity: O(n) - allocate new array of size 2n
        
        Strategy:
            1. Create new array with double the capacity
            2. Copy all existing elements to new array
            3. Update reference to point to new array
            4. Old array is garbage collected
            
        Note:
            This is called infrequently (only when full), so pushback
            remains O(1) amortized despite this O(n) operation.
        """
        # Create new array of double capacity
        self.capacity = 2 * self.capacity  # Double the capacity
        newArr = [0] * self.capacity  # Allocate new larger array
        
        # Copy elements to newArr
        for i in range(self.length):  # Copy only the elements in use
            newArr[i] = self.arr[i]  # Transfer each element
        self.arr = newArr  # Point to the new array (old array discarded)
        
    def popback(self):
        """
        Remove the last element from the array.
        
        Time Complexity: O(1) - just decrement length
        Space Complexity: O(1) - no additional space needed
        
        Note:
            Doesn't actually "delete" the element or resize down.
            Just decrements length so the element is considered removed.
            The value remains in memory but is inaccessible and will be
            overwritten on the next pushback.
        """
        if self.length > 0:  # Check array is not empty
            self.length -= 1  # Simply decrease the count (lazy deletion)
    
    def get(self, i):
        """
        Retrieve the value at a specific index.
        
        Time Complexity: O(1) - direct array access
        Space Complexity: O(1) - no additional space needed
        
        Args:
            i: int - index to retrieve
            
        Returns:
            Value at index i, or None if out of bounds
            
        Note:
            Only allows access to valid indices (i < length).
            Doesn't allow access to allocated but unused capacity.
        """
        if i < self.length:  # Check if index is within valid range
            return self.arr[i]  # Return value at index
        # Here we would throw an out of bounds exception

    def insert(self, i, n):
        """
        Overwrite the value at a specific index (not insert-and-shift).
        
        Time Complexity: O(1) - direct array access
        Space Complexity: O(1) - no additional space needed
        
        Args:
            i: int - index to overwrite
            n: int - new value
            
        Note:
            This is "insert" by overwriting, not by shifting elements.
            Only works for valid indices (i < length).
            For true insertion with shifting, see static array insertMiddle().
        """
        if i < self.length:  # Check if index is within valid range
            self.arr[i] = n  # Overwrite the value at index i
            return
        # Here we would throw an out of bounds exception       

    def print(self):
        """
        Print all elements currently in the array (up to length).
        
        Time Complexity: O(n) - must print n elements
        Space Complexity: O(1) - no additional space needed
        
        Note:
            Only prints elements in use (up to length), not entire capacity.
            This is different from the static array print which printed capacity.
        """
        for i in range(self.length):  # Iterate only through elements in use
            print(self.arr[i])  # Print each element
        print()  # Empty line for formatting