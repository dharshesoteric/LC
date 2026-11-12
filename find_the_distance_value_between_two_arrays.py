class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:

        
        near_elements = 0

        arr2.sort()

        for i in range(len(arr1)):
            
            l, r = 0, len(arr2) - 1

            while l <= r:

                mid = l + (r - l) // 2

                if abs(arr2[mid] - arr1[i]) <= d:
                    near_elements += 1
                    break
                elif arr2[mid] < arr1[i]:
                    l = mid + 1
                else:
                    r = mid - 1 


        return len(arr1) - near_elements
            




        

        