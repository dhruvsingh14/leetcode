from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        angrm_dict = defaultdict(list)
        for s in strs:
            sorted_string = "".join(sorted(s))
            angrm_dict[sorted_string].append(s)

        return list(angrm_dict.values())

