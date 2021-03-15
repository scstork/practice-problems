class Solution:

    """
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.
    """

    def hammingDistance(self, x: int, y: int) -> int:
        str_x = bin(x)[2:]
        str_y = bin(y)[2:]
        
        if len(str_x) < len(str_y):
            str_x = str_x.zfill(len(str_y))
        else:
            str_y = str_y.zfill(len(str_x))
        hamming_distance = 0
        
        for char_x, char_y in zip(str_x[::-1], str_y[::-1]):
            if char_x != char_y:
                hamming_distance += 1
        
        return hamming_distance