class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # visited set when i get one 'O'
        # dfs, if it goes to edge of the board then, continue
        # backtrak and make sure that every cell is surrounf by three X or four X

        # if not board or len(board) == 1 or len(board[0]) == 1:
        #     return

        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != "O":
                return
            
            board[i][j] = "E"

            for dir_i, dir_j in directions:
                dfs(i + dir_i, j + dir_j)
        
        for n in range(rows):
            dfs(n, 0)
            dfs(n, cols - 1)
        
        for n in range(cols):
            dfs(0, n)
            dfs(rows - 1, n)

        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"

            


            

        
     