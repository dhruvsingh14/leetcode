from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        INCORRECT APPROACH - Using set() to remove duplicates
        
        Problem: LeetCode 26 - Remove Duplicates from Sorted Array
        
        WHY THIS APPROACH IS WRONG:
        
        1. **Loses Sorted Order** (CRITICAL FAILURE)
           - set() is unordered in Python < 3.7, and even in 3.7+ it maintains
             insertion order, but converting back loses the original sorted order
           - Example: nums = [0,0,1,1,1,2,2,3,3,4]
           - After set: could become [0,1,2,3,4] OR [0,2,1,4,3] (order not guaranteed)
           - Problem explicitly requires: "relative order should be kept the same"
           - Judge expects: nums = [0,1,2,3,4,_,_,_,_,_] in SORTED order
        
        2. **Space Complexity Violation**
           - Creates new list with O(n) extra space: nums_deduped = list(set(nums))
           - Problem requires O(1) space complexity (in-place modification)
           - "Remove duplicates in-place" means no additional data structures
        
        3. **Not Demonstrating Algorithm Skills**
           - This is a "gotcha" solution that bypasses the learning objective
           - Interview goal: demonstrate understanding of two-pointer technique
           - Using built-in functions shows lack of algorithmic thinking
        
        WHAT SHOULD BE IMPROVED:
        
        1. Use two-pointer technique (slow/fast pointers) for O(1) space
        2. Leverage the fact that array is ALREADY SORTED
           - Only need to compare adjacent elements
           - No need to check entire array for duplicates
        3. Modify array in-place without creating new data structures
        4. Maintain sorted order throughout the process
        
        CORRECT APPROACH:
        See the two-pointer solution which:
        - Maintains sorted order ✓
        - Uses O(1) space ✓
        - Demonstrates algorithmic thinking ✓
        - Time complexity O(n) - same as this approach
        """

        nums_deduped = list(set(nums)) # Creates new list - O(n) space violation

        nums[:] = nums_deduped # Loses sorted order - will fail judge's assertions

        return len(nums_deduped)


if __name__ == "__main__":
    solver = Solution()
    nums1 = [1, 1, 2]
    output1 = solver.removeDuplicates(nums=nums1)
    print(output1)
    print(f"nums1 after: {nums1}")  # Will show unsorted result

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    output2 = solver.removeDuplicates(nums=nums2)
    print(output2)
    print(f"nums2 after: {nums2}")  # Will show unsorted result - FAILS requirement

