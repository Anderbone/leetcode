class GameEndException(Exception):
    pass

class AlreadyTakenException(Exception):
    pass

class TicTacToe:
    """
    @return: nothing
    """
    def __init__(self):
        self.gameEnd = 0
        self.board = [['-' for i in range(3)] for j in range(3)]
        self.currentMark = 'x'
        # print(self.board)

    def getCurrentPlayer(self):
        # return str(self.currentMark)+'player wins!'
        return str(self.currentMark)+'player wins!'

    def full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False

        self.gameEnd = 1
        return True

    def changePlayer(self):
        if self.currentMark == 'x':
            self.currentMark = 'o'
        else:
            self.currentMark = 'x'


    def move(self, row, col):
        if (self.gameEnd == 1):
            raise GameEndException()
        if self.board[row][col] != '-':
            raise AlreadyTakenException()

        self.board[row][col] = self.currentMark
# row
        win = 1

        for i in range(len(self.board)):
            if self.board[row][i] != self.currentMark:
                win = 0
                break
        if win:
            self.gameEnd = 1
            return True
#col
        win = 1

        for i in range(len(self.board)):
            if self.board[i][col] != self.currentMark:
                win = 0
                break
        if win:
            self.gameEnd = 1
            return True
#diagonal
        win = 1

        for i in range(len(self.board)):
            if self.board[i][i] != self.currentMark:
                win = 0
                break
        if win:
            self.gameEnd = 1
            return True
        #forward diagonal
        win = 1

        for i in range(len(self.board)):
            if self.board[i][len(self.board)-i-1] != self.currentMark:
                win = 0
                break
        if win:
            self.gameEnd = 1
            return True

        self.changePlayer()
        return False