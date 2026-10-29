class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        

        length = len(nums)
        res = []

        
        i = 1
        while i <= length:

            if i == 1:
                i += 1
                continue
            
            else:
                l, r = 0, i

                while r <= length:

                    subArray = nums[l : r]
                    res.append(len(set(subArray)))
                    l += 1
                    r += 1

            i += 1
        

        return sum([x ** 2 for x in res]) + length









