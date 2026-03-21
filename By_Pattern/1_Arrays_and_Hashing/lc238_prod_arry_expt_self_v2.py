class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        prod = 1
        pref_arr = [1] * n
        for i in range(1, n):
            prod *= nums[i-1]
            pref_arr[i] = prod

        prod = 1
        suf_arr = [1] * n
        for i in range(n-2, -1, -1):
            prod *= nums[i+1]
            suf_arr[i] = prod

        return [pref*suf for pref, suf in zip(pref_arr, suf_arr)]


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

