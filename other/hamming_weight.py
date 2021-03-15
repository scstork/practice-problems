class Solution:

    """
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
    """
    
    def hammingWeight(self, n: str) -> int:
        bits = 0
        str_n = bin(n)
        for bit in str_n:
            if bit == "1":
                bits += 1
        return bits