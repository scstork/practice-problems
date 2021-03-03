from typing import List

class Solution:

    """
    Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
     
    Integers can appear more than once in the list. You may assume all numbers in the list are positive.
    
    For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
    """

    def subset_with_sum(self, S: List[int], k: int) -> List[int]:
        S.sort(reverse=True)

        # any portion of S that is > k doesn't matter
        index = 0
        while index < len(S) and S[index] > k:
            index += 1

        # if we've reached the end of the list, return
        if index == len(S):
            return None

        S = S[index:]

        # iterate through each item looking for subsets; think this is O(nlog(n))
        # modifying and searching through ranges in each iteration is potentially n
        # space efficiency is terrible
        for outer, index in zip(S, range(len(S))):
            ranges = []
             # list of tuples of subsets and their sums for optimization; prob the wrong data structure
            for inner in S[index + 1:]:
                curr_sum = outer + inner
                if curr_sum == k:
                    return [outer, inner]
                for (subset, subset_sum), subset_index in zip(ranges, range(len(ranges))):
                    inner_sum = subset_sum + inner
                    if inner_sum == k:
                        subset.append(inner)
                        return subset
                    elif inner_sum < k:
                        subset.append(inner)
                        ranges[subset_index] = (subset, inner_sum)
                if curr_sum < k:
                    ranges.append(([outer, inner], curr_sum))

        return None


if __name__ == "__main__":
    S = [12, 1, 61, 5, 9, 2]
    s_original = str(S)
    k = 24
    soln = Solution().subset_with_sum(S=S, k=k)
    print(f"Subset {soln} of {s_original} adds up to {k}!")