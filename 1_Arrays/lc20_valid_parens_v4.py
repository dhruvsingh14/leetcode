from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if a string of brackets is valid using a stack and hashmap.
        
        Problem: LeetCode 20 - Valid Parentheses
        Pattern: Stack + Hashmap
        
        Approach:
        - Use a hashmap to map closing brackets to their corresponding opening brackets
        - Use a stack to track opening brackets as we scan the string
        - When we encounter a closing bracket: check hashmap and validate against stack top
        - When we encounter an opening bracket: push it onto the stack
        - At the end, stack must be empty (all openers have matching closers)
        
        Advantages over direct comparison approach:
        - More elegant and maintainable code
        - Easier to extend (just add entries to hashmap for new bracket types)
        - Less repetitive logic (no if/elif chains)
        - More Pythonic
        
        Time Complexity: O(n) - single pass through string
        Space Complexity: O(n) - stack in worst case + O(1) for hashmap = O(n)
        
        Args:
            s: str - string containing only bracket characters: ()[]{}
            
        Returns:
            bool - True if all brackets are properly matched and nested, False otherwise
        """
        
        stack = []  # Stack to store opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}  # Map closing brackets to opening brackets
        
        for char in s:  # Iterate through each character
            if char in bracket_map:  # It's a closing bracket
                # Check if stack is empty or top doesn't match the required opener
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Valid pair found, remove the opening bracket
            else:  # It's an opening bracket
                stack.append(char)  # Push opening bracket onto stack
        
        return len(stack) == 0  # Stack should be empty if all brackets matched


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