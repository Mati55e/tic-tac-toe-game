import os

game_board = """
     a     b     c
        |     |     
 1   -  |  -  |  -  
   _____|_____|_____
        |     |     
 2   -  |  -  |  -  
   _____|_____|_____
        |     |     
 3   -  |  -  |  -  
        |     |     """

board_positions = {"a1": 0, "b1": 1, "c1": 2, "a2": 3, "b2": 4, "c2": 5, "a3": 6, "b3": 7, "c3": 8}
game_progress = [46, 52, 58, 109, 115, 121, 172, 178, 184]

def update_board(player, gp_index):
    global game_board
    global game_progress
    position = game_progress[gp_index]
    game_board = game_board[:position] + player + game_board[position+1:]
    game_progress[gp_index] = player
    os.system('cls')
    print(game_board.replace("-", " "))

def get_player_input(player):
    """Gets the index for the game_progress list."""
    while True:
        player_input = input(f"Where would you like to place your '{player}'? Example: a1, b3, c2..\n")
        if player_input in board_positions:
            input_to_num = board_positions[player_input]
            if game_progress[input_to_num] != "x" and game_progress[input_to_num] != "o":
                return input_to_num
        os.system('cls')
        print(game_board.replace("-", " "))
        print("Please choose a correct location.")
                
def check_game_over():
    if game_progress[0] == game_progress[1] == game_progress[2]:
        return True
    elif game_progress[3] == game_progress[4] == game_progress[5]:
        return True
    elif game_progress[6] == game_progress[7] == game_progress[8]:
        return True
    
    elif game_progress[0] == game_progress[3] == game_progress[6]:
        return True
    elif game_progress[1] == game_progress[4] == game_progress[7]:
        return True
    elif game_progress[2] == game_progress[5] == game_progress[8]:
        return True

    elif game_progress[0] == game_progress[4] == game_progress[8]:
        return True
    elif game_progress[2] == game_progress[4] == game_progress[6]:
        return True
    
    else:
        return False

game_over = False
player = "o"
os.system('cls')
print(game_board.replace("-", " "))

while not game_over:
    player_choice = get_player_input(player=player)
    update_board(player, player_choice)
    game_over = check_game_over()
    if game_over:
        print(f"Player '{player}' has won the game.")
        break
    if player == "o":
        player = "x"
    elif player == "x":
        player = "o"

