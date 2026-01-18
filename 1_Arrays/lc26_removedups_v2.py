from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0 
        j = i+1

        while j < len(nums): # j scans entire array
            if nums[i] != nums[j]: # if ith, jth elements aren't equal, ensure they're adjacent
                nums[i+1] = nums[j]
                i+=1 # advance both pointers
                j+=1
            else:
                j+=1 # while scanning dup. seq. keep i fixed
                
        return i+1 # only returning the length of unique values, doesn't matter what comes after


if __name__ == "__main__":
    solver = Solution()
    nums1 = [1, 1, 2]
    output1 = solver.removeDuplicates(nums=nums1)
    print(output1)

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    output2 = solver.removeDuplicates(nums=nums2)
    print(output2)

