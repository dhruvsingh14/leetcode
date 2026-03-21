from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_dict = defaultdict(int)

        for i in nums:
            count_dict[i] += 1

        count_dict_sorted = sorted(count_dict.keys(), key = lambda x: count_dict[x], reverse=True)

        return count_dict_sorted[:k]