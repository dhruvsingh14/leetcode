class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for i, n in enumerate(nums):
            if (target - n) in index_map:
                return (index_map[target - n], i)
            index_map[n] = i


        