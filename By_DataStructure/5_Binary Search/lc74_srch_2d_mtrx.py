class Solution(object):
    def searchMatrix(self, matrix, target):

        # 2 binary searches: row, then within row
        width = len(matrix[0])
        t, b = 0, len(matrix) - 1

        if target < matrix[0][0] or target > matrix[len(matrix)-1][width-1]:
            return False

        while t <= b:
            mid = (b + t) // 2

            if target < matrix[mid][0]:
                b = mid - 1

            elif target > matrix[mid][width-1]:
                t = mid + 1

            else:
                nums = matrix[mid]
                break

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
                return True
            
        # exit with -1 if not found
        return False

if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    output1 = solver.searchMatrix(matrix=matrix1, target=target1)
    print(output1) # Expected: true

    # Test case 2: 
    solver = Solution()
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    output2 = solver.searchMatrix(matrix=matrix2, target=target2)
    print(output2) # Expected: false