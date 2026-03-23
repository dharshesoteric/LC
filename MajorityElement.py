class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_lookup = {}
        
        for num in nums:
            freq_lookup[num] = freq_lookup.get(num, 0) + 1
            if freq_lookup[num] > (len(nums) // 2):
                return num
        