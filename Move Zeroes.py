class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

    for i in range(len(nums)):
        if nums[i] == 0:
            for k in range(i, len(nums)):
                if nums[k] != 0:
                    nums[i], nums[k] = nums[k], nums[i]
                    break
    