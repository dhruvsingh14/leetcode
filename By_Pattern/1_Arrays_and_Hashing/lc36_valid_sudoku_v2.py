# class Solution(object):
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         nums = list(range(1, 10))
#         # checking rows:
#         for i in board1:
#             for j in i:
#                 if j in nums:
#                     nums.remove(j)
#                 else:
#                     return False


"""
Valid Sudoku Checker (Three-Pass Approach)

Problem: LeetCode 36 - Valid Sudoku
Pattern: Matrix Traversal + Hash Set (Three Separate Passes)
Concept: Constraint Validation with Sequential Checks

Problem Statement:
Determine if a 9x9 Sudoku board is valid according to Sudoku rules:
1. Each row must contain digits 1-9 without repetition
2. Each column must contain digits 1-9 without repetition  
3. Each of the nine 3x3 sub-boxes must contain digits 1-9 without repetition

Approach Comparison:
- Previous solution: Single pass, tracks all constraints simultaneously
- This solution: Three separate passes (rows, then columns, then boxes)
- Both are correct, this one is more intuitive/readable

Why Three Passes:
✓ Easier to understand: each validation is separate
✓ Clear separation of concerns
✓ Each pass has simple, focused logic
✗ Slightly less efficient: visits cells multiple times
✗ More code: three loops instead of one

Algorithm Overview:
Pass 1: Validate all rows (check each row independently)
Pass 2: Validate all columns (check each column independently)
Pass 3: Validate all 3x3 boxes (check each box independently)

If all three passes complete without finding duplicates → valid board

3x3 Box Numbering (for Pass 3):
The nine 3x3 boxes are numbered 0-8:
    
    Box Layout:
    0 | 1 | 2
    --+---+--
    3 | 4 | 5
    --+---+--
    6 | 7 | 8
    
    Cell positions in each box:
    Box 0 (top-left):     rows 0-2, cols 0-2
    Box 1 (top-middle):   rows 0-2, cols 3-5
    Box 2 (top-right):    rows 0-2, cols 6-8
    Box 3 (middle-left):  rows 3-5, cols 0-2
    Box 4 (center):       rows 3-5, cols 3-5
    Box 5 (middle-right): rows 3-5, cols 6-8
    Box 6 (bottom-left):  rows 6-8, cols 0-2
    Box 7 (bottom-middle):rows 6-8, cols 3-5
    Box 8 (bottom-right): rows 6-8, cols 6-8

Box to Row/Col Conversion:
For a given box number (0-8), convert to actual board positions:
- Box row start = (square // 3) * 3
  - Boxes 0,1,2 → row 0
  - Boxes 3,4,5 → row 3
  - Boxes 6,7,8 → row 6
  
- Box col start = (square % 3) * 3
  - Boxes 0,3,6 → col 0
  - Boxes 1,4,7 → col 3
  - Boxes 2,5,8 → col 6

Example: Box 4 (center box)
- square = 4
- (4 // 3) * 3 = 1 * 3 = 3 → row starts at 3
- (4 % 3) * 3 = 1 * 3 = 3 → col starts at 3
- So box 4 covers rows [3,4,5] and cols [3,4,5]

Detailed Box Iteration:
    for i in range(3):      # i = 0, 1, 2 (row offset within box)
        for j in range(3):  # j = 0, 1, 2 (col offset within box)
            row = (square//3) * 3 + i  # base row + offset
            col = (square % 3) * 3 + j # base col + offset

Example for Box 5 (middle-right):
    square = 5
    Base row = (5//3)*3 = 1*3 = 3
    Base col = (5%3)*3 = 2*3 = 6
    
    i=0, j=0: row=3, col=6
    i=0, j=1: row=3, col=7
    i=0, j=2: row=3, col=8
    i=1, j=0: row=4, col=6
    i=1, j=1: row=4, col=7
    i=1, j=2: row=4, col=8
    i=2, j=0: row=5, col=6
    i=2, j=1: row=5, col=7
    i=2, j=2: row=5, col=8
    
    Covers: rows 3-5, cols 6-8 ✓

Time Complexity: O(1) - technically O(3 * 81) = O(243)
- Pass 1: Check 9 rows × 9 cells = 81 operations
- Pass 2: Check 9 cols × 9 cells = 81 operations
- Pass 3: Check 9 boxes × 9 cells = 81 operations
- Total: 243 operations (constant since board is always 9×9)

Space Complexity: O(1)
- Each pass uses one set that holds at most 9 values
- Set is reset for each row/col/box
- No growing data structures

Comparison to Single-Pass Solution:
Single Pass:
✓ More efficient: visits each cell once (81 operations)
✓ Less code overall
✗ Harder to understand: tracks three constraints at once
✗ More complex indexing

Three Pass (This Solution):
✓ Very clear and readable
✓ Easy to debug (can test each constraint independently)
✓ Natural mental model (check rows, then cols, then boxes)
✗ Less efficient: visits cells three times (243 operations)
✗ More code

Interview Strategy:
- If time is limited: implement single-pass (more impressive)
- If clarity matters: implement three-pass (easier to explain)
- Can mention both approaches and trade-offs

Edge Cases (Same as Single-Pass):
✓ Empty board (all "."): valid
✓ Partially filled: validates only filled cells
✓ Full board: validates all 81 cells
✓ Duplicate detection works correctly
✓ Empty cells properly skipped

Common Mistakes:
❌ Wrong box calculation formula
❌ Forgetting to reset 'seen' set between rows/cols/boxes
❌ Not skipping "." cells
❌ Off-by-one errors in box iteration
"""

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validate a 9x9 Sudoku board using three separate passes.
        
        Time Complexity: O(1) - always 9×9 board (243 cell checks)
        Space Complexity: O(1) - single set reused, max 9 elements
        
        Args:
            board: List[List[str]] - 9×9 Sudoku board
                   Cells are "1"-"9" or "." (empty)
                   
        Returns:
            bool - True if valid, False if any constraint violated
            
        Algorithm:
            Pass 1: Check all 9 rows for duplicates
            Pass 2: Check all 9 columns for duplicates
            Pass 3: Check all 9 boxes for duplicates
            
        Example:
            Valid board:
            [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             ...]
            → Returns True
            
            Invalid (duplicate in row):
            [["5","3","5",...],  # Two 5's in first row
             ...]
            → Returns False (caught in Pass 1)
            
        Note:
            - Three passes make the logic very clear
            - Each pass is independent and easy to understand
            - Less efficient than single-pass but more readable
        """
        # PASS 1: Validate all rows
        # Check each of the 9 rows independently for duplicates
        for row in range(9):  # For each row (0 to 8)
            seen = set()  # Fresh set for this row
            for i in range(9):  # For each cell in this row
                # Skip empty cells - they don't violate any constraint
                if board[row][i] == ".":
                    continue  # Move to next cell
                # Check if we've already seen this value in this row
                if board[row][i] in seen:
                    return False  # Duplicate found in row - invalid!
                # Add this value to the set for this row
                seen.add(board[row][i])
        
        # PASS 2: Validate all columns
        # Check each of the 9 columns independently for duplicates
        for col in range(9):  # For each column (0 to 8)
            seen = set()  # Fresh set for this column
            for i in range(9):  # For each cell in this column
                # Skip empty cells
                if board[i][col] == ".":
                    continue  # Move to next cell
                # Check if we've already seen this value in this column
                if board[i][col] in seen:
                    return False  # Duplicate found in column - invalid!
                # Add this value to the set for this column
                seen.add(board[i][col])
        
        # PASS 3: Validate all 3×3 boxes
        # Check each of the 9 boxes independently for duplicates
        for square in range(9):  # For each box (numbered 0 to 8)
            seen = set()  # Fresh set for this box
            # Iterate through all 9 cells in this box
            for i in range(3):  # Row offset within box (0, 1, 2)
                for j in range(3):  # Column offset within box (0, 1, 2)
                    # Convert box number + offsets to actual board coordinates
                    # (square//3)*3 gives the starting row for this box
                    # (square%3)*3 gives the starting column for this box
                    # i and j are offsets (0-2) within that box
                    row = (square//3) * 3 + i  # Actual row on board
                    col = (square % 3) * 3 + j  # Actual column on board
                    
                    # Skip empty cells
                    if board[row][col] == ".":
                        continue  # Move to next cell in box
                    # Check if we've already seen this value in this box
                    if board[row][col] in seen:
                        return False  # Duplicate found in box - invalid!
                    # Add this value to the set for this box
                    seen.add(board[row][col])
        
        # All three passes completed without finding duplicates
        # Board is valid!
        return True

        





if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    board1 = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    output1 = solver.isValidSudoku(board=board1)
    print(output1) # Expected: true

    # Test case 2: 
    solver = Solution()
    board2 = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    output2 = solver.isValidSudoku(board=board2)
    print(output2) # Expected: false