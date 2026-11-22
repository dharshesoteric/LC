class Solution:
    def checkString(self, s: str) -> bool:
        

        a_indices = [-1]

        for i in range(len(s)):

            if s[i] == 'a':
                
                if abs((i - a_indices[-1])) > 1:
                    return False

                if a_indices[-1] == -1:
                    a_indices[-1] = i
                else:
                    a_indices.append(i)
    
        return True



