class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        num_ways = self.climbStairs(n-1) + self.climbStairs(n-2)


        return num_ways
        