from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of a given value from an array in-place.
        
        Problem: LeetCode 27 - Remove Element
        Pattern: Two Pointers (write pointer technique)
        
        Approach:
        - Use two pointers: i (write position) and j (read position)
        - i tracks where to write the next valid (non-val) element
        - j scans through the entire array looking for valid elements
        - When a valid element is found (nums[j] != val), write it to position i
        - Order of remaining elements doesn't matter, only first k elements count
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - only using two pointers, no extra space
        
        Args:
            nums: List[int] - input array to modify in-place
            val: int - value to remove from the array
            
        Returns:
            int - number of elements not equal to val (k)
            
        Note:
            The first k elements of nums will contain all values != val.
            Elements beyond index k-1 are ignored. Order can be changed.
        """
        i = 0 # the left pointer doesn't exist for comparison, merely to track where to write to
        j = i # Right pointer: scans through array to find valid elements
        while j < len(nums): # Scan entire array with j
            if nums[j] != val: # Found a valid element (not equal to val)
                    nums[i] = nums[j] # Write valid element to position i
                    i += 1 # Advance write position
                    j += 1 # if jth elt is valid, write it to ith position
            else:
                    j+=1 # if not, continue scanning for valid elts.

        return i # i represents the count of valid elements


if __name__ == "__main__":
    # Test case 1: Remove all 3s from array
    solver = Solution()
    nums1 = [3,2,2,3]
    val1 = 3
    output1 = solver.removeElement(nums=nums1, val=val1)
    print(output1) # Expected: 2, nums1 = [2, 2, _, _]

    # Test case 2: Remove all 2s from array with multiple occurrences
    solver = Solution()
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    output2 = solver.removeElement(nums=nums2, val=val2)
    print(output2) # Expected: 5, nums2 = [0, 1, 3, 0, 4, _, _, _] (order may vary)

