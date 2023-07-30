class Solution(object):

 
            
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        arr = []
        arr0 = []

        for x in range(9):
            arr.append(set())
        
        
        arr0 = [[0 for x in range(3)] for y in range(3)]
        for x in range(3):

            for y in range(3):
                arr0[x][y] = set()


        for x in range(9):

            hs = set()
            for y in range(9):
                if(board[x][y] != '.'):
                    if (board[x][y] in hs) or (board[x][y] in arr[y]):
                        return False
                    
                    x0 = x / 3 
                    y0 = y / 3

                    if (board[x][y] in arr0[x0][y0]):
                        return False
                    
                    

                    
                    hs.add(board[x][y])
                    arr[y].add(board[x][y])
                    arr0[x0][y0].add(board[x][y])
            
        return True
       
                    