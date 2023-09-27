class Game:
    size = 3
    n_turns = 0
    board = []
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for i in range(size)] for j in range(size)]

    
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
                return True
        
            if(self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] != ' '):
                return True
        
        if(self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != ' '):
            return True

        if(self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != ' '):
            return True

        
        return 0

def bestMove(g):
    best_score = -1000
    best_i = 0
    best_j = 0
    for i in range(g.size):
        for j in range(g.size):
            if(g.make_move(i, j)):
                score = minimax(g, True)
                g.undo(i, j)
                if(score > best_score):
                    best_score = score
                    best_i = i
                    best_j = j
    
    return best_i, best_j


def minimax(g, is_maximizing):
    if(g.check_win() and g.n_turns % 2 == 1):
        return -10
    
    elif(g.check_win() and g.n_turns % 2 == 0):
        return 10
    
    if(is_maximizing):
        best_score = -1000
        for i in range(g.size):
            for j in range(g.size):
                if(g.make_move(i, j)):
                    score = minimax(g, False)
                    g.undo(i, j)
                    best_score = max(score, best_score)
    
    else:
        best_score = 1000
        for i in range(g.size):
            for j in range(g.size):
                if(g.make_move(i, j)):
                    score = minimax(g, True)
                    g.undo(i, j)
                    best_score = min(score, best_score)

    return best_score

def play():
    g = Game(3)
    while(True):
        g.display()
        print("Enter your move: ")
        i = int(input())
        g.make_move((i - 1) // 3, (i - 1) % 3)
        if(g.check_win()):
            print("You is_win!")
            break
        i, j = bestMove(g)
        g.make_move(i, j)
        if(g.check_win()):
            print("You lose!")
            break

play()