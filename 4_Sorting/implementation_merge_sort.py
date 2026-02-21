"""
Merge Sort Implementation

Pattern: Divide and Conquer + Recursion
Concept: Merge Sort (One of the Most Efficient General-Purpose Sorting Algorithms)

How Merge Sort Works:
1. Divide: Recursively split the array in half until you have subarrays of size 1
2. Conquer: Single elements are trivially sorted
3. Combine: Merge the sorted subarrays back together in sorted order

Key Insight:
- Merging two sorted arrays into one sorted array is easy and efficient (O(n))
- By recursively breaking down the problem, we reduce sorting to just merging

Algorithm Visualization for [38, 27, 43, 3]:
    
    Level 0 (Split):     [38, 27, 43, 3]
                        /              \
    Level 1 (Split):  [38, 27]        [43, 3]
                      /     \          /     \
    Level 2 (Base): [38]   [27]     [43]   [3]
                      \     /          \     /
    Level 1 (Merge): [27, 38]        [3, 43]
                        \              /
    Level 0 (Merge):   [3, 27, 38, 43]

Recursion Tree Structure:
    - Height of tree: log₂(n) levels
    - Work at each level: O(n) for merging
    - Total work: O(n) × O(log n) = O(n log n)

Time Complexity:
- Best case: O(n log n) - always splits and merges the same way
- Average case: O(n log n)
- Worst case: O(n log n) - guaranteed! Unlike quicksort
- Always O(n log n) regardless of input (very predictable)

Space Complexity:
- O(n) - needs temporary arrays for merging
- Not in-place (requires extra memory)
- Can be optimized but still needs O(n) space

When to Use Merge Sort:
✓ Large datasets where O(n log n) is guaranteed
✓ When stable sort is required (maintains relative order)
✓ External sorting (data doesn't fit in memory)
✓ Linked lists (can be done in-place on linked lists!)
✓ When worst-case O(n log n) is critical

When NOT to Use:
✗ Space is severely limited (needs O(n) extra space)
✗ Small arrays (insertion sort is faster)
✗ When in-place sorting is required (use heap sort or quick sort)

Comparison to Other Sorts:
- Quick Sort: O(n log n) average, but O(n²) worst; in-place; not stable
- Heap Sort: O(n log n) always; in-place; not stable
- Merge Sort: O(n log n) always; NOT in-place; stable
- Insertion Sort: O(n²) but better for small/nearly-sorted arrays

Properties:
- Stable: Yes (equal elements maintain relative order)
- In-place: No (requires O(n) auxiliary space)
- Adaptive: No (always does same work regardless of input order)
- Comparison-based: Yes

Real-World Uses:
- Python's sorted() and list.sort() use Timsort (hybrid of merge + insertion)
- External sorting (sorting large files that don't fit in RAM)
- Sorting linked lists (where it CAN be in-place)
- As part of more complex algorithms
"""


def mergeSort(arr, s, e):
    """
    Sort an array using the merge sort algorithm (divide and conquer).
       
    Args:
        arr: list - array to be sorted (modified in-place)
        s: int - start index of the portion to sort
        e: int - end index of the portion to sort (inclusive)
        
    Returns:
        list - the sorted array (same reference as input)
        
    Algorithm:
        1. Base case: if subarray has 1 or 0 elements, it's already sorted
        2. Find middle point to divide array into two halves
        3. Recursively sort the left half
        4. Recursively sort the right half
        5. Merge the two sorted halves
        
    Example:
        arr = [38, 27, 43, 3, 9, 82, 10]
        mergeSort(arr, 0, len(arr) - 1)
        # arr is now [3, 9, 10, 27, 38, 43, 82]
        
    Recursion Tree for [38, 27, 43, 3]:
        mergeSort([38,27,43,3], 0, 3)
        ├── mergeSort([38,27], 0, 1)
        │   ├── mergeSort([38], 0, 0) → returns [38]
        │   ├── mergeSort([27], 1, 1) → returns [27]
        │   └── merge → [27, 38]
        ├── mergeSort([43,3], 2, 3)
        │   ├── mergeSort([43], 2, 2) → returns [43]
        │   ├── mergeSort([3], 3, 3) → returns [3]
        │   └── merge → [3, 43]
        └── merge → [3, 27, 38, 43]
        
    """
    # Base case: if subarray has 1 or fewer elements, it's already sorted
    # e - s + 1 gives the length of the current subarray
    # A single element (or empty array) is trivially sorted
    if e - s + 1 <= 1:
        return arr

    # The middle index of the array
    # This splits the array into two roughly equal halves
    # Using integer division to get the midpoint
    m = (s + e) // 2

    # Sort the left half
    # Recursively sort from start (s) to middle (m)
    # This will keep dividing until we hit base case
    mergeSort(arr, s, m)

    # Sort the right half
    # Recursively sort from middle+1 (m+1) to end (e)
    # This will keep dividing until we hit base case
    mergeSort(arr, m + 1, e)

    # Merge sorted halfs
    # At this point, both halves are sorted
    # Now combine them into a single sorted array
    merge(arr, s, m, e)
    
    # Return the sorted array (modified in-place)
    return arr


def merge(arr, s, m, e):
    """
    Merge two sorted subarrays into a single sorted subarray.
    
    Time Complexity: O(n) where n = e - s + 1 (length of subarray)
    Space Complexity: O(n) - creates temporary arrays L and R
    
    Args:
        arr: list - the array containing both sorted subarrays
        s: int - start index of first sorted subarray
        m: int - end index of first sorted subarray (middle)
        e: int - end index of second sorted subarray
        
    Structure:
        arr[s..m] is sorted (left half)
        arr[m+1..e] is sorted (right half)
        After merge: arr[s..e] is sorted
        
    Algorithm:
        1. Copy left and right subarrays to temporary arrays
        2. Use three pointers (i for L, j for R, k for arr)
        3. Compare elements from L and R, place smaller one in arr
        4. After one array is exhausted, copy remaining elements
        
    Example:
        arr = [27, 38, 3, 43, ...]  (after sorting left and right halves)
               s    m  m+1  e
        L = [27, 38]
        R = [3, 43]
        
        Merge steps:
        1. Compare 27 vs 3 → place 3: [3, 38, 3, 43]
        2. Compare 27 vs 43 → place 27: [3, 27, 3, 43]
        3. Compare 38 vs 43 → place 38: [3, 27, 38, 43]
        4. R exhausted, place 43: [3, 27, 38, 43]
        
    Note:
        - This is the "combine" step in divide-and-conquer
        - Merging two sorted arrays is linear time
        - Stable: if L[i] == R[j], we take from L first (using <=)
    """
    # Copy the sorted left & right halfs to temp arrays
    # L contains elements from start to middle (inclusive)
    # R contains elements from middle+1 to end (inclusive)
    # These are copies, so we can safely overwrite arr
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0  # index for L (left temporary array)
    j = 0  # index for R (right temporary array)
    k = s  # index for arr (position in original array where we write)

    # Merge the two sorted halfs into the original array
    # While both temporary arrays have elements remaining
    # Compare front elements and place smaller one in arr
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:  # Left element is smaller or equal (stable sort)
            arr[k] = L[i]  # Place left element in arr
            i += 1  # Move to next element in L
        else:  # Right element is smaller
            arr[k] = R[j]  # Place right element in arr
            j += 1  # Move to next element in R
        k += 1  # Move to next position in arr

    # One of the halfs will have elements remaining
    # Copy any remaining elements from L (if j exhausted R first)
    while i < len(L):
        arr[k] = L[i]  # Copy remaining left elements
        i += 1
        k += 1
        
    # Copy any remaining elements from R (if i exhausted L first)
    while j < len(R):
        arr[k] = R[j]  # Copy remaining right elements
        j += 1
        k += 1