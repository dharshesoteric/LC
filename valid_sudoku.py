class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = defaultdict(set)
        columns = defaultdict(set)
        grids = defaultdict(set)

        #Traversal for checking the integrity of rows, columns and grids

        for i in range(len(board)):

            box = (i // 3) * 3
            
            for j in range(len(board)):

                if board[i][j] in rows[i]:
                    return False
                
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                
                if board[j][i] in columns[i]:
                    return False

                if board[j][i] != '.':
                    columns[i].add(board[j][i])
                
                if board[i][j] in grids[box + (j // 3)]:
                    return False
                
                if board[i][j] != '.':
                    grids[box + (j // 3)].add(board[i][j])
                
        return True
                
