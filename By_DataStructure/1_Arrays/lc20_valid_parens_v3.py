from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if a string of brackets is valid using a stack and hashmap.
        
        Problem: LeetCode 20 - Valid Parentheses
        Pattern: Stack + Hashmap
        
        Approach:
        - Use a hashmap (closeToOpen) to map closing brackets to opening brackets
        - Use a stack to track opening brackets as we scan the string
        - For each character:
          - If it's a closing bracket (exists in closeToOpen): validate and pop
          - If it's an opening bracket (not in closeToOpen): push to stack
        - At the end, stack must be empty (all openers matched)
        
        Key difference from other approaches:
        - Checks if character is in the hashmap keys to determine if it's a closer
        - Uses implicit else for opening brackets (cleaner logic flow)
        - Returns True/False in a single concise line at the end
        
        Time Complexity: O(n) - single pass through string
        Space Complexity: O(n) - stack in worst case + O(1) for hashmap = O(n)
        
        Args:
            s: str - string containing only bracket characters: ()[]{}
            
        Returns:
            bool - True if all brackets are properly matched and nested, False otherwise
        """
        
        stack = []  # Stack to store opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}  # Map closing brackets to opening brackets
        
        for c in s:  # Iterate through each character in the string
            if c in closeToOpen:  # Character is a closing bracket (exists in hashmap keys)
                # Validate: stack must not be empty AND top must match the required opener
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Valid pair found, remove the opening bracket from stack
                else:
                    return False  # Invalid: either stack empty or mismatch
            else:  # Character is an opening bracket (not in hashmap keys)
                stack.append(c)  # Push opening bracket onto stack
        
        return True if not stack else False  # Return True if stack is empty, False otherwise


if __name__ == "__main__":
    # Test case 1: Simple valid pair
    solver = Solution()
    s1 = "()"
    output1 = solver.isValid(s=s1)
    print(output1)  # Expected: True
    
    # Test case 2: Multiple valid pairs in sequence
    solver = Solution()
    s2 = "()[]{}"
    output2 = solver.isValid(s=s2)
    print(output2)  # Expected: True

    # Test case 3: Mismatched bracket types
    solver = Solution()
    s3 = "(]"
    output3 = solver.isValid(s=s3)
    print(output3)  # Expected: False

    # Test case 4: Properly nested brackets
    solver = Solution()
    s4 = "([])"
    output4 = solver.isValid(s=s4)
    print(output4)  # Expected: True
        
    # Test case 5: Invalid nesting - brackets interleaved incorrectly
    solver = Solution()
    s5 = "([)]"
    output5 = solver.isValid(s=s5)
    print(output5)  # Expected: False