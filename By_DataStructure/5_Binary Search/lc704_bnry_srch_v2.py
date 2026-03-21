"""
Binary Search Implementation (LeetCode Style)

Problem: LeetCode 704 - Binary Search
Pattern: Divide and Conquer (Iterative)
Concept: Standard Binary Search

Problem Statement:
- Given a sorted array of integers nums and a target value
- Return the index of target if it exists in nums
- Return -1 if target does not exist
- Must implement in O(log n) time complexity

This is the classic, standard binary search algorithm - foundational for:
- Many coding interview problems
- More complex variations (rotated arrays, search ranges, etc.)
- Understanding divide-and-conquer paradigm
- Building blocks for more advanced algorithms

Algorithm Overview:
- Repeatedly divide search space in half
- Compare target with middle element
- Eliminate half of remaining elements based on comparison
- Continue until target found or search space exhausted

Key Characteristics:
- Works ONLY on sorted arrays (ascending order in this case)
- O(log n) time complexity - extremely efficient
- O(1) space complexity - only uses pointers
- Returns single index (not first/last if duplicates exist)

Example Walkthrough for nums = [-1, 0, 3, 5, 9, 12], target = 9:
    
    Step 1: L=0, R=5, mid=2
    nums = [-1, 0, 3, 5, 9, 12]
            L     mid      R
    nums[mid] = 3, target (9) > 3
    Search right: L = mid + 1 = 3
    
    Step 2: L=3, R=5, mid=4
    nums = [-1, 0, 3, 5, 9, 12]
                     L  mid R
    nums[mid] = 9, target (9) == 9
    Found! Return mid = 4

Example Walkthrough for nums = [-1, 0, 3, 5, 9, 12], target = 2:
    
    Step 1: L=0, R=5, mid=2
    nums = [-1, 0, 3, 5, 9, 12]
            L     mid      R
    nums[mid] = 3, target (2) < 3
    Search left: R = mid - 1 = 1
    
    Step 2: L=0, R=1, mid=0
    nums = [-1, 0, 3, 5, 9, 12]
            L
            mid
               R
    nums[mid] = -1, target (2) > -1
    Search right: L = mid + 1 = 1
    
    Step 3: L=1, R=1, mid=1
    nums = [-1, 0, 3, 5, 9, 12]
                L
                mid
                R
    nums[mid] = 0, target (2) > 0
    Search right: L = mid + 1 = 2
    
    Now L > R (2 > 1), exit loop
    Return -1 (not found)

Time Complexity: O(log n)
- Each iteration reduces search space by half
- For array of size n, need at most log₂(n) iterations
- Example: n = 1,000,000 → only ~20 iterations maximum!

Space Complexity: O(1)
- Only uses three variables: L, R, mid
- No additional data structures or recursion
- Constant space regardless of input size

Why This Implementation Works:
- Loop invariant: if target exists, it's always in range [L, R]
- Each iteration maintains this invariant by eliminating one half
- When L > R, we've checked all possible positions
- Three cases exhaustively cover all possibilities

Common Pitfalls (Avoided Here):
✓ Using (L + R) // 2 works in Python (no integer overflow)
  (In C++/Java, use L + (R - L) // 2 to avoid overflow)
✓ Correct loop condition: L <= R (not L < R)
✓ Correct boundary updates: L = mid + 1 and R = mid - 1 (not mid)
✓ Handles all edge cases: empty array, single element, not found

Interview Tips:
- Always clarify: is array sorted? Ascending or descending?
- Ask about duplicates: return any, first, or last occurrence?
- Confirm return value for not found (-1 is conventional)
- Consider: what if array is empty?
- Time/space constraints: O(log n) and O(1) are expected

Related LeetCode Problems:
- 34. Find First and Last Position (binary search variations)
- 33. Search in Rotated Sorted Array (binary search with twist)
- 35. Search Insert Position (modified binary search)
- 74. Search 2D Matrix (apply binary search concept)
- 153. Find Minimum in Rotated Sorted Array
"""


class Solution(object):
    def search(self, nums, target):
        """
        Search for a target value in a sorted array using binary search.
        
        Time Complexity: O(log n) where n = len(nums)
        Space Complexity: O(1) - only uses constant extra space
        
        Args:
            nums: List[int] - sorted array in ascending order
            target: int - value to search for
            
        Returns:
            int - index of target if found, -1 otherwise
            
        Preconditions:
            - nums is sorted in ascending order
            - -10^4 <= nums[i], target <= 10^4 (typical LeetCode constraint)
            
        Examples:
            nums = [-1, 0, 3, 5, 9, 12], target = 9
            Output: 4 (nums[4] = 9)
            
            nums = [-1, 0, 3, 5, 9, 12], target = 2
            Output: -1 (not in array)
            
        Edge Cases:
            - Empty array: Return -1 (L=0, R=-1, L > R immediately)
            - Single element: Works correctly
            - Target at boundaries: Works correctly
            - All elements equal: Returns any occurrence
            
        Algorithm:
            1. Set left pointer to start (0), right pointer to end (len-1)
            2. While search space exists (L <= R):
               a. Calculate middle index: mid = (L + R) // 2
               b. If target < nums[mid]: search left half (R = mid - 1)
               c. If target > nums[mid]: search right half (L = mid + 1)
               d. If target == nums[mid]: found, return mid
            3. If loop exits without finding: return -1
        """
        # Initialize pointers
        # L (left) points to start of search range
        # R (right) points to end of search range
        L, R = 0, len(nums) - 1 

        # Loop while there's a valid search space
        # Condition L <= R ensures we check even when L == R (single element)
        while L <= R:

            # Calculate mid - within loop:
            # Must recalculate each iteration as L and R change
            # Integer division gives us the middle index
            mid = (L+R)//2

            # Check 1: checking right half
            # If target is less than middle element,
            # target MUST be in left half (if it exists)
            # Eliminate right half by moving R to left of mid
            if target < nums[mid]:
                R = mid - 1  # New search range: [L, mid-1]

            # Check 2: checking left half
            # If target is greater than middle element,
            # target MUST be in right half (if it exists)
            # Eliminate left half by moving L to right of mid
            elif target > nums[mid]:
                L = mid + 1  # New search range: [mid+1, R]

            # Check 3: target equals middle element
            # Found the target! Return its index
            # This is the success case
            else:
                return mid  # Found at index mid
            
        # Exit with -1 if not found
        # If we reach here, L > R (search space exhausted)
        # Target does not exist in the array
        return -1  # Not found


if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    output1 = solver.search(nums=nums1, target=target1)
    print(output1) # Expected: 4

    # Test case 2: 
    solver = Solution()
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    output2 = solver.search(nums=nums2, target=target2)
    print(output2) # Expected: -1