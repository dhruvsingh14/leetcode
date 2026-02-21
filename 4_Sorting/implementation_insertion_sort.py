"""
Insertion Sort Implementation

Pattern: Sorting Algorithm (Comparison-based)
Concept: Insertion Sort

How Insertion Sort Works:
- Build the sorted array one element at a time
- Take each element and insert it into its correct position in the sorted portion
- Like sorting a hand of playing cards: pick up cards one by one and insert each into the correct position

Algorithm Steps:
1. Start with the second element (index 1) - consider first element already sorted
2. Compare it with elements in the sorted portion (to its left)
3. Shift larger elements one position to the right
4. Insert the current element in its correct position
5. Repeat for all elements

Visual Example for [5, 2, 4, 6, 1, 3]:
    Initial: [5, 2, 4, 6, 1, 3]
             ^ sorted portion
    
    i=1, key=2: [5, 2, 4, 6, 1, 3] → [2, 5, 4, 6, 1, 3]
                ^^ sorted portion
    
    i=2, key=4: [2, 5, 4, 6, 1, 3] → [2, 4, 5, 6, 1, 3]
                ^^^^^ sorted portion
    
    i=3, key=6: [2, 4, 5, 6, 1, 3] → [2, 4, 5, 6, 1, 3] (already in place)
                ^^^^^^^ sorted portion
    
    i=4, key=1: [2, 4, 5, 6, 1, 3] → [1, 2, 4, 5, 6, 3]
                ^^^^^^^^^ sorted portion
    
    i=5, key=3: [1, 2, 4, 5, 6, 3] → [1, 2, 3, 4, 5, 6]
                ^^^^^^^^^^^^ sorted (done!)

Time Complexity:
- Best case: O(n) - array already sorted, just one comparison per element
- Average case: O(n²) - random order, roughly n²/4 comparisons and swaps
- Worst case: O(n²) - array sorted in reverse, maximum comparisons and swaps

Space Complexity: O(1) - in-place sorting, only uses constant extra space (tmp variable)

When to Use Insertion Sort:
✓ Small datasets (n < 10-20)
✓ Nearly sorted data (very efficient, approaches O(n))
✓ Online sorting (can sort data as it arrives)
✓ Simple implementation needed
✓ Stable sort required (maintains relative order of equal elements)

When NOT to Use:
✗ Large datasets (use merge sort, quick sort, or heap sort)
✗ Performance critical applications with random data
✗ Already have access to built-in sort functions

Comparison to Other Sorts:
- Bubble Sort: O(n²) but more swaps, simpler but less efficient
- Selection Sort: O(n²) but fewer swaps, not stable
- Merge Sort: O(n log n) but O(n) space, better for large data
- Quick Sort: O(n log n) average, but O(n²) worst case, not stable
- Insertion Sort: Good for small/nearly-sorted data, stable, in-place

Properties:
- Stable: Yes (equal elements maintain their relative order)
- In-place: Yes (only O(1) extra space)
- Adaptive: Yes (faster on nearly sorted data)
- Online: Yes (can sort data as it arrives)

Real-World Uses:
- Used in hybrid sorts (Timsort uses it for small subarrays)
- Used in practice for small arrays in library implementations
- Good for maintaining a sorted list as new elements arrive
"""


def insertionSort(arr):
    """
    Sort an array in ascending order using insertion sort algorithm.
       
    Args:
        arr: list - array to be sorted (modified in-place)
        
    Returns:
        list - the sorted array (same reference as input)
                
    Invariant:
        At the start of iteration i, elements arr[0..i-1] are in sorted order
        (though not necessarily in their final positions)
        
    Note:
        - Modifies the array in-place
        - Stable sort (maintains relative order of equal elements)
        - Efficient for small or nearly-sorted arrays
        - Inefficient for large random arrays
    """
    # Traverse through 1 to len(arr)
    # Start at index 1 because single element (index 0) is trivially sorted
    for i in range(1, len(arr)):
        # j points to the element just before the current element
        # We'll compare arr[j+1] (current element) with arr[j] and work backwards
        j = i - 1
        
        # While we haven't reached the beginning AND current element is smaller than predecessor
        # This loop shifts larger elements one position to the right
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            # Swap using temporary variable (classic three-step swap)
            tmp = arr[j + 1]  # Save the smaller element (current element being inserted)
            arr[j + 1] = arr[j]  # Move the larger element one position right
            arr[j] = tmp  # Place the smaller element in the now-empty position
            
            # Move j backwards to continue comparing with earlier elements
            j -= 1  # Check next position to the left
            
    # Return the sorted array (though it's modified in-place, so this is optional)
    return arr