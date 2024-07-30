board = [' ' for _ in range(9)]
def print_board(board):
  for i in range(3):
    print(board[i*3: (i+1)*3])
def get_player_input(player):
  while True:
    try:
      position = int(input(f"Player {player}, enter your move (1-9): "))
      if 1 <= position <= 9 and board[position-1] == ' ':
        return position - 1
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")
def check_win(board, player):
  win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
    [0, 4, 8], [2, 4, 6]             # diagonal
  ]
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False
def play_game():
  current_player = 'X'
  game_over = False

  while not game_over:
    print_board(board)
    position = get_player_input(current_player)
    board[position] = current_player

    if check_win(board, current_player):
      print_board(board)
      print(f"Player {current_player} wins!")
      game_over = True
    elif ' ' not in board:
      print_board(board)
      print("It's a tie!")
      game_over = True

    current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
  play_game()
