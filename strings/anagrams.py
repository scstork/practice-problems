class Solution:

    """Given two strings s and t , write a function to determine if t is an anagram of s."""

    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are different, s and t can't be anagrams
        if len(s) != len(t):
            return False
        # compare occurences of each char in s and t
        sletters, tletters = {}, {}
        for char in s:
            sletters[char] = sletters.get(char, 0) + 1
        for char in t:
            tletters[char] = tletters.get(char, 0) + 1
        if sletters == tletters:
            return True
        return False