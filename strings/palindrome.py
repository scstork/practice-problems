import re

class Solution:

    """Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases."""

    def isPalindrome(self, s: str) -> bool:
        s =  re.sub(r'[\W_]+', '', s).lower()
        length = len(s)
        if length == 0:
            return True
        start = 0
        end = length - 1
        while start < length / 2:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True