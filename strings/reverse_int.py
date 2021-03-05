class Solution:

    """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
                the signed 32-bit integer range [-231, 231 - 1], then return 0."""

    def reverse(self, x: int) -> int:
        strx = str(x)
        if strx[0] == "-":
            strx = f"-{strx[:0:-1]}"
        else:
            strx= strx[::-1]
        try:
            intx = int(strx)
            if intx > -2**31 and intx < 2**31 - 1:
                return int(strx)
        except ValueError:
            return 0
        return 0