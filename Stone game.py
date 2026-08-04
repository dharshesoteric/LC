class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        alice = 0
        bob = 0

        i = 0

        length = len(piles)

        while i < length:
            if i % 2 == 0:
                ind = piles.index(max(piles))
                alice += piles.pop(ind)
            else:
                Ind = piles.index(max(piles))
                bob += piles.pop(Ind)
            
            i += 1
        
        return True if alice > bob else False
