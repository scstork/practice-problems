class Solution:
    """
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    
    If needle is an empty string, return 0.
    """

    class Solution:
    def strStr_faster(self, haystack: str, needle: str) -> int:
        # runs in less time than the previous solution
        if needle == "":
            return 0
        # check if first len(needle) characters in haystack == needle
        # use string splicing to compare strings
        orig_index = 0
        while len(haystack) >= len(needle):
            index = 0
            if haystack[:len(needle)] == needle:
                return orig_index
            orig_index += 1
            haystack = haystack[1:]
        return -1
        

    def strStr_lessmem(self, haystack: str, needle: str) -> int:
        # uses less memory than the previous solution
        if needle == "":
            return 0
        # check if first len(needle) characters in haystack == needle
        # break as soon as we know they aren't equal
        # this should be faster than the builtin str starts with method
        orig_index = 0
        while len(haystack) >= len(needle):
            index = 0
            while index < len(needle) and haystack[index] == needle[index]:
                index += 1
            if index == len(needle):
                return orig_index
            orig_index += 1
            haystack = haystack[1:]
        return -1
        