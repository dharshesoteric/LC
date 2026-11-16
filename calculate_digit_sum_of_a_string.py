class Solution:
    def digitSum(self, s: str, k: int) -> str:
        

        copy = s

        if len(copy) <= k:
            return copy        
        
        while True:

            res = ""
            string_builder = ""

            for i in range(1, len(copy) + 1):
                
                string_builder += copy[i - 1]

                if i % k == 0:

                    d_sum = 0

                    for string in string_builder:
                        
                        d_sum += int(string)
                    
                    res += str(d_sum)
                    string_builder = ""

                    if i == len(copy):
                        break
                
                if i == len(copy):
                    
                    d_sum = 0

                    for string in string_builder:

                        d_sum += int(string)
                    
                    res += str(d_sum)
            
            if len(res) <= k:
                return res
            else:
                copy = res

                


