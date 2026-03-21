class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:       

        '''pseudocode
        - sort numbers ascending
        - hashmap for each unique element
        - store element
        - use two pointer two sum algorithm on remaining elements 
            {not sure how to skip}
            - look for -(that element)
        - if found, store pair as value, next to that element / key in hashmap
        - key value pairs will be unique
        - to convert to list of lists, can loop over dict.items(), and simply
            append key to value lists     
        '''
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # deduplicating:
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            # fixing element i and looking for valid triplets
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > -1*nums[i]:
                    r-=1
                elif nums[l] + nums[r] < -1*nums[i]:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    # deduplicating matches / pairs found
                    while (l < r) and (nums[l] == nums[l-1]):
                        l+=1
                    while (r > l) and  (r < len(nums)-1) and (nums[r] == nums[r+1]):
                        r-=1
        return res


if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    nums1 = [-1,0,1,2,-1,-4]
    output1 = solver.threeSum(nums=nums1)
    print(output1) # Expected: [[-1,-1,2],[-1,0,1]]

    # Test case 2: 
    solver = Solution()
    nums2 = [0,1,1]
    output2 = solver.threeSum(nums=nums2)
    print(output2) # Expected: []

    # Test case 3: 
    solver = Solution()
    nums3 = [0,0,0]
    output3 = solver.threeSum(nums=nums3)
    print(output3) # Expected: [[0,0,0]]
