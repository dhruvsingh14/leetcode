# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n

        while L <= R:
            mid = (L + R) // 2

            if isBadVersion(mid) == False: # guessed less than
                L = mid + 1
            elif isBadVersion(mid) == True: # guessed greater than equal to
                R = mid - 1
        
        return L

