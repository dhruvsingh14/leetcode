from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Create a new array that is the concatenation of the input array with itself.
        
        Problem: LeetCode 1929 - Concatenation of Array
        Pattern: Array Manipulation
        
        Approach:
        - Simply concatenate the array with itself using the + operator
        - Result has length 2n where ans[i] == nums[i] and ans[i+n] == nums[i]
        - This is the most Pythonic and straightforward solution
        
        Time Complexity: O(n) - must copy all n elements twice to create new array
        Space Complexity: O(n) - creating new array of size 2n (O(2n) = O(n))
        
        Args:
            nums: List[int] - input array of length n
            
        Returns:
            List[int] - concatenated array of length 2n
            
        Note:
            This problem tests basic array understanding and language features.
            Alternative approaches could use loops or list comprehension, but
            the + operator is the cleanest solution in Python.
        """

        return nums + nums


if __name__ == "__main__":
    # Test case 1: Array of length 3
    solver = Solution()
    nums1 = [1,2,1]
    output1 = solver.getConcatenation(nums=nums1)
    print(output1) # Expected: [1, 2, 1, 1, 2, 1]

    # Test case 2: Array of length 4
    solver = Solution()
    nums2 = [1,3,2,1]
    output2 = solver.getConcatenation(nums=nums2)
    print(output2) # Expected: [1, 3, 2, 1, 1, 3, 2, 1]



