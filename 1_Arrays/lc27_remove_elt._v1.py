from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # the left pointer doesn't exist for comparison, merely to track where to write to
        j = i
        while j < len(nums):
            if nums[j] != val:
                    nums[i] = nums[j]
                    i += 1 
                    j += 1 # if jth elt is valid, write it to ith position
            else:
                    j+=1 # if not, continue scanning for valid elts.

        return i


if __name__ == "__main__":
    solver = Solution()
    nums1 = [3,2,2,3]
    val1 = 3
    output1 = solver.removeElement(nums=nums1, val=val1)
    print(output1)

    solver = Solution()
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    output2 = solver.removeElement(nums=nums2, val=val2)
    print(output2)

