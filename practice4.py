class Nqueens:
    def __init__(self) -> None:
        self.size = int(input("Enter size: "))
        self.board = [[False for i in range(self.size)] for i in range(self.size)]
        self.count = 0

    def PrintBoard(self):
        for row in self.board:
            for ele in row:
                if ele == True:
                    print('Q', end = ' ') 
                else:
                    print('X', end = ' ')
            print()
        print()

    def isSafe(self, row: int, col: int) -> bool:

        for i in self.board:
            if i[col] == True:
                return False 
        
        i = row
        j = col
        # \ upward
        while i >= 0 and j >= 0:
            if self.board[i][j] == True:
                return False
            i-=1
            j-=1
        
        i = row
        j = col        
        # \ downward
        while i < self.size and j < self.size:
            if self.board[i][j] == True:
                return False
            i+=1
            j+=1
        
        i = row
        j = col
        # / upward
        while i >= 0 and j < self.size:
            if self.board[i][j] == True:
                return False
            i-=1
            j+=1
        
        i = row
        j = col        
        # / downward
        while i < self.size and j >= 0:
            if self.board[i][j] == True:
                return False
            i+=1
            j-=1
        
        return True

    def SetFirstQueen(self):
        row = int(input(f"Enter row between (1, {self.size}): "))
        col = int(input(f"Enter col between (1,{self.size}): "))
        self.board[row-1][col-1] = True
        self.PrintBoard()

    def solve(self, row:int):
        if row == self.size:
            self.count+=1
            self.PrintBoard()
            return
        
        if any(self.board[row]) is True:
            self.solve(row+1)
            return
        
        for col in range(self.size):
            if self.isSafe(row, col):
                self.board[row][col] = True
                self.solve(row+1)
                self.board[row][col] = False

    def displayMessage(self):
        if self.count > 0:
            print("Solution exists for the given position of the queen.")
        else:
            print("Solution doesn't exist for the given position of the queen.")

solver = Nqueens()
solver.SetFirstQueen()
solver.solve(0)
solver.displayMessage()