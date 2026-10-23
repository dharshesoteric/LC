class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:


        nums.sort()
        res = []

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                res.append(mid)
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if not res:
            return res
        else:
            left, right = mid - 1, mid + 1
            while left > -1:
                if nums[left] == target:
                    res.append(left)
                    left -= 1
                else:
                    break
            
            while right < len(nums):
                if nums[right] == target:
                    res.append(right)
                    right += 1
                else:
                    break
            
            return sorted(res)
                
                
        



        
