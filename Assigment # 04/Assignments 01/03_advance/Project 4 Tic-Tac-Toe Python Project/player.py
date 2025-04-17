import math
import random

class Player:
    def __init__(self, letter):
        # Letter is 'X' or 'O'
        self.letter = letter

    # We want all players to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Randomly choose a square from available moves
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):  
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class GeniusComputerPlayer(Player):  # Fixed constructor name here
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # If it's the first move, pick randomly
            square = random.choice(game.available_moves())
        else:
            # Use minimax for subsequent moves
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # The maximizer (this player's letter)
        other_player = 'O' if player == 'X' else 'X'  # The minimizer (the other player's letter)

        # Check for terminal state
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}  # Tie

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximizing player's turn
        else:
            best = {'position': None, 'score': math.inf}  # Minimizing player's turn

        for possible_move in state.available_moves():
            # Try the move
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate a game after the move

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None

            sim_score['position'] = possible_move  # Update the position to the current move

            if player == max_player:  # Maximizing player's turn
                if sim_score['score'] > best['score']:
                    best = sim_score  # Update best score and position
            else:  # Minimizing player's turn
                if sim_score['score'] < best['score']:
                    best = sim_score  # Update best score and position

        return best