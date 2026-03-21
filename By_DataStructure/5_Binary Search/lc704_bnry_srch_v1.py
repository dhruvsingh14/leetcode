class Solution(object):
    def search(self, nums, target):
        # initialize
        L, R = 0, len(nums) - 1 

        # loop
        while L <= R:

            # calculate mid - within loop:
            mid = (L+R)//2

            # check 1: checking right half
            if target < nums[mid]:
                R = mid - 1

            # check 2: checking left half
            elif target > nums[mid]:
                L = mid + 1

            # check 3:
            else:
                return mid
            
        # exit with -1 if not found
        return -1


if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    output1 = solver.search(nums=nums1, target=target1)
    print(output1) # Expected: 4

    # Test case 2: 
    solver = Solution()
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    output2 = solver.search(nums=nums2, target=target2)
    print(output2) # Expected: -1