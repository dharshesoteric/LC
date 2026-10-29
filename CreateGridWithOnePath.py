class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        

        res = []

        for i in range(m):

            string = ""

            for j in range(n):

                if i == m - 1:
                    string += '.'
                else:
                    if j == 0:
                        string += '.'
                    else:
                        string += '#'

            res.append(string)

        return res 
