from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for i in range(len(s)):
            dict1[s[i]] += 1
            dict2[t[i]] += 1

        return dict1 == dict2
