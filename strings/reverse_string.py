class Solution:

    """
    Write a function that reverses a string. The input string is given as an array of characters char[].
    
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    """
    
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start < end:
            save = s[start]
            s[start] = s[end]
            s[end] = save
            start +=1
            end -= 1
        