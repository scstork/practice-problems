class Solution:

    """
    Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
    
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    """
    
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = self.remove_duplicates_recurse(nums, 0, 1)
        return ret
    
    def remove_duplicates_recurse(self, nums: List[int], current = int, index = int) -> List[int]:
        if index == len(nums) - 1:
            if nums[index] == nums[current]:
                return current + 1
            return current + 2
        while index < len(nums) and nums[current] == nums[index]:
            index += 1
        if index < len(nums):
            nums[current + 1] = nums[index]
            return self.remove_duplicates_recurse(nums, current + 1, index)
        else:
            return current + 1
        