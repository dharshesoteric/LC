class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        if target not in words:
            return -1
        
        distance = float('inf')
        leftDistance = 0
        rightDistance = 0
        
        #Traversing the left side of the array
        LTindex = startIndex
        while True:
            
            if words[LTindex] == target:
                distance = min(distance, leftDistance)
                break
            
            leftDistance += 1
            LTindex -= 1

        #Traversing the right side of the array
        RTindex = startIndex
        while True:
            if RTindex == len(words) - 1 and words[RTindex] != target:
                RTindex = 0
                rightDistance += 1
            
            if words[RTindex] == target:
                distance = min(distance, rightDistance)
                break
            
            rightDistance += 1
            RTindex += 1
        
        return distance
        
                            