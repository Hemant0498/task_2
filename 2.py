import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.human_player = 'X'
        self.ai_player = 'O'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}')
            if i < 6:
                print('-' * 9)

    def is_board_full(self):
        return ' ' not in self.board

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(0, 3):
            if all(self.board[i * 3 + j] == player for j in range(3)) or \
               all(self.board[j * 3 + i] == player for j in range(3)):
                return True
        if all(self.board[i] == player for i in [0, 4, 8]) or \
           all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def is_game_over(self):
        return self.is_winner(self.human_player) or self.is_winner(self.ai_player) or self.is_board_full()

    def get_empty_cells(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, player, position):
        self.board[position] = player

    def undo_move(self, position):
        self.board[position] = ' '

    def get_best_move(self):
        _, best_move = self.minimax(self.ai_player)
        return best_move

    def minimax(self, player):
        if self.is_winner(self.human_player):
            return -1
        elif self.is_winner(self.ai_player):
            return 1
        elif self.is_board_full():
            return 0

        empty_cells = self.get_empty_cells()

        if player == self.ai_player:
            best_score = float('-inf')
            for cell in empty_cells:
                self.make_move(player, cell)
                score = self.minimax(self.human_player)
                self.undo_move(cell)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for cell in empty_cells:
                self.make_move(player, cell)
                score = self.minimax(self.ai_player)
                self.undo_move(cell)
                best_score = min(score, best_score)
            return best_score

# Main game loop
def play_tic_tac_toe():
    game = TicTacToe()
    human_turn = random.choice([True, False])

    while not game.is_game_over():
        game.print_board()

        if human_turn:
            try:
                move = int(input('Enter your move (1-9): ')) - 1
                if game.board[move] == ' ':
                    game.make_move(game.human_player, move)
                    human_turn = not human_turn
                else:
                    print('Invalid move. Cell already taken. Try again.')
            except (ValueError, IndexError):
                print('Invalid input. Please enter a number between 1 and 9.')
        else:
            ai_move = game.get_best_move()
            game.make_move(game.ai_player, ai_move)
            human_turn = not human_turn

    game.print_board()

    if game.is_winner(game.human_player):
        print('You win! Congratulations!')
    elif game.is_winner(game.ai_player):
        print('You lose. Better luck next time.')
    else:
        print('It\'s a draw!')

# Run the game
play_tic_tac_toe()
