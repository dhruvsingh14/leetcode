"""
Binary Search Implementation

Pattern: Divide and Conquer (Iterative Approach)
Concept: Binary Search

How Binary Search Works:
- Efficiently search for a target value in a SORTED array
- Repeatedly divide the search space in half
- Compare target with middle element
- Eliminate half of remaining elements each iteration
- Continue until target found or search space exhausted

Key Requirement: Array MUST be sorted!
- Binary search only works on sorted data
- If unsorted, must sort first (O(n log n)) or use linear search (O(n))

Algorithm Steps:
1. Set left pointer (L) to start, right pointer (R) to end
2. While search space exists (L <= R):
   a. Calculate middle index: mid = (L + R) // 2
   b. If target > arr[mid]: search right half (L = mid + 1)
   c. If target < arr[mid]: search left half (R = mid - 1)
   d. If target == arr[mid]: found! return mid
3. If loop exits, target not found, return -1

Visual Example - Searching for 6 in [1, 3, 3, 4, 5, 6, 7, 8]:
    
    Iteration 1:
    [1, 3, 3, 4, 5, 6, 7, 8]
     L        mid        R
    mid = 3, arr[3] = 4
    6 > 4, so search right half
    
    Iteration 2:
    [1, 3, 3, 4, 5, 6, 7, 8]
                 L  mid  R
    mid = 5, arr[5] = 6
    6 == 6, found! return 5

Visual Example - Searching for 2 (not in array):
    
    Iteration 1:
    [1, 3, 3, 4, 5, 6, 7, 8]
     L        mid        R
    mid = 3, arr[3] = 4
    2 < 4, so search left half
    
    Iteration 2:
    [1, 3, 3, 4, 5, 6, 7, 8]
     L  mid  R
    mid = 1, arr[1] = 3
    2 < 3, so search left half
    
    Iteration 3:
    [1, 3, 3, 4, 5, 6, 7, 8]
     L
     mid
     R
    mid = 0, arr[0] = 1
    2 > 1, so L = mid + 1 = 1
    Now L > R (1 > 0), exit loop
    Return -1 (not found)

Time Complexity: O(log n)
- Each iteration cuts search space in half
- After k iterations, search space = n / 2^k
- When search space = 1, we're done: n / 2^k = 1 → k = log₂(n)
- Extremely efficient! For n=1,000,000, only ~20 comparisons needed!

Space Complexity: O(1)
- Only uses a few variables (L, R, mid)
- Iterative approach (no recursion stack)
- Constant space regardless of input size

Comparison: Binary Search vs Linear Search:
- Linear Search: O(n) time, works on unsorted data
- Binary Search: O(log n) time, requires sorted data
- For n=1,000,000:
  - Linear: up to 1,000,000 comparisons
  - Binary: only ~20 comparisons!
- Trade-off: speed vs. requirement for sorted data

When to Use Binary Search:
✓ Searching in sorted array/list
✓ Large datasets (O(log n) is much faster than O(n))
✓ Multiple searches on same data (sort once, search many times)
✓ Finding insertion point for maintaining sorted order

When NOT to Use:
✗ Unsorted data (must sort first, might not be worth it for single search)
✗ Very small arrays (overhead not worth it, linear search is fine)
✗ Linked lists (no random access, can't efficiently find middle)
✗ Data structure doesn't support indexing

Properties:
- Requires: Sorted array with random access (indexing)
- Iterative vs Recursive: Both possible, iterative uses O(1) space
- Deterministic: Always same number of steps for given n
- Logarithmic: Extremely efficient scaling

Real-World Applications:
- Searching in databases (B-trees use binary search concept)
- Dictionary/spell-checker lookups
- Finding insertion position in sorted list
- Game tree search (alpha-beta pruning uses similar concept)
- System utilities (searching sorted log files)

Common Interview Variations:
- Find first/last occurrence of target (handle duplicates)
- Find insertion position (where to insert to maintain sorted order)
- Search in rotated sorted array
- Find peak element
- Search in 2D matrix
- Square root calculation (binary search on answer space)

Edge Cases to Handle:
- Empty array: L > R initially, return -1
- Single element: Works correctly
- Target not in array: Return -1
- Duplicates: Returns one occurrence (not necessarily first/last)
- Target at boundaries: L=0 or R=len-1

Binary Search Invariant:
- If target exists, it's always in range [L, R]
- After each iteration, this property is maintained
- When L > R, we've exhausted all possibilities
"""

# Example sorted array for demonstration
arr = [1, 3, 3, 4, 5, 6, 7, 8]


def binarySearch(arr, target):
    """
    Search for a target value in a sorted array using binary search.
      
    Args:
        arr: list - SORTED array of comparable elements
        target: comparable type - value to search for
        
    Returns:
        int - index of target if found, -1 if not found
        
    Precondition:
        arr must be sorted in ascending order
        
    Algorithm:
        1. Initialize left (L) and right (R) pointers
        2. While search space exists (L <= R):
           - Calculate middle index
           - If target is in right half, move L
           - If target is in left half, move R
           - If target equals middle, return index
        3. If not found, return -1
        
    Examples:
        arr = [1, 3, 3, 4, 5, 6, 7, 8]
        binarySearch(arr, 6) → 5
        binarySearch(arr, 2) → -1
        binarySearch(arr, 1) → 0
        binarySearch(arr, 8) → 7
        
    Why O(log n):
        - Each comparison eliminates half the search space
        - Search space: n → n/2 → n/4 → ... → 1
        - Number of steps = log₂(n)
        
    Note on Duplicates:
        - If array contains duplicates, returns AN index
        - Not guaranteed to be first or last occurrence
        - For first/last, need modified binary search
        
    Note:
        - This is the iterative implementation
        - Recursive version also possible but uses O(log n) stack space
        - Iterative preferred for space efficiency
    """
    # Initialize left and right pointers
    # L starts at beginning (index 0)
    # R starts at end (index len(arr) - 1)
    L, R = 0, len(arr) - 1

    # Continue searching while there's a valid search space
    # When L > R, we've exhausted all possibilities
    while L <= R:
        # Calculate middle index
        # Using integer division to get the midpoint
        # This avoids overflow issues compared to (L + R) / 2 in some languages
        mid = (L + R) // 2

        # Compare target with middle element to decide which half to search
        
        # Case 1: Target is greater than middle element
        # Target must be in the RIGHT half (if it exists)
        # Eliminate left half by moving L past mid
        if target > arr[mid]:
            L = mid + 1  # Search right half: [mid+1, R]
            
        # Case 2: Target is less than middle element
        # Target must be in the LEFT half (if it exists)
        # Eliminate right half by moving R before mid
        elif target < arr[mid]:
            R = mid - 1  # Search left half: [L, mid-1]
            
        # Case 3: Target equals middle element
        # Found the target! Return its index
        else:
            return mid  # Target found at index mid
    
    # If we exit the loop, L > R, meaning search space is exhausted
    # Target is not in the array
    return -1  # Target not found