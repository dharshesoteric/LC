class Solution:
    def maxProduct(self, n: int) -> int:
        
        sortedList = [int(x) for x in str(n)]
        sortedList.sort()
        return sortedList[-1] * sortedList[-2]
                
        