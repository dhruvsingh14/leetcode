class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        clean_str = [c.lower() for c in s if c.isalnum()]

        l, r = 0, len(clean_str)-1        
        while l < r:
            if clean_str[l] == clean_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
            

if __name__ == "__main__":
    # Test case 1: 
    solver = Solution()
    s1 = "A man, a plan, a canal: Panama"
    output1 = solver.isPalindrome(s=s1)
    print(output1) # Expected: True

    # Test case 2: 
    solver = Solution()
    s2 = "race a car"
    output2 = solver.isPalindrome(s=s2)
    print(output2) # Expected: False


    # Test case 3: 
    solver = Solution()
    s3 = " "
    output3 = solver.isPalindrome(s=s3)
    print(output3) # Expected: True