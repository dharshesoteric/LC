class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        divisibleNum = n
    
        while True:
            val = 1
            for i in str(divisibleNum):
                val *= int(i)
            
            if val % t == 0:
                return divisibleNum
            else:
                divisibleNum += 1
        



