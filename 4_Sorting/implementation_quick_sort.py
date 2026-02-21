"""
Quick Sort Implementation

Pattern: Divide and Conquer + Recursion + Partitioning
Concept: Quick Sort (One of the Fastest Sorting Algorithms in Practice)

How Quick Sort Works:
1. Pick a "pivot" element from the array (here: last element)
2. Partition: rearrange array so elements < pivot are on left, >= pivot on right
3. Recursively apply quick sort to left and right partitions
4. No merge step needed - partitioning does the work in-place!

Key Insight:
- After partitioning, the pivot is in its FINAL sorted position
- All elements to the left are smaller, all to the right are larger
- Recursively sort the two partitions independently

Algorithm Visualization for [3, 7, 8, 5, 2, 1, 9]:
    
    Initial: [3, 7, 8, 5, 2, 1, 9]  pivot = 9
    Partition: [3, 7, 8, 5, 2, 1] [9] (all < 9, pivot in final position)
    
    Left side: [3, 7, 8, 5, 2, 1]  pivot = 1
    Partition: [1] [3, 7, 8, 5, 2] (1 in final position)
    
    Right side: [3, 7, 8, 5, 2]  pivot = 2
    Partition: [2] [3, 7, 8, 5] (2 in final position)
    
    Right side: [3, 7, 8, 5]  pivot = 5
    Partition: [3] [5] [7, 8] (3 and 5 in final positions)
    
    Right side: [7, 8]  pivot = 8
    Partition: [7] [8] (both in final positions)
    
    Final: [1, 2, 3, 5, 7, 8, 9]

Partitioning Example for [3, 7, 8, 5, 2, 1] with pivot = 1:
    Start:       [3, 7, 8, 5, 2, 1]  left=0, pivot=1
                  ^              ^
                  left           pivot
    
    i=0: 3 >= 1, skip
    i=1: 7 >= 1, skip
    i=2: 8 >= 1, skip
    i=3: 5 >= 1, skip
    i=4: 2 >= 1, skip
    
    After partition: [3, 7, 8, 5, 2, 1]  swap pivot to left position (0)
                     [1, 7, 8, 5, 2, 3]
                      ^
                      pivot in final position!

Time Complexity:
- Best case: O(n log n) - pivot always splits array roughly in half
- Average case: O(n log n) - random pivots tend to split reasonably
- Worst case: O(n²) - pivot is always smallest/largest (already sorted array!)
- Average case is common in practice (why it's often fastest)

Space Complexity:
- O(log n) - recursion call stack in average case
- O(n) - worst case recursion depth (unbalanced partitions)
- In-place: Yes (only uses recursion stack, no auxiliary arrays like merge sort)

Pivot Selection Strategies:
- Last element (this implementation): Simple but poor for sorted data
- First element: Same issue
- Random element: Better average case, avoids worst case on sorted data
- Median-of-three: Pick median of first, middle, last (more robust)
- The choice of pivot significantly affects performance!

When to Use Quick Sort:
✓ Large datasets (O(n log n) average is very fast in practice)
✓ When in-place sorting is needed (no extra memory)
✓ Average-case performance matters more than worst-case
✓ Cache-friendly operations (better locality than merge sort)

When NOT to Use:
✗ When worst-case O(n log n) is required (use merge sort or heap sort)
✗ When stable sort is needed (quick sort is not stable)
✗ Already sorted or nearly sorted data with naive pivot (degrades to O(n²))
✗ Small arrays (insertion sort is faster)

Comparison to Other Sorts:
- Merge Sort: O(n log n) always, but needs O(n) space, stable
- Quick Sort: O(n log n) average, in-place, NOT stable, can degrade to O(n²)
- Heap Sort: O(n log n) always, in-place, NOT stable, slower constant factors
- Quick sort is fastest in practice due to good cache performance

Properties:
- Stable: No (equal elements may swap positions)
- In-place: Yes (only recursion stack, no auxiliary arrays)
- Adaptive: No (doesn't take advantage of existing order with naive pivot)
- Comparison-based: Yes

Real-World Uses:
- C's qsort() library function
- Java's Arrays.sort() for primitives (uses dual-pivot quick sort)
- Many language standard libraries use hybrid approaches (quick + insertion)
- Still one of the most used sorting algorithms in practice

Quick Sort vs Merge Sort:
- Quick Sort: Faster in practice (better cache, in-place), but O(n²) worst case
- Merge Sort: Guaranteed O(n log n), stable, but needs O(n) space
- Choice depends on: memory constraints, stability needs, worst-case guarantees
"""


def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    """
    Sort an array using the quick sort algorithm (divide and conquer).
        
    Args:
        arr: list[int] - array to be sorted (modified in-place)
        s: int - start index of the portion to sort
        e: int - end index of the portion to sort (inclusive)
        
    Returns:
        list[int] - the sorted array (same reference as input)
        
    Algorithm:
        1. Base case: if subarray has 1 or 0 elements, already sorted
        2. Choose pivot (last element in this implementation)
        3. Partition array: elements < pivot on left, >= pivot on right
        4. Place pivot in its final sorted position
        5. Recursively quick sort left partition
        6. Recursively quick sort right partition
                
    Partitioning Strategy:
        - Use "left" pointer to track boundary between small and large elements
        - Scan array, swap small elements to left side
        - Finally, swap pivot into position between left and right partitions
        
        
    Why It Can Be Slow:
        - Choosing last element as pivot is bad for sorted arrays
        - Degrades to O(n²) when pivot is always min/max element
        - Solution: randomize pivot or use median-of-three
        
    Note:
        - NOT stable (equal elements may change relative order)
        - In-place sorting (only uses recursion stack)
        - Partition step does the heavy lifting (merge sort has separate merge)
    """
    # Base case: if subarray has 1 or fewer elements, it's already sorted
    # e - s + 1 gives the length of the current subarray
    if e - s + 1 <= 1:
        return arr
        
    # Choose pivot element (using last element in this implementation)
    # This is simple but can lead to O(n²) on already sorted arrays
    # Better strategies: random element, median-of-three
    pivot = arr[e]
    
    # Left pointer marks the boundary between small and large elements
    # Everything to the left of 'left' will be < pivot
    # Everything from 'left' to i will be >= pivot
    left = s  # pointer for left side
    
    # Partition: elements smaller than pivot on left side
    # Scan through array (excluding pivot at end)
    # Move elements < pivot to the left side by swapping
    for i in range(s, e):
        if arr[i] < pivot:  # Found element smaller than pivot
            # Swap arr[i] with arr[left] to move small element left
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1  # Expand the "small elements" region
            
    # Move pivot in-between left & right sides
    # At this point: arr[s..left-1] < pivot, arr[left..e-1] >= pivot
    # Swap pivot from end (arr[e]) to its final position (arr[left])
    arr[e] = arr[left]
    arr[left] = pivot
    # Now pivot is in its FINAL sorted position!
    # arr[s..left-1] < pivot < arr[left+1..e]
    
    # Quick sort left side
    # Sort elements smaller than pivot (from s to left-1)
    # These are all elements that ended up left of the pivot
    quickSort(arr, s, left - 1)
    
    # Quick sort right side
    # Sort elements greater than or equal to pivot (from left+1 to e)
    # These are all elements that ended up right of the pivot
    quickSort(arr, left + 1, e)
    
    # Return the sorted array (modified in-place)
    return arr