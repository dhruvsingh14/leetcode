class Solution(object):

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def hrsToEat(k):
            time_per_pile = [(x + k - 1) // k for x in piles]
            return sum(time_per_pile)

        L, R = 1, max(piles)
        
        while L <= R:
            k = (L+R) // 2

            if hrsToEat(k) <= h:
                R = k - 1

            elif hrsToEat(k) > h:
                L = k + 1
        
        return L


if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    piles1 = [3,6,7,11]
    h1 = 8
    output1 = solver.minEatingSpeed(piles=piles1, h=h1)
    print(output1) # Expected: 4

    # Test case 2: 
    solver = Solution()
    piles2 = [30,11,23,4,20]
    h2 = 5
    output2 = solver.minEatingSpeed(piles=piles2, h=h2)
    print(output2) # Expected: 30

    # Test case 3: 
    solver = Solution()
    piles3 = [30,11,23,4,20]
    h3 = 6
    output3 = solver.minEatingSpeed(piles=piles3, h=h3)
    print(output3) # Expected: 23

