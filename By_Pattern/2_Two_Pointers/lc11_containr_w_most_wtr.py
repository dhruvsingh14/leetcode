class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        pseudocode
        - initialize two pointers, one at each end of the array
        - create var to store current area, and the maximum_area
        - initialize loop, run while l<r
        - calculate area: (dist = r-l)*(min(height[l], height[r])), store
            compare w/ max
        - advance smaller of left or right pointer in hope of finding greater 
            height
        - recalculate area
        - return max area
        '''
        l, r = 0, len(height) - 1
        curr_area = 0
        max_area = curr_area
        while l < r:
            curr_area = (r-l)*(min(height[l], height[r]))
            max_area = max(max_area, curr_area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area

if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    height1 = [1,8,6,2,5,4,8,3,7]
    output1 = solver.maxArea(height=height1)
    print(output1) # Expected: 49

    # Test case 2: 
    solver = Solution()
    height2 = [1,1]
    output2 = solver.maxArea(height=height2)
    print(output2) # Expected: 1
