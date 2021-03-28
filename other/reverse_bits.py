class Solution:

    """
    Reverse bits of a given 32 bits unsigned integer.
    """
    
    def reverseBits(self, n: int) -> int:
        # convert n to 32 bit binary string
        n_bin = bin(n)[2:].zfill(32)
        # reverse the binary string
        n_bin_rev = n_bin[::-1]\
        # return the binary string cast to int
        return int(n_bin_rev, 2)