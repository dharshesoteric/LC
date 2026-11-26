class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        if n < 10:
            return False

        x = 10

        while n > 0:

            if n - x > 0:
                n -= x
                if x - 1 > 0:
                    x -= 1
                    
            elif n - x == 0:
                if x % 2 == 0:
                    return True
                else:
                    return False
            else:
                if x % 2 == 0:
                    return False
                else:
                    return True
