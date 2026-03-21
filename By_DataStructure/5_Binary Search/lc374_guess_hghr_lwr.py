# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# n is the picked number

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n

        while L <= R:
            mid = (L + R) // 2

            if guess(mid) == 1: # guessed low
                L = mid + 1
            elif guess(mid) == -1: # guessed high
                R = mid - 1
            else:
                return mid
        return -1