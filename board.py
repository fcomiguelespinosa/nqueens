from copy import copy
from db_manager import QueenSolution

class Board():
    def __init__(self,n): #Class Board receive the N parameter.
        self.__cells = [] # Cells  NxN are used only for printing the board.
        self.__n = n
        for i in range(n):
            self.__cells.append([0]*n)

    def returnDiagAsc(self,row,col):        # This funtion returns the number that identifies
        while(row>0 and col<(self.__n-1)):  # the diagonal value for any cell given. Values start from 0.
            row -= 1                        #  e.g. (0,0) = 0, (N,N) = 2*N-2, (0,N) =  N-1
            col += 1                        # Diagonal with positive slope.
        if row == 0:
            return col
        else:
            return (self.__n-1) + row

    def returnDiagDesc(self,row,col):       # This funtion also returns a diagonal number for each cell but
        while(col>0 and row>0):             # this has a diferent direction, it has a negative slope.
            row -= 1                        # e.g (0,0) = N-1, (N,N) = N-1, (0,N) = 0
            col -= 1
        if col == 0:
            return (self.__n-1) - row
        else:
            return (self.__n-1) + col

    def findSolutions(self):
        solutions, diag_asc, diag_desc, stack_inBoard = [], [], [], []  # I use multiple lists to check what are the columns availables,
        cols, queens = [], [[],[]]                                      # and when a queen's position is given if there are other
        founds, i_queen, j  = 0, 0, 0                                    # queens in thesame diagonal.

        for i in range (self.__n):
            cols.append(i)       # List of columns without queen
            queens[0].append(i)  # Queen 1 is in row 1 ... Queen N is in row N
            queens[1].append(-1) # Queen are going to be moved throught columns but row's number are fixed.

        while j < self.__n:
            while j < len(cols): # Iterate over the list of columns without queen
                da = self.returnDiagAsc(i_queen, cols[j]) # Check if there is other queen in both diagonals
                dd = self.returnDiagDesc(i_queen,  cols[j])
                if not da in diag_asc and not dd in diag_desc: # -If the diagonal is free it can assign
                    queens[1][i_queen] = cols[j]               #   this position.
                    diag_asc.append(da)                        # -Add the number of diagonal to the list of diagonals to
                    diag_desc.append(dd)                       #   know that there is a queen in this diagonal-
                    cols.remove(cols[j])                       # -Remove the column of the list of colums without queen.
                    stack_inBoard.append(j)                    # -This "stack" saves the order of movements it's used to
                    j = 0                                      #   go back when there is a unsolvable point.
                    i_queen += 1
                else:
                    j += 1
                if len(cols) == 0: # When there aren't elements in the array it means that all queens have been positioned.
                    solutions.append(QueenSolution(queen_rows=copy(queens[0]), queen_cols=copy(queens[1])))
                    founds += 1    # One solution found :)
            if j < self.__n:    # When there is a unsolvable point go back to remove the last queen positioned.
                i_queen -= 1
                cols.insert(stack_inBoard.pop(), queens[1][i_queen])      # Restore the column that had the last queen
                diag_asc.remove(self.returnDiagAsc(i_queen, queens[1][i_queen])) # Remove the last queen's diagonal of the lists of
                diag_desc.remove(self.returnDiagDesc(i_queen, queens[1][i_queen]))  # diagonals with a queen.
                j = cols.index(queens[1][i_queen]) +1
                queens[1][i_queen] = -1
        return [founds,solutions]                # Return the number of solutions founds and these solutions.

    def printBoard(self, queen_rows, queen_cols):   # Print the board like this:
        for i in queen_rows:                        # [0, 0, 1, ... 0]
            self.__cells[i] = ([0]*self.__n)        # [1, 0, 0, ... 0]
            j = queen_cols[i]                       # [0, 0, 0, ... 0]
            if j != -1:                             # ...
                self.__cells[i][j] = 1              # [0, 0 ,0, ... 1]
        for row in self.__cells:                    # It's used only for testing and debugging.
            print(row)
        print("-"*self.__n*3)
