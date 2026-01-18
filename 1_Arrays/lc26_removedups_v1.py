from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums_deduped = list(set(nums))

        nums[:] = nums_deduped

        return len(nums_deduped)


if __name__ == "__main__":
    solver = Solution()
    nums1 = [1, 1, 2]
    output1 = solver.removeDuplicates(nums=nums1)
    print(output1)

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    output2 = solver.removeDuplicates(nums=nums2)
    print(output2)

