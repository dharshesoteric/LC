class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:


        #return sorted(list(set(range(min(nums), max(nums) + 1)) - set(nums)))

        res = []

        nums = set(nums)

        for i in range(min(nums), max(nums) + 1):
            if i not in nums:
                res.append(i)

        return res

        