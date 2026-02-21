"""
Climbing Stairs (Naive Recursive Approach)

Problem: LeetCode 70 - Climbing Stairs
Pattern: Recursion (Tree Recursion) / Dynamic Programming

Problem Statement:
- You are climbing a staircase with n steps
- Each time you can climb 1 or 2 steps
- How many distinct ways can you climb to the top?

Key Insight - This Is Actually Fibonacci!:
- To reach step n, you must have come from either:
  - Step (n-1) with a 1-step climb, OR
  - Step (n-2) with a 2-step climb
- So: ways(n) = ways(n-1) + ways(n-2)
- This is the Fibonacci recurrence relation!
- Base cases: ways(1) = 1, ways(2) = 2

Examples:
    n=1: [1] → 1 way
    n=2: [1,1], [2] → 2 ways
    n=3: [1,1,1], [1,2], [2,1] → 3 ways
    n=4: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2] → 5 ways
    n=5: 8 ways
    
    Pattern: 1, 2, 3, 5, 8, 13, 21... (Fibonacci starting from F(1)=1, F(2)=2)

Call Tree Visualization for climbStairs(5):
                    climb(5)
                   /        \
              climb(4)      climb(3)
              /     \        /     \
         climb(3) climb(2) climb(2) climb(1)
         /     \
    climb(2) climb(1)

Notice the MASSIVE REDUNDANCY (same as Fibonacci):
- climb(3) is calculated 2 times
- climb(2) is calculated 3 times
- This gets exponentially worse as n grows

Time Complexity: O(2^n) - exponential! Same problem as naive Fibonacci
- For n=5: ~15 function calls
- For n=20: ~21,891 calls
- For n=40: ~331,160,281 calls (takes several seconds!)

Space Complexity: O(n) - maximum depth of call stack

Why This Implementation Is BAD (Same as Fibonacci):
- Extremely slow for even moderate values of n (n > 35)
- Recalculates same subproblems over and over
- No memoization = massive waste of computation
- Used for teaching recursion, NOT for production code

Better Approaches:
1. Dynamic Programming (Memoization): O(n) time, O(n) space
   - Store calculated values in a dictionary/array
   - Check if already calculated before recursing
2. Dynamic Programming (Tabulation): O(n) time, O(n) space
   - Build up solution iteratively in an array
3. Space-optimized DP: O(n) time, O(1) space
   - Only keep track of last two values (like iterative Fibonacci)
   - Best practical solution

Interview Follow-up Questions:
- "How would you optimize this?" → Add memoization or use iteration
- "What if you could climb 1, 2, or 3 steps?" → Same pattern, just add climb(n-3)
- "Can you solve it in O(1) space?" → Use two variables to track last two values

Connection to Fibonacci:
    Climbing Stairs: 1, 2, 3, 5, 8, 13, 21...
    Fibonacci:       1, 1, 2, 3, 5, 8, 13, 21...
    They're the same sequence, just shifted by one position!
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb n stairs.
        
        WARNING: This is an exponentially slow implementation!
        Use only for small values of n (n < 35) or for learning purposes.
        
        Time Complexity: O(2^n) - exponential, extremely slow
        Space Complexity: O(n) - call stack depth
        
        Args:
            n: int - number of steps in the staircase
            
        Returns:
            int - number of distinct ways to climb to the top
            
        Recurrence Relation:
            ways(1) = 1 (base case)
            ways(2) = 2 (base case)
            ways(n) = ways(n-1) + ways(n-2) for n > 2
            
        Examples:
            climbStairs(1) → 1
            climbStairs(2) → 2
            climbStairs(3) → 3 (2 + 1)
            climbStairs(4) → 5 (3 + 2)
            climbStairs(5) → 8 (5 + 3)
            climbStairs(6) → 13 (8 + 5)
            
        Recursive Breakdown for climbStairs(4):
            climbStairs(4) = climbStairs(3) + climbStairs(2)
                           = (climbStairs(2) + climbStairs(1)) + 2
                           = (2 + 1) + 2
                           = 3 + 2
                           = 5
                           
        Why It Works:
            To reach step n, you must come from either:
            - Step (n-1) with a 1-step climb
            - Step (n-2) with a 2-step climb
            So total ways = ways to reach (n-1) + ways to reach (n-2)
            
        Performance Warning:
            climbStairs(10) → instant
            climbStairs(20) → still fast
            climbStairs(30) → ~0.5 seconds
            climbStairs(40) → several seconds
            climbStairs(45) → takes MINUTES (don't try!)
            
        Note:
            This demonstrates tree recursion but is NOT suitable for
            production. Use memoization or iterative DP instead.
        """
        # Base case 1: Only 1 step
        # There's only one way to climb 1 step: [1]
        if n == 1:
            return 1
            
        # Base case 2: 2 steps
        # There are two ways to climb 2 steps: [1,1] or [2]
        if n == 2:
            return 2
        
        # Recursive case: ways(n) = ways(n-1) + ways(n-2)
        # To reach step n, you either:
        # 1. Came from step (n-1) and climbed 1 step, OR
        # 2. Came from step (n-2) and climbed 2 steps
        # Total ways is the sum of ways to reach these two previous positions
        num_ways = self.climbStairs(n-1) + self.climbStairs(n-2)  # Fibonacci recurrence

        # Return the total number of distinct ways to climb n stairs
        return num_ways