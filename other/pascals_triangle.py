class Solution:

    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    Examples:
        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

        Input: numRows = 1
        Output: [[1]]

    Input should be between 1 and 30, but this implementation allows for 0 as well, returning [].
    """

    def generate(self, numRows: int) -> List[List[int]]:
        return self.generate_recurse(numRows, [])
    
    def generate_recurse(self, num_rows: int, triangle: List[List[int]]) -> List[List[int]]:
        if num_rows == 0:
            return triangle
        if len(triangle) == 0:
            return self.generate_recurse(num_rows - 1, [[1]])
        prev_row = triangle[-1]
        new_row = [1]
        index = 0
        for start, end in zip(prev_row[:-1], prev_row[1:]):
            new_row.append(start + end)
        new_row.append(1)
        triangle.append(new_row)
        return self.generate_recurse(num_rows - 1, triangle)