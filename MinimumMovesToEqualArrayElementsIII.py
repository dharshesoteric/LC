class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        maxVal = max(nums)

        moves = 0

        for num in nums:

            moves += maxVal - num
        
        return moves
