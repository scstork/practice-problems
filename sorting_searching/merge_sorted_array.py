class Solution:

    """Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
            
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = len(nums1) - 1
        index1 = m - 1
        index2 = n - 1
        while end >= 0 and (index2 >=0 or index1 >= 0):
            print(end, index1, index2)
            if index1 >= 0:
                a = nums1[index1]
            else:
                a = None
            if index2 >= 0:
                b = nums2[index2]
            else:
                b = None
            if a is not None and b is None:
                break
            elif b is not None and a is None:
                nums1[end] = b
                index2 -= 1
            elif a < b:
                nums1[end] = b
                index2 -=1
            else:
                nums1[end] = a
                index1 -= 1
            end -= 1