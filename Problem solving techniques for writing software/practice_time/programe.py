def main():
    print()
    print("Welcome to Connect 4")
    print()

    # Create the 6x7 board
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]
    players = ["You", "Computer"]
    symbols = ["O", "X"]
    active_player_index = 0

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue

        # Toggle active player
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board:")
    show_board(board)
    print()


def choose_location(board, symbol):
    column = int(input("Choose the column (1-7): "))
    column -= 1  # Adjust to zero-based index

    # Check if column is in range
    if column < 0 or column >= len(board[0]):
        return False

    # Drop the disc to the lowest empty row in this column
    for row in reversed(range(len(board))):
        if board[row][column] is None:
            board[row][column] = symbol
            return True

    print("This column is full!")
    return False


def show_board(board):
    for row in board:
        print("| ", end="")
        for cell in row:
            symbol = cell if cell else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board")
    print()


def find_winner(board):
    sequences = get_winning_sequences(board)
    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True
    return False


def get_winning_sequences(board):
    sequences = []

    rows = len(board)
    cols = len(board[0])
    win_length = 4

    # Horizontal wins
    for row in board:
        for col in range(cols - win_length + 1):
            sequences.append(row[col:col + win_length])

    # Vertical wins
    for col in range(cols):
        for row in range(rows - win_length + 1):
            vertical = [board[row + i][col] for i in range(win_length)]
            sequences.append(vertical)

    # Diagonal (top-left to bottom-right)
    for row in range(rows - win_length + 1):
        for col in range(cols - win_length + 1):
            diagonal = [board[row + i][col + i] for i in range(win_length)]
            sequences.append(diagonal)

    # Diagonal (top-right to bottom-left)
    for row in range(rows - win_length + 1):
        for col in range(win_length - 1, cols):
            diagonal = [board[row + i][col - i] for i in range(win_length)]
            sequences.append(diagonal)

    return sequences


if __name__ == "__main__":
    main()
