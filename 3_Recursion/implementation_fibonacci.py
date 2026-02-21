"""
Fibonacci Number Calculation Using Recursion (Naive Approach)

Pattern: Recursion (Tree Recursion - Multiple Recursive Calls)
Concept: Fibonacci Sequence

Fibonacci Sequence Definition:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1
- Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Why This Is Called "Tree Recursion":
- Unlike factorial (linear recursion - one recursive call),
  Fibonacci makes TWO recursive calls per level
- Creates a tree-like structure of function calls
- Each node spawns two more nodes (except base cases)

Call Tree Visualization for fibonacci(5):
                        fib(5)
                       /      \
                   fib(4)      fib(3)
                   /    \      /    \
              fib(3)  fib(2) fib(2) fib(1)
              /   \   /   \   /   \
          fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
          /   \
      fib(1) fib(0)

Notice the MASSIVE REDUNDANCY:
- fib(3) is calculated 2 times
- fib(2) is calculated 3 times
- fib(1) is calculated 5 times
- fib(0) is calculated 3 times
This is extremely inefficient!

Time Complexity: O(2^n) - exponential! Each call spawns ~2 more calls
- For n=5: ~15 function calls
- For n=10: ~177 function calls
- For n=20: ~21,891 function calls
- For n=40: ~331,160,281 function calls (takes several seconds!)

Space Complexity: O(n) - maximum depth of call stack
- The call stack only goes n levels deep (longest path)
- But we make exponentially many calls overall

Why This Implementation Is BAD:
- Extremely slow for even moderate values of n (n > 35)
- Recalculates same values over and over (no memoization)
- Used for teaching recursion, NOT for production code
- Classic example of when recursion is inefficient without optimization

Better Approaches:
1. Dynamic Programming (Memoization): O(n) time, O(n) space
   - Store calculated values to avoid recomputation
2. Iterative approach: O(n) time, O(1) space
   - Use a loop with two variables
3. Matrix exponentiation: O(log n) time
   - Advanced technique using matrix multiplication

Common Interview Question:
"What's wrong with this Fibonacci implementation and how would you fix it?"
Answer: Exponential time due to redundant calculations. Fix with memoization/DP or iteration.

Real-World Applications of Fibonacci:
- Nature (spiral patterns, flower petals, tree branching)
- Financial markets (Fibonacci retracements)
- Computer algorithms (Fibonacci heap, search algorithms)
- Art and architecture (golden ratio approximation)
"""


def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using naive recursion.
    
    WARNING: This is an exponentially slow implementation!
    Use only for small values of n (n < 35) or for learning purposes.
    
    Time Complexity: O(2^n) - exponential, extremely slow
    Space Complexity: O(n) - call stack depth
    
    Args:
        n: int - position in Fibonacci sequence (0-indexed)
        
    Returns:
        int - the n-th Fibonacci number
        
    Mathematical Definition:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1
        
    Examples:
        fibonacci(0) → 0
        fibonacci(1) → 1
        fibonacci(2) → 1 (0 + 1)
        fibonacci(3) → 2 (1 + 1)
        fibonacci(4) → 3 (1 + 2)
        fibonacci(5) → 5 (2 + 3)
        fibonacci(6) → 8 (3 + 5)
        fibonacci(10) → 55
        
    Recursive Breakdown for fibonacci(4):
        fibonacci(4) = fibonacci(3) + fibonacci(2)
                     = (fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0))
                     = ((fibonacci(1) + fibonacci(0)) + 1) + (1 + 0)
                     = ((1 + 0) + 1) + 1
                     = (1 + 1) + 1
                     = 2 + 1
                     = 3
                     
    Performance Warning:
        fibonacci(10) → ~177 calls → instant
        fibonacci(20) → ~21,891 calls → still fast
        fibonacci(30) → ~2,692,537 calls → ~0.5 seconds
        fibonacci(40) → ~331,160,281 calls → several seconds
        fibonacci(50) → takes MINUTES (don't try this!)
        
    Note:
        This implementation demonstrates the concept of tree recursion
        but is NOT suitable for production use. See module docstring
        for better alternatives (memoization, iteration, etc.).
    """
    # Base case: n = 0 or 1
    # These are the terminating conditions that stop the recursion
    # F(0) = 0 and F(1) = 1 by definition of Fibonacci sequence
    if n <= 1:
        return n  # Return n itself (0 for n=0, 1 for n=1)

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    # Break problem into two smaller subproblems
    # This creates a binary tree of recursive calls
    # Each call spawns two more calls until hitting base cases
    return fibonacci(n - 1) + fibonacci(n - 2)  # Sum of two previous Fibonacci numbers