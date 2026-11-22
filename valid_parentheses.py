class Solution:
    def isValid(self, s: str) -> bool:

        brackets_lookup = {')':'(',']':'[','}':'{'}

        lookup = []
        
        for string in s:

            if string not in brackets_lookup:
                lookup.append(string)

            else:

                if lookup:
                
                    if lookup[-1] == brackets_lookup[string]:
                        lookup.pop()

                    else:
                        return False
                else:
                    return False
        
        if not lookup:
            return True
        else:
            return False
                
            
