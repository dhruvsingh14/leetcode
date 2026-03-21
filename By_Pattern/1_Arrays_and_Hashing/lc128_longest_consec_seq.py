class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_deduped = list(sorted(set(nums)))

        curr_len = 1
        max_len = curr_len

        for i in range(1, len(nums_deduped)):
            
            if nums_deduped[i] - nums_deduped[i-1] == 1:
                curr_len += 1
            else:
                curr_len = 1

            max_len = max(max_len, curr_len)

        return max_len


            

if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    nums1 = [100,4,200,1,3,2]
    output1 = solver.longestConsecutive(nums=nums1)
    print(output1) # Expected: 4

    # Test case 2: 
    solver = Solution()
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    output2 = solver.longestConsecutive(nums=nums2)
    print(output2) # Expected: 9


    # Test case 3: 
    solver = Solution()
    nums3 = [1,0,1,2]
    output3 = solver.longestConsecutive(nums=nums3)
    print(output3) # Expected: 3