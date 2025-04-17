from player import GeniusComputerPlayer, HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')    

    def available_moves(self):
        moves = []
        for i, spot in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves       

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    

    def winner(self , square , letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game , x_player , o_player , print_game=True):
    letter = 'X'  # Starting letter

    while game.empty_squares():
        if game.num_empty_squares() == 1:
            square = game.available_moves()[0]
        else:
            square = x_player.get_move(game) if letter == 'X' else o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # Empty line

            if game.current_winner:  # Check for a winner
                if print_game:
                    print(letter + ' wins!')
                return letter  # Ends the loop and exits the game
                
            letter = 'O' if letter == 'X' else 'X'  # Switches player

    if print_game:  
        print('It\'s a tie!')

if __name__ == '__main__':
    X_player = HumanPlayer('X')
    O_player = GeniusComputerPlayer('O')  
    t = TicTacToe()
    play(t, X_player, O_player, print_game=True)
