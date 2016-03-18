class ConnectBoard:
    def __init__(self, width, height):
        # Define each of the board's attributes:
        # gameFinished is present to aggregate the result of the multiple recursive calls to checkWinnerHelper that finish at different timesself.
        # A list of lists was chosen as the data structure because run time would not be compromised since it is just being manipulated by index.
        self.players = []
        self.width = width
        self.height = height
        self.board = []
        self.ColCounts = [0] * width
        #ColMax maintains the highest piece so that the search to check if there's a winner doesn't make unnecessary calls and slow the run time.
        self.ColMax = 0
        self.currentPlayer = None
        self.gameFinished = False
        widthList = ["-"] * width

        # Create Board
        for i in range(height):
            self.board.append(list(widthList))


    # CheckIfWinner is optimized such that the max number of recursive calls is 4 for each case: horizontal, vertical, and diagonal.
    # Also, it will only check the spaces that have a piece in them, which reduces the run time massively for larger tables because
    # of ColMax and ColCounts evaluations in various places
    # Also, it won't start new checks for vertical and diagonal if the pieces aren't 3 spots lower than the piece at the highest point.
    # Other optimizations can be made such as an individual ColMax for each column but it's not feasible in such a trivially small case of Connect 4
    def checkIfWinner(self):
        def checkWinnerHelper(piece, count, Xcoord, Ycoord, method):
            if count == 4:
                print("Player with the piece " + piece + " won!")
                self.gameFinished = True
                return
            elif method == "horizontal":
                if Xcoord + 1 < self.width:
                    if self.board[Ycoord][Xcoord + 1] == piece:
                        return checkWinnerHelper(piece, count + 1, Xcoord + 1, Ycoord, method)
            elif method == "vertical":
                if Ycoord + 1 < self.ColMax:
                    if self.board[Ycoord + 1][Xcoord] == piece:
                        return checkWinnerHelper(piece, count + 1, Xcoord, Ycoord + 1, method)
            elif method == "diagonal":
                if Ycoord + 1 < self.ColMax and Xcoord + 1 < self.width:
                    if self.board[Ycoord + 1][Xcoord + 1] == piece:
                        return checkWinnerHelper(piece, count + 1, Xcoord + 1, Ycoord + 1, method)
        for i, piece in enumerate(self.board[0]):
            if piece != "-":
                checkWinnerHelper(piece, 1, i, 0, "horizontal")
                checkWinnerHelper(piece, 1, i, 0, "vertical")
                checkWinnerHelper(piece, 1, i, 0, "diagonal")
        row = 1
        while self.gameFinished == False:
            for i, piece in enumerate(self.board[row]):
                if self.ColCounts[i] < row:
                    pass
                elif piece != "-":
                    checkWinnerHelper(piece, 1, i, row, "horizontal")
                    checkWinnerHelper(piece, 1, i, row, "vertical")
                    checkWinnerHelper(piece, 1, i, row, "diagonal")
            row += 1
            if row >= self.ColMax:
                return False



    def __str__(self):
        for i in range(self.height):
            print(self.board[self.height - 1 - i])
        return "                                 "

class Player:
    def __init__(self, piece, board):
        self.piece = piece
        if len(board.players) >= 2:
            print("This game is full")
        elif board.gameFinished == True:
            print("This Game has Finished - Please reset game board!")
        else:
            self.board = board
            self.board.players.append(self)

    def playPiece(self, column):
        if len(self.board.players) != 2:
            print("There aren't enough players")
        elif column >= self.board.width:
            print("Please pick a column in range")
        elif self.board.ColCounts[column] == self.board.height:
            print("This column is full!")
        elif self.board.currentPlayer == self:
            print("It's not your turn")
        elif sum(self.board.ColCounts) == self.board.width * self.board.height:
            print("It's a Draw! Please clear the game board before playing again")
        else:
            self.board.currentPlayer = self
            self.board.board[self.board.ColCounts[column]][column] = self.piece
            heightForColumn = self.board.ColCounts[column]
            self.board.ColCounts[column] = heightForColumn + 1
            if heightForColumn + 1 > self.board.ColMax:
                self.board.ColMax = heightForColumn + 1
            print(self.board)
            print("Checking for Winner...")

#Test for Diagonal Case
B = ConnectBoard(10,10)
player1 = Player("X", B)
player2 = Player("O", B)
player1.playPiece(2)
B.board = [['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', 'X', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'X', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', 'X', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
B.ColMax = 5
B.checkIfWinner()

#Test for Horizontal Case
A = ConnectBoard(10,10)
player1 = Player("X", A)
player2 = Player("O", A)
player1.playPiece(2)
A.board = [['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', 'X', '', '-', '-', '-', '-', '-', '-'], ['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
A.ColMax = 5
A.checkIfWinner()
