"""
Factorial Calculation Using Recursion

Pattern: Recursion (Divide and Conquer)
Concept: Recursive Function

Key Characteristics of Recursion:
- Function calls itself with a smaller/simpler input
- Must have a base case to stop recursion (prevents infinite loop)
- Builds up solution by combining results from recursive calls
- Uses the call stack implicitly to store intermediate states

Recursion Anatomy:
1. Base case: Stopping condition (when to stop recursing)
2. Recursive case: How to break problem into smaller subproblems
3. Combine: How to use result from subproblem to solve current problem

Why Recursion Works for Factorial:
- n! = n × (n-1) × (n-2) × ... × 2 × 1
- This can be rewritten as: n! = n × (n-1)!
- (n-1)! is a smaller version of the same problem
- Base case: 0! = 1 and 1! = 1 (by definition)

Call Stack Visualization for factorial(4):
    factorial(4)
        ↓ returns 4 * factorial(3)
    factorial(3)
        ↓ returns 3 * factorial(2)
    factorial(2)
        ↓ returns 2 * factorial(1)
    factorial(1)
        ↓ returns 1 (base case)
    
    Unwinding:
    factorial(1) → 1
    factorial(2) → 2 * 1 = 2
    factorial(3) → 3 * 2 = 6
    factorial(4) → 4 * 6 = 24

Time Complexity: O(n) - n recursive calls
Space Complexity: O(n) - n frames on the call stack

Recursion vs Iteration:
- Recursion: More elegant, easier to understand for some problems
- Iteration: More efficient (no call stack overhead), harder to overflow
- For factorial: iteration is actually better in practice
- But recursion is great for teaching the concept!

Common Recursive Interview Problems:
- Tree traversal (pre/in/post-order)
- Binary search (recursive version)
- Fibonacci sequence
- Permutations and combinations
- Backtracking problems (N-Queens, Sudoku solver)
- Merge sort, Quick sort
- Graph DFS (Depth-First Search)

Key Recursion Pitfall:
- Missing/wrong base case → Stack overflow (infinite recursion)
- Too deep recursion → Stack overflow (even with base case)
- Python default recursion limit: ~1000 calls
"""


def factorial(n):
    """
    Calculate n! (n factorial) using recursion.
    
    Time Complexity: O(n) - makes n recursive calls
    Space Complexity: O(n) - n frames on the call stack
    
    Args:
        n: int - non-negative integer to calculate factorial of
        
    Returns:
        int - the factorial of n (n!)
        
    Mathematical Definition:
        n! = n × (n-1) × (n-2) × ... × 2 × 1
        0! = 1 (by definition)
        1! = 1
        
    Examples:
        factorial(0) → 1
        factorial(1) → 1
        factorial(4) → 4 × 3 × 2 × 1 = 24
        factorial(5) → 5 × 4 × 3 × 2 × 1 = 120
        
    Recursive Breakdown:
        factorial(4) = 4 × factorial(3)
                     = 4 × (3 × factorial(2))
                     = 4 × (3 × (2 × factorial(1)))
                     = 4 × (3 × (2 × 1))
                     = 4 × (3 × 2)
                     = 4 × 6
                     = 24
                     
    Note:
        This implementation assumes n >= 0. For negative numbers,
        factorial is undefined (would need error handling).
    """
    # Base case: n = 0 or 1
    # This is where recursion stops - prevents infinite loop
    # Both 0! and 1! are defined as 1
    if n <= 1:
        return 1
        
    # Recursive case: n! = n * (n - 1)!
    # Break problem into: current number × factorial of (n-1)
    # This call will eventually hit the base case when n reaches 1
    return n * factorial(n - 1)  # Recursive call with smaller input