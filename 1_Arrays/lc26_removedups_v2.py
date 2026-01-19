from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array in-place using two pointers.
        
        Problem: LeetCode 26 - Remove Duplicates from Sorted Array
        Pattern: Two Pointers (slow and fast pointer technique)
        
        Approach:
        - Use two pointers: i (slow / left) tracks position of last / most recent unique element
        - j (fast / right) scans through array looking for next unique element
        - When new unique element found, place it at i+1 and advance i
        - Array is modified in-place, only first k elements matter
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - only using two pointers, no extra space
        
        Args:
            nums: List[int] - sorted array in non-decreasing order
            
        Returns:
            int - number of unique elements (k)
            
        Note:
            The first k elements of nums will contain unique values in sorted order.
            Elements beyond index k-1 are ignored by the judge.
        """

        i = 0 # Slow pointer: tracks the position of the last unique element
        j = i+1 # Fast pointer: scans ahead to find next unique element

        while j < len(nums): # j scans entire array
            if nums[i] != nums[j]: # if ith, jth elements aren't equal, ensure they're adjacent
                nums[i+1] = nums[j]
                i+=1 # advance both pointers
                j+=1
            else:
                j+=1 # while scanning dup. seq. keep i fixed
                
        return i+1 # only returning the length of unique values, doesn't matter what comes after


if __name__ == "__main__":
    # Test case 1: Simple case with one duplicate
    solver = Solution()
    nums1 = [1, 1, 2]
    output1 = solver.removeDuplicates(nums=nums1)
    print(output1) # Expected: 2, nums1 = [1, 2, _]

    # Test case 2: Multiple duplicates of various numbers
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    output2 = solver.removeDuplicates(nums=nums2)
    print(output2) # Expected: 5, nums2 = [0, 1, 2, 3, 4, _, _, _, _, _]

