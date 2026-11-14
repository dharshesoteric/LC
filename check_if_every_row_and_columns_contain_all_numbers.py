class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        

        for i in range(len(matrix)):

            rows = set()
            columns = set()

            for j in range(len(matrix)):

                rows.add(matrix[i][j])
                columns.add(matrix[j][i])
            
            if len(rows) != len(matrix) or len(columns) != len(matrix):
                return False
        
        return True
