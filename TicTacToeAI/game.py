class Game:
    size = 3
    n_turns = 0
    board = []
    def __init__(self):
        self.board = [[' ' for i in range(self.size)] for j in range(self.size)]


    def display(self):
        print(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("---|---|---")
        print(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("---|---|---")
        print(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")


    def make_move(self, x, y):
        if(self.board[x][y] == ' '):
            if(self.n_turns % 2 == 0):
                self.board[x][y] = 'X'
            else:
                self.board[x][y] = 'O'
            self.n_turns += 1
            return True

        return False


    def undo(self, x, y):
        self.board[x][y] = ' '
        self.n_turns -= 1


    def check_win(self):
        for i in range(self.size):
            if(self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != ' '):
                return self.board[i][0]
        
            if(self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != ' '):
                return self.board[0][i]
        
        if(self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != ' '):
            return self.board[0][0]

        if(self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != ' '):
            return self.board[0][2]
        return False

def bestMove(g):
    # Initialize best score and move
    best_score = -1000
    best_i = 0
    best_j = 0

    # Loop through all possible moves
    for i in range(g.size):
        for j in range(g.size):
            # Check if the move is valid
            if(g.make_move(i, j)):
                # Calculate the score of the move
                score = minimax(g, False)
                # Undo the move
                g.undo(i, j)
                # Update the best score and move if necessary
                if(score > best_score):
                    best_score = score
                    best_i = i
                    best_j = j

    # Return the best move
    return best_i, best_j


def minimax(g, is_maximizing):
    # Check for win or draw
    if(g.check_win() == 'X'):
        return -10
    elif(g.check_win() == 'O'):
        return 10
    elif(g.n_turns == 9):
        return 0

    # Initialize best score
    if(is_maximizing):
        best_score = -1000
    else:
        best_score = 1000

    # Loop through all possible moves
    for i in range(g.size):
        for j in range(g.size):
            # Check if move is valid
            if(g.make_move(i, j)):
                # Recursively call minimax for next player
                score = minimax(g, not is_maximizing)
                # Undo move and update best score
                g.undo(i, j)
                if(is_maximizing):
                    best_score = max(score, best_score)
                else:
                    best_score = min(score, best_score)

    # Return best score
    return best_score


def play():
    g = Game()
    while(True):
        g.display()
        print("Enter your move: ")
        i = int(input())
        g.make_move((i - 1) // 3, (i - 1) % 3)
        if(g.check_win()):
            print("You win!")
            break
        if(g.n_turns == 9):
            print("Draw!")
            break
        i, j = bestMove(g)
        g.make_move(i, j)
        if(g.check_win()):
            print("You lose!")
            break

play()