class Solution:

    """Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1."""

    def firstUniqChar(self, s: str) -> int:
        found = {}
        for char in s:
            found[char] = found.get(char, 0) + 1
        for char, index in zip(s, range(len(s))):
            if found.get(char) == 1:
                return index
        return -1