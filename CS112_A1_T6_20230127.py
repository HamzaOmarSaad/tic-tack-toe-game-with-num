#  File:CS112_A1_T6_1_20230127.py
#  Purpose:it is a tic tac toe game but winning here when a player making a row or a column or a diagonal summation equal to 15
#  name: Hamza Omar Saad
# section : not registerd yet
#  ID : 20230127
#date :1/3/2024

def win():
    # if sum of row are 15 then its a win
    for row in board:
        if sum(row) == 15:
            return True
 # if sum of columns are 15 then its a win
    for col in range(0,3):
        if board[0][col] + board[1][col] + board[2][col] == 15:
            return True
 # if sum of diagonals  are 15 then its a win
    if board[0][0] + board[1][1] + board[2][2] == 15 or board[0][2] + board[1][1] + board[2][0] == 15:
        return True

    return False
 #board where the game will be
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# identifying the player choices 
player_one_choices = [1, 3, 5, 7, 9] # player one choose odd num 
player_two_choices = [0, 2, 4, 6, 8]# player two choose even num 

while True:
    print(board)
    player_1_move = int(input("Player one choose odd num: "))
    # if player one choise not an odd num tthen its wrong 
    if player_1_move not in player_one_choices:
        print("Wrong input")
        break
    
    row = int(input("Enter the row: "))
    column = int(input("Enter the column: "))
    # updating game status 
    board[row-1][column-1] = player_1_move
    player_one_choices.remove(player_1_move)

    if win():
        print("Player one is the winner")
        break 

    print(board)
 # if player two choise not an odd num tthen its wrong 
    player_2_move = int(input("Player two choose even num: "))
    if player_2_move not in player_two_choices:
        print("Wrong input")
        break

    row = int(input("Enter the row: "))
    column = int(input("Enter the column: "))
    # updating game status
    board[row-1][column-1] = player_2_move
    player_two_choices.remove(player_2_move)

    if win():
        print("Player two is the winner")
        break
