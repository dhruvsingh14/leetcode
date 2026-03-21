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
Valid Sudoku Checker

Problem: LeetCode 36 - Valid Sudoku
Pattern: Hash Set + Matrix Traversal
Concept: Constraint Validation

Problem Statement:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain digits 1-9 without repetition
2. Each column must contain digits 1-9 without repetition
3. Each of the nine 3x3 sub-boxes must contain digits 1-9 without repetition

Note: 
- A Sudoku board (partially filled) could be valid but is not necessarily solvable
- Only filled cells need to be validated (empty cells marked as ".")
- We're NOT solving the Sudoku, just checking if current state is valid

Key Insight:
- Use hash sets to track seen numbers in each row, column, and 3x3 square
- For each filled cell, check if its value already exists in:
  - Its row
  - Its column  
  - Its 3x3 sub-box
- If duplicate found in any, return False
- If no duplicates found after checking all cells, return True

Data Structure Choice: defaultdict(set)
- cols: maps column index → set of values seen in that column
- rows: maps row index → set of values seen in that row
- squares: maps (row//3, col//3) → set of values seen in that 3x3 box

3x3 Sub-box Indexing:
The 9x9 board is divided into nine 3x3 sub-boxes:
    
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    (2,0) (2,1) (2,2)
    
To map cell (r, c) to its sub-box:
- Box row = r // 3 (integer division)
- Box col = c // 3 (integer division)
- Key = (r // 3, c // 3)

Example:
    Cell (0,0) → Box (0,0) - top-left
    Cell (4,7) → Box (1,2) - middle-right
    Cell (8,8) → Box (2,2) - bottom-right

Visual Example of 3x3 Boxes:
    Board positions:        Box indices:
    0 1 2 | 3 4 5 | 6 7 8   (0,0) | (0,1) | (0,2)
    0 1 2 | 3 4 5 | 6 7 8   (0,0) | (0,1) | (0,2)
    0 1 2 | 3 4 5 | 6 7 8   (0,0) | (0,1) | (0,2)
    ------+-------+------   ------+-------+------
    3 4 5 | 6 7 8 | 0 1 2   (1,0) | (1,1) | (1,2)
    3 4 5 | 6 7 8 | 0 1 2   (1,0) | (1,1) | (1,2)
    3 4 5 | 6 7 8 | 0 1 2   (1,0) | (1,1) | (1,2)
    ------+-------+------   ------+-------+------
    6 7 8 | 0 1 2 | 3 4 5   (2,0) | (2,1) | (2,2)
    6 7 8 | 0 1 2 | 3 4 5   (2,0) | (2,1) | (2,2)
    6 7 8 | 0 1 2 | 3 4 5   (2,0) | (2,1) | (2,2)

Algorithm Flow:
1. Initialize three defaultdict(set) for tracking rows, cols, squares
2. For each cell (r, c) in the 9x9 board:
   a. If cell is ".", skip it (empty cells don't need validation)
   b. If value already in rows[r], return False (row duplicate)
   c. If value already in cols[c], return False (column duplicate)
   d. If value already in squares[(r//3, c//3)], return False (box duplicate)
   e. Add value to rows[r], cols[c], and squares[(r//3, c//3)]
3. If all cells checked without duplicates, return True

Time Complexity: O(1) - technically O(81) since board is always 9x9
- We iterate through exactly 81 cells
- Each check and insert is O(1) for hash set
- Constant time since board size is fixed

Space Complexity: O(1) - technically O(81) 
- At most 81 entries across all three defaultdicts
- Maximum 9 values per row/col/square
- Constant space since board size is fixed

Why defaultdict(set):
- defaultdict: automatically creates empty set for new keys
- set: O(1) lookup and insertion, perfect for duplicate detection
- Alternative: could use arrays/lists but sets are cleaner

Edge Cases:
✓ Empty board (all "."): valid, returns True
✓ Partially filled: validates only filled cells
✓ Full board: validates all 81 cells
✓ Duplicate in row/col/box: correctly returns False
✓ Valid but unsolvable: returns True (not checking solvability)

Common Mistakes to Avoid:
❌ Forgetting to skip "." cells
❌ Wrong sub-box calculation (not using //)
❌ Checking solvability instead of just validity
❌ Using inefficient data structures (lists instead of sets)

Interview Tips:
- Clarify: Do empty cells count as valid? (Yes)
- Clarify: Are we solving or just validating? (Just validating)
- Explain the (r//3, c//3) box indexing clearly
- Mention time/space are both O(1) since board is fixed size
"""

from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        
        Time Complexity: O(1) - always 9x9 board (81 cells)
        Space Complexity: O(1) - at most 81 values stored
        
        Args:
            board: List[List[str]] - 9x9 Sudoku board
                   Each cell is either "1"-"9" or "." (empty)
                   
        Returns:
            bool - True if board is valid, False otherwise
            
        Validation Rules:
            1. Each row must contain digits 1-9 without repetition
            2. Each column must contain digits 1-9 without repetition
            3. Each 3x3 sub-box must contain digits 1-9 without repetition
            
        Examples:
            Valid board (partially filled):
            [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
            → True
            
            Invalid (duplicate 8 in first column):
            [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ...
            → False
            
        Algorithm:
            1. Create tracking structures (sets) for rows, cols, boxes
            2. Iterate through every cell in the 9x9 board
            3. Skip empty cells (".")
            4. For each filled cell, check for duplicates in row/col/box
            5. If duplicate found, return False
            6. Otherwise, add to tracking sets
            7. If all cells pass, return True
            
        Note:
            - We only validate current state, not solvability
            - Empty cells are always valid
            - Uses (r//3, c//3) to identify which 3x3 box a cell belongs to
        """
        # Initialize tracking structures using defaultdict(set)
        # Each will map an index/key to a set of values seen
        cols = collections.defaultdict(set)  # cols[c] = set of values in column c
        rows = collections.defaultdict(set)  # rows[r] = set of values in row r
        squares = collections.defaultdict(set)  # key = (r // 3, c // 3)
        
        # Iterate through every cell in the 9x9 board
        for r in range(9):  # For each row (0 to 8)
            for c in range(9):  # For each column (0 to 8)
                # Check if current cell is empty
                # Empty cells don't need validation, skip them
                if board[r][c] == ".":
                    continue  # Skip to next cell
                
                # Check for duplicates in row, column, or 3x3 sub-box
                # If current value already exists in any of these, board is invalid
                if (board[r][c] in rows[r] or  # Duplicate in same row
                    board[r][c] in cols[c] or  # Duplicate in same column
                    board[r][c] in squares[(r // 3, c // 3)]):  # Duplicate in same 3x3 box
                    return False  # Found duplicate, board is invalid
                
                # No duplicate found, add current value to tracking sets
                # Add to column c's set
                cols[c].add(board[r][c])
                # Add to row r's set
                rows[r].add(board[r][c])
                # Add to the appropriate 3x3 sub-box
                # (r // 3, c // 3) identifies which of the 9 boxes this cell belongs to
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # If we've checked all cells without finding duplicates, board is valid
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