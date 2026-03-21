class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1, r+1]
            

if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    numbers1 = [2,7,11,15]
    target1 = 9
    output1 = solver.twoSum(numbers=numbers1, target=target1)
    print(output1) # Expected: [1,2]

    # Test case 2: 
    solver = Solution()
    numbers2 = [2,3,4]
    target2 = 6
    output2 = solver.twoSum(numbers=numbers2, target=target2)
    print(output2) # Expected: [1,3]

    # Test case 3: 
    solver = Solution()
    numbers3 = [-1,0]
    target3 = -1
    output3 = solver.twoSum(numbers=numbers3, target=target3)
    print(output3) # Expected: [1,2]

