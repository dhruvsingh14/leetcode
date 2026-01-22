from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if a string of brackets is valid using a stack.
        
        Problem: LeetCode 20 - Valid Parentheses
        Pattern: Stack (LIFO - Last In First Out)
        
        Approach:
        - Use a stack to track opening brackets as we scan the string
        - When we encounter an opening bracket: push it onto the stack
        - When we encounter a closing bracket: check if it matches the most recent opening bracket
        - If brackets match: pop from stack (pair is valid)
        - If brackets don't match OR stack is empty when we see a closer: invalid
        - At the end, stack must be empty (all openers have matching closers)
        
        Key Insights:
        - Stack is perfect for this because brackets must close in LIFO order
        - Example: "([)]" is invalid because ] tries to close [ but ( is still open
        - Valid example: "([])" - [ closes first, then ( closes
        
        Time Complexity: O(n) - single pass through string
        Space Complexity: O(n) - worst case all characters are opening brackets
        
        Args:
            s: str - string containing only bracket characters: ()[]{}
            
        Returns:
            bool - True if all brackets are properly matched and nested, False otherwise
            
        Edge Cases:
        - String starts with closing bracket: return False immediately
        - Unmatched opening brackets remain: return False at end
        - Closing bracket with no corresponding opener: return False
        """

        stack = [] # Stack to store opening brackets

        for i in range(len(s)): # Iterate through each character in the string
            # Edge case: if stack is empty and we encounter a closing bracket, it's invalid
            if not stack and s[i] in [')', ']', '}']:
                return False

            # If we encounter an opening bracket, push it onto the stack
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])

            # If closing parenthesis, check if it matches the most recent opening bracket
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop() # Valid pair found, remove the opening bracket

            # If closing square bracket, check if it matches the most recent opening bracket
            elif s[i] == "]" and stack[-1] == "[":
                stack.pop() # Valid pair found, remove the opening bracket

            # If closing curly brace, check if it matches the most recent opening bracket
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop() # Valid pair found, remove the opening bracket

            else:
                # Mismatch: closing bracket doesn't match the most recent opener
                return False

        # After processing all characters, stack should be empty
        # If stack has elements, there are unmatched opening brackets
        if stack:
            return False
        else:
            return True

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
