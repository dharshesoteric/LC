class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        grids = defaultdict(set)

        #Traversal for checking the integrity of rows, columns and grids

        for i in range(len(board)):

            box = (i // 3) * 3

            rows = set()
            columns = set()
            
            for j in range(len(board)):

                if board[i][j] in rows:
                    return False
                
                if board[i][j] != '.':
                    rows.add(board[i][j])
                
                if board[j][i] in columns:
                    return False

                if board[j][i] != '.':
                    columns.add(board[j][i])
                
                if board[i][j] in grids[box + (j // 3)]:
                    return False
                
                if board[i][j] != '.':
                    grids[box + (j // 3)].add(board[i][j])
                
        return True
                
