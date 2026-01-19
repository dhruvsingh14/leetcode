from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):
            if not stack and s[i] in [')', ']', '}']:
                return False

            if s[i] in ['(', '[', '{']:
                stack.append(s[i])

            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()

            elif s[i] == "]" and stack[-1] == "[":
                stack.pop()

            elif s[i] == "}" and stack[-1] == "{":
                stack.pop()

            else:
                return False

        if stack:
            return False
        else:
            return True

if __name__ == "__main__":
    solver = Solution()
    s1 = "()"
    output1 = solver.isValid(s=s1)
    print(output1)
    
    solver = Solution()
    s2 = "()[]{}"
    output2 = solver.isValid(s=s2)
    print(output2)

    solver = Solution()
    s3 = "(]"
    output3 = solver.isValid(s=s3)
    print(output3)

    solver = Solution()
    s4 = "([])"
    output4 = solver.isValid(s=s4)
    print(output4)
        
    solver = Solution()
    s5 = "([)]"
    output5 = solver.isValid(s=s5)
    print(output5)
