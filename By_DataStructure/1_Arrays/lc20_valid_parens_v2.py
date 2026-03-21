from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if a string of brackets is valid using a stack and hashmap.
        
        Problem: LeetCode 20 - Valid Parentheses
        Pattern: Stack + Hashmap
        
        Approach:
        - Use a hashmap (matching) to map closing brackets to opening brackets
        - Use a stack to track opening brackets as we scan the string
        - If character is an opening bracket '([{': push to stack
        - If character is a closing bracket ')]}': 
          - Check if stack is empty (no opener available) → invalid
          - Check if top of stack matches required opener from hashmap → invalid if no match
          - If valid match, pop from stack
        - At the end, stack must be empty (all openers matched)
        
        Advantages over direct comparison approach:
        - Cleaner logic with single if/else instead of multiple elif chains
        - Easy to extend for new bracket types
        - More Pythonic and maintainable
        - Checks for opening brackets using string membership ('([{')
        
        Time Complexity: O(n) - single pass through string
        Space Complexity: O(n) - stack in worst case + O(1) for hashmap = O(n)
        
        Args:
            s: str - string containing only bracket characters: ()[]{}
            
        Returns:
            bool - True if all brackets are properly matched and nested, False otherwise
            
        Note:
            This implementation assumes input only contains valid bracket characters.
            If char is not in '([{', it's treated as a closing bracket.
        """
        
        stack = []  # Stack to store opening brackets
        matching = {')': '(', ']': '[', '}': '{'}  # Map closing brackets to their opening pairs

        for char in s:  # Iterate through each character in the string
            if char in '([{':  # Check if character is an opening bracket
                stack.append(char)  # Push opening bracket onto stack
            else:  # Character is a closing bracket
                # Validate: stack must not be empty AND top must match the required opener
                if not stack or stack[-1] != matching[char]:
                    return False  # Invalid: either no opener available or mismatch
                stack.pop()  # Valid pair found, remove the opening bracket from stack

        return len(stack) == 0  # Return True if stack is empty (all brackets matched)

if __name__ == "__main__":
    # Test case 1: Simple valid pair
    solver = Solution()
    s1 = "()"
    output1 = solver.isValid(s=s1)
    print(output1) # Expected: True
    
    # Test case 2: Multiple valid pairs in sequence
    solver = Solution()
    s2 = "()[]{}"
    output2 = solver.isValid(s=s2)
    print(output2) # Expected: True

    # Test case 3: Mismatched bracket types
    solver = Solution()
    s3 = "(]"
    output3 = solver.isValid(s=s3)
    print(output3) # Expected: False

    # Test case 4: Properly nested brackets
    solver = Solution()
    s4 = "([])"
    output4 = solver.isValid(s=s4)
    print(output4) # Expected: True

    # Test case 5: Invalid nesting - brackets interleaved incorrectly        
    solver = Solution()
    s5 = "([)]"
    output5 = solver.isValid(s=s5)
    print(output5) # Expected: False - ] tries to close [ but ( is still open
