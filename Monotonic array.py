class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        

        ascending = True
        descending = True


        for i in range(1, len(nums)):
            if not ascending and not descending:
                return False
            curr = nums[i]
            prev = nums[i - 1]
            
            if not curr >= prev:
                ascending = False
            if not curr <= prev:
                descending = False

        return ascending or descending