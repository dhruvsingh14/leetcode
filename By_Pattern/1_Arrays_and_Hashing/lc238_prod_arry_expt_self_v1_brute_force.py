class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    prod *= nums[j]
            res.append(prod)
        return res


if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    nums1 = [1,2,3,4]
    output1 = solver.productExceptSelf(nums=nums1)
    print(output1) # Expected: [24,12,8,6]

    # Test case 2: 
    solver = Solution()
    nums2 = [-1,1,0,-3,3]
    output2 = solver.productExceptSelf(nums=nums2)
    print(output2) # Expected: [0,0,9,0,0]

