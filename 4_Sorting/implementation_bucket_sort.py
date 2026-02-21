"""
Bucket Sort (Counting Sort) Implementation

Pattern: Non-Comparison Based Sorting
Concept: Bucket Sort / Counting Sort

How This Algorithm Works:
1. Count the frequency of each unique value in the array
2. Use the counts to determine final positions
3. Overwrite original array with sorted values

Key Insight:
- When the range of values is small and known (here: 0, 1, 2), we can
  sort WITHOUT comparing elements!
- Just count occurrences and reconstruct the array in order
- This breaks the O(n log n) lower bound for comparison-based sorts

Algorithm Visualization for [2, 1, 2, 0, 1, 2]:
    
    Step 1 - Count occurrences:
    Input: [2, 1, 2, 0, 1, 2]
    counts[0] = 1  (one 0)
    counts[1] = 2  (two 1s)
    counts[2] = 3  (three 2s)
    
    Step 2 - Reconstruct array:
    Write 1 zero:  [0, _, _, _, _, _]
    Write 2 ones:  [0, 1, 1, _, _, _]
    Write 3 twos:  [0, 1, 1, 2, 2, 2]
    
    Final: [0, 1, 1, 2, 2, 2]

Why This Is Called "Bucket Sort":
- Conceptually, we have one "bucket" for each unique value (0, 1, 2)
- Each element goes into its corresponding bucket
- Then we dump the buckets back in order
- More generally, bucket sort divides range into buckets and sorts within each

Counting Sort vs Bucket Sort:
- Counting Sort: One bucket per unique value, just count and reconstruct
- Bucket Sort (general): Divide range into buckets, sort within each bucket
- This implementation is technically counting sort (special case)

Time Complexity: O(n + k) where k is the range of values
- O(n) to count all elements
- O(k) to iterate through counts (here k=3)
- In this case: O(n + 3) = O(n) linear time!
- This is FASTER than comparison sorts' O(n log n) lower bound!

Space Complexity: O(k) where k is the range of values
- Need array to store counts (here: size 3)
- Sorts in-place by overwriting original array
- Only extra space is the counts array

When to Use Bucket/Counting Sort:
✓ Small, known range of integer values (like 0-9, 0-100)
✓ Need O(n) time complexity (faster than O(n log n))
✓ Values are non-negative integers (or can be mapped to them)
✓ Stable sort needed and you implement it carefully

When NOT to Use:
✗ Large range of values (space becomes prohibitive)
✗ Floating point numbers (would need rounding/bucketing)
✗ Unknown range (need to find min/max first)
✗ Sparse data (many possible values, few actual values)
✗ Need in-place sort with O(1) space (this needs O(k) space)

Comparison to Other Sorts:
- Comparison sorts (merge, quick, heap): O(n log n), work on any comparable data
- Counting sort: O(n + k), only for small integer ranges
- Radix sort: O(d * n), sorts by digit, uses counting sort as subroutine
- Bucket sort (general): O(n + k), distributes into buckets then sorts each

Properties:
- Stable: Can be made stable with careful implementation
- In-place: No (overwrites array but needs counts array)
- Adaptive: No (always does same work regardless of input order)
- Non-comparison based: Yes (uses array indexing, not comparisons)

Real-World Applications:
- Sorting ages, grades, or other bounded integers
- Dutch National Flag problem (sort 0s, 1s, 2s) - this exact use case!
- Histogram creation
- As subroutine in radix sort
- Any situation with small integer range

Dutch National Flag Problem:
- This is a famous problem by Dijkstra
- Sort an array of 0s, 1s, and 2s (like the Dutch flag colors)
- This counting sort approach is perfect for it!
- Alternative: two-pointer in-place approach (O(n) time, O(1) space)

Limitations:
- Only works for integers (or values that can be mapped to integers)
- Range must be reasonable (can't sort [1, 1000000] efficiently)
- Not suitable as a general-purpose sort
- Specialized tool for specific scenarios

Extension to Larger Ranges:
- For larger k, this becomes inefficient (space and time for O(k))
- Could use hash map instead of array (only store counts for values present)
- Or use general bucket sort (divide range into buckets, sort within each)
"""


def bucketSort(arr):
    """
    Sort an array containing only values 0, 1, and 2 using counting sort.
    
    Time Complexity: O(n) - linear time!
    Space Complexity: O(1) - only uses 3 fixed-size buckets
    
    Args:
        arr: list - array containing only 0, 1, and 2 (modified in-place)
        
    Returns:
        list - the sorted array (same reference as input)
        
    Algorithm:
        1. Count occurrences of each value (0, 1, 2) in the array
        2. Overwrite original array with sorted values based on counts
        3. Write all 0s first, then all 1s, then all 2s
                
    Why This Works:
        - We know exactly what values exist (0, 1, 2)
        - Counting tells us how many of each
        - We can directly place them in sorted order
        
    Why This Is Fast:
        - No comparisons needed (non-comparison based sort)
        - Direct placement using counts
        - Breaks the O(n log n) lower bound for comparison sorts
        
    Assumptions:
        - Array only contains values 0, 1, and 2
        - If other values present, this will fail or produce wrong results
        
    Use Cases:
        - Dutch National Flag problem (Dijkstra)
        - Sorting small bounded integers
        - Any 3-value categorization problem
        
    Note:
        - This is a special case of counting sort
        - For general values, would need to find range first
        - For larger ranges, might need different approach
    """
    # Assuming arr only contains 0, 1 or 2
    # Create buckets to count occurrences of each value
    # counts[0] = how many 0s, counts[1] = how many 1s, counts[2] = how many 2s
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    # For each element, increment the corresponding bucket
    # This is the "counting" phase
    for n in arr:
        counts[n] += 1  # Use value as index: arr[0], arr[1], or arr[2]
    
    # Fill each bucket in the original array
    # Now reconstruct the sorted array using the counts
    # i tracks our position in the original array
    i = 0
    
    # For each possible value (0, 1, 2)
    for n in range(len(counts)):
        # Write that value 'counts[n]' times
        # j goes from 0 to counts[n]-1
        for j in range(counts[n]):
            arr[i] = n  # Write the value n into array
            i += 1  # Move to next position
            
    # After this:
    # - All 0s are written first (counts[0] times)
    # - All 1s are written next (counts[1] times)
    # - All 2s are written last (counts[2] times)
    # Result: sorted array!
    
    return arr