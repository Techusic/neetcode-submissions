class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        waist = set()
        ass = set()
        boob1 = set()
        boob2 = set()
        boobs = set()
        for i in range(9):

            for j in range(9):

                if j < 3:
                    if board[i][j] in boob1 and board[i][j] != ".":
           
                        return False
                    boob1.add(board[i][j])
        
                if j > 2 and j < 6:
                    if board[i][j] in boob2 and board[i][j] != ".":
   
                        return False
                    boob2.add(board[i][j])

                if j > 5:
                    if board[i][j] in boobs and board[i][j] != ".":
           
                        return False
                    boobs.add(board[i][j])

                if board[i][j] in ass and board[i][j] != ".":

                    return False
                ass.add(board[i][j])

                if board[j][i] in waist and board[j][i] != ".":   
       
                    return False
                waist.add(board[j][i])

            if (i+1)%3 == 0:
                boob1.clear()
                boob2.clear()
                boobs.clear()

            ass.clear()
            waist.clear()
        return True
        