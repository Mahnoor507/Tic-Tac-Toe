#game on going or not
game_is_going =True

winner= None

current_player="X"

board=["-","-","-",
       "-","-","-",
       "-","-","-"]
       

def display_board():
  print(board[0] + " | " +board[1] + " | " + board[2])
  print(board[3] + " | " +board[4] + " | " + board[5])
  print(board[6] + " | " +board[7] + " | " + board[8]) 


def play_game():
  #first display a board
  display_board()
  #unless a winner
  while game_is_going:
    #give turn tu player
    handle_turn(current_player)
    #check winner or tie
    check_if_game_over()
    #change player
    flip_player() 
  if winner == "X" or winner == "O":
    print(winner + " won wehee!")
  elif winner == None:
    print("Tie huh!")  

#handle turnsss
def handle_turn(player):
  print(player + "'s Turn.")
  position = input("Choose position from 1-9: ")
  #if position is empty to avoid over ridding
  valid=False
  #until position is empty
  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position=input("Choose position from 1-9: ")  
    position=int(position)-1
    #if position is empty place X or O 
    if board[position] == "-":
      valid = True
    else:  
      print("Already filled, choose another one")

  board[position]=player
  display_board()

def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():
  global winner

  row_winner = check_rows()

  col_winner = check_coloum()

  diag_winner = check_digaonalS()

  if row_winner:
    winner=row_winner
  elif col_winner:
    winner=col_winner
  elif diag_winner:
    winner=diag_winner
  else:
    winner=None      
  return

def check_rows():
  global game_is_going
  row_1 = board[0]==board[1]==board[2] != "-"
  row_2 = board[3]==board[4]==board[5] != "-"
  row_3 = board[6]==board[7]==board[8] != "-"
  
  if row_1 or row_2 or row_3:
    game_is_going =False

  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]      
  return



def check_coloum():
  global game_is_going
  col_1 = board[0]==board[3]==board[6] != "-"
  col_2 = board[1]==board[4]==board[7] != "-"
  col_3 = board[2]==board[5]==board[8] != "-"
  
  if col_1 or col_2 or col_3:
    game_is_going =False

  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return



def check_digaonalS():
  global game_is_going
  diag_1 = board[0]==board[4]==board[8] != "-"
  diag_2 = board[6]==board[4]==board[2] != "-"

  if diag_1 or diag_2 :
    game_is_going =False

  if diag_1:
    return board[0]
  elif diag_2:
    return board[6]
  return

def check_if_tie():
  global game_is_going
  # if no empty place boom
  if "-" not in board:
    game_is_going=False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"  
  return

play_game()