class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Saves memory as we use an approach similar to that of two pointers. To be specific they act as comparison variables.
        nums.sort()

        i = 0
        k = i + 1
        while i < len(nums) and k < len(nums):
            if nums[i] == nums[k]:
                return True
            if nums[i] != nums[k]:
                i = k
            k += 1
        
        return False

        #Faster than the above code but memory weighs in here. 
        lookup = set()

        for num in nums:
            if num in lookup:
                return True
            lookup.add(num)

        return False





