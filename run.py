import keyboard
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

game_mode_status = "PENDING"
board_size = "PENDING"
team_selection = "PENDING"
play_status = "LOCKED"

def begin_game():
    global board_size
    if board_size == "DEFAULT":
        display_board_normal()
    elif board_size == " LARGE ":
        display_board_large()
    else: 
        display_board_xlarge()

def display_board_normal():
    print("                                      ")
    print("--------------------------------------------")
    print(f"Game mode:{game_mode_status}, Board Size: {board_size}")
    print("--------------------------------------------")
    print("|                                          |")
    print("|           A  B  C  D  E  F  G  H         |")
    print("|                                          |")
    print("|      0    O  -  &  -  O  -  0  -         |")
    print("|      1    -  O  -  O  -  @  -  O         |")
    print("|      2    O  -  O  -  O  -  O  -         |")
    print("|      3    -  -  -  -  -  -  -  -         |")
    print("|      4    -  -  -  -  -  -  -  -         |")
    print("|      5    X  -  X  -  X  -  X  -         |")
    print("|      6    -  X  -  X  -  X  -  X         |")
    print("|      7    #  -  X  -  X  -  X  -         |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|__________________________________________|")
    input("")
    clear()
    print("To Be Continued...")

def e_start_game():
    global play_status
    if play_status != "LOCKED":
        print("--------------------------------------------")
        print("|                                          |")
        print("|***************BEGIN GAME*****************|")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|           LET'S PLAY CHECKERS !          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|        [PRESS ENTER TO CONTINUE]         |")
        print("--------------------------------------------")
        input("")
        clear()
        begin_game()
    else:
        print("--------------------------------------------")
        print("|                                          |")
        print("|******** GAME LOCKED UNTIL SETUP *********|")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|           PLEASE COMPLETE GAME           |")
        print("|              SETUP OPTIONS               |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|        [PRESS ENTER TO CONTINUE]         |")
        print("--------------------------------------------")
        input("")
        clear()
        setup_screen()

def d_view_rules():
    print("--------------------------------------------")
    print("|****************GAME RULES****************|")
    print("|                                          |")
    print("| 1. Objective of the game is to capture   |")
    print("|    all of the opposition's pieces        |")
    print("|                                          |")
    print("| 2. Pieces can normally only move one     |")
    print("|    square - diagonally and forwards      |")
    print("|                                          |")
    print("| 3. An opposition piece is captured       |")
    print("|    by jumping diagonally over it         |")
    print("|                                          |")
    print("| 4. The capture of an opposition piece    |")
    print("|    is a compulsory move if possible      |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("--------------------------------------------")
    setup = input("")
    clear()        
    setup_screen()

def c_side_selection():
    print("--------------------------------------------")
    print("|                                          |")
    print("|***********PLEASE CHOOSE A SIDE***********|")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|             A. NOUGHTS [ O ]             |")
    print("|                                          |")
    print("|                                          |")
    print("|             B. CROSSES [ X ]             |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|             [PLEASE SELECT]              |")
    print("|                                          |")
    print("--------------------------------------------")
    setup = input("Select option A or B: ")
    if setup.upper() == "A":
        clear()
        side_selected_A()    
    elif setup.upper() == "B":            
        clear()        
        side_selected_B()
    else:
        print("Please make a valid choice")

def side_selected_A():
    global team_selection 
    team_selection = "NOUGHTS"
    print("                                      ")
    print("--------------------------------------------")
    print("        You have chosen Team Noughts        ")
    print("--------------------------------------------")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|          TEAM NOUGHTS SELECTED           |")
    print("|                                          |")
    print("|                  [ O ]                   |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("|__________________________________________|")
    input("")
    clear()
    
    setup_screen()

def side_selected_B():
    global team_selection 
    team_selection = "CROSSES"
    print("                                      ")
    print("--------------------------------------------")
    print("        You have chosen Team Crosses        ")
    print("--------------------------------------------")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|          TEAM CROSSES SELECTED           |")
    print("|                                          |")
    print("|                  [ X ]                   |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("|__________________________________________|")
    input("")
    clear()
    setup_screen()

def select_board_normal():
    global board_size 
    board_size = "DEFAULT"
    print("                                      ")
    print("--------------------------------------------")
    print("You have chosen Board Size: Standard (8 x 8)")
    print("--------------------------------------------")
    print("|                                          |")
    print("|           A  B  C  D  E  F  G  H         |")
    print("|                                          |")
    print("|      0    O  -  &  -  O  -  0  -         |")
    print("|      1    -  O  -  O  -  @  -  O         |")
    print("|      2    O  -  O  -  O  -  O  -         |")
    print("|      3    -  -  -  -  -  -  -  -         |")
    print("|      4    -  -  -  -  -  -  -  -         |")
    print("|      5    X  -  X  -  X  -  X  -         |")
    print("|      6    -  X  -  X  -  X  -  X         |")
    print("|      7    #  -  X  -  X  -  X  -         |")
    print("|                                          |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("|__________________________________________|")
    input("")
    clear()
    setup_screen()

def select_board_large():
    global board_size 
    board_size = " LARGE "
    print("                                      ")
    print("-------------------------------------------")
    print("You have chosen Board Size: Large (9 x 9)  ")
    print("-------------------------------------------")
    print("|                                          |")
    print("|           A  B  C  D  E  F  G  H  I      |")
    print("|                                          |")
    print("|      0    O  -  O  -  O  -  O  -  O      |")
    print("|      1    -  O  -  O  -  O  -  O  -      |")
    print("|      2    O  -  O  -  O  -  O  -  O      |")
    print("|      3    -  -  -  -  -  -  -  -  -      |")
    print("|      4    -  -  -  -  -  -  -  -  -      |")
    print("|      5    -  -  -  -  -  -  -  -  -      |")
    print("|      6    -  X  -  X  -  X  -  X  -      |")
    print("|      7    X  -  X  -  X  -  X  -  X      |")
    print("|      8    -  X  -  X  -  X  -  X  -      |")
    print("|                                          |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("|__________________________________________|")
    input("")
    clear()
    setup_screen()

def select_board_extralarge():
    global board_size 
    board_size = "X-LARGE"
    print("                                         ")
    print("-------------------------------------------------")
    print("You have chosen Board Size: Extra-Large (10 x 10)")
    print("-------------------------------------------------")
    print("|                                               |")
    print("|                                               |")
    print("|           A  B  C  D  E  F  G  H  I  J        |")
    print("|                                               |")
    print("|      0    O  -  O  -  O  -  O  -  O  -        |")
    print("|      1    -  O  -  O  -  O  -  O  -  O        |")
    print("|      2    O  -  O  -  O  -  O  -  O  -        |")
    print("|      3    -  -  -  -  -  -  -  -  -  -        |")
    print("|      4    -  -  -  -  -  -  -  -  -  -        |")
    print("|      5    -  -  -  -  -  -  -  -  -  -        |")
    print("|      6    -  -  -  -  -  -  -  -  -  -        |")
    print("|      7    X  -  X  -  X  -  X  -  X  -        |")
    print("|      8    -  X  -  X  -  X  -  X  -  X        |")
    print("|      9    X  -  X  -  X  -  X  -  X  -        |")
    print("|                                               |")
    print("|                                               |")
    print("|        [PRESS ENTER TO CONTINUE]              |")
    print("|_______________________________________________|")
    input("")
    clear()
    setup_screen()

def b_select_board_size():

    print("--------------------------------------------")
    print("|                                          |")
    print("|************SELECT BOARD SIZE*************|")
    print("|                                          |")
    print("|                                          |")
    print("|    A. STANDARD                           |")
    print("|                                          |")
    print("|    B. LARGE                              |")
    print("|                                          |")
    print("|    C. EXTRA-LARGE                        |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|            [PLEASE SELECT]               |")
    print("|                                          |")
    print("--------------------------------------------")
    setup = input("Select option A, B or C: ")
    if setup.upper() == "A":
        clear()
        select_board_normal()
    elif setup.upper() == "B":            
        clear()        
        select_board_large()
    elif setup.upper() == "C":            
        clear()        
        select_board_extralarge()        
    else:
        print("Please make a valid choice")

def a_select_game_mode():

    print("--------------------------------------------")
    print("|                                          |")
    print("|************SELECT GAME MODE**************|")
    print("|                                          |")
    print("|                                          |")
    print("|    A. Player1    vs.    Computer         |")
    print("|                                          |")
    print("|                                          |")
    print("|    B. Player1    vs.    Player2          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|            [PLEASE SELECT]               |")
    print("|                                          |")
    print("--------------------------------------------")
    setup = input("Select option A or B: ")
    if setup.upper() == "A":
        clear()
        game_mode_A()    
    elif setup.upper() == "B":            
        clear()        
        game_mode_B()
    else:
        print("Please make a valid choice")

def game_mode_A():
    global game_mode_status 
    game_mode_status = "P vs. C"
    print("--------------------------------------------")
    print("|                                          |")
    print("|************SELECT GAME MODE**************|")
    print("|                                          |")
    print("|                                          |")
    print("|      YOU HAVE SELECTED GAME MODE: A      |")
    print("|                                          |")
    print("|                                          |")
    print("|        PLAYER1    vs.   COMPUTER         |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("|                                          |")
    print("|                                          |")
    print("--------------------------------------------")
    input("")
    clear()
    setup_screen()

def game_mode_B():
    global game_mode_status 
    game_mode_status = "P vs. P"
    print("--------------------------------------------")
    print("|                                          |")
    print("|************SELECT GAME MODE**************|")
    print("|                                          |")
    print("|                                          |")
    print("|      YOU HAVE SELECTED GAME MODE: B      |")
    print("|                                          |")
    print("|                                          |")
    print("|        PLAYER1    vs.   PLAYER2          |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|        [PRESS ENTER TO CONTINUE]         |")
    print("|                                          |")
    print("|                                          |")
    print("--------------------------------------------")
    input("")
    clear()
    setup_screen()

def welcome_screen():
    print("--------------------------------------------")
    print("|                                          |")
    print("|    W  E  L  C  O  M  E                   |")
    print("|                                          |")
    print("|       T O                                |")
    print("|                                          |")
    print("|          P  Y  T  H  O  N                |")
    print("|                                          |")
    print("|              C  H  E  C  K  E  R  S !    |")
    print("|                                          |")
    print("|                                          |")
    print("|                                          |")
    print("|         [PRESS ENTER TO BEGIN]           |")
    print("|                                          |")
    print("|                                          |")
    print("--------------------------------------------")    

welcome_screen()
input("")
clear()

def setup_screen():
    global play_status
    global game_mode_status 
    global board_size 
    global team_selection 
    if game_mode_status and board_size and team_selection != "PENDING":
        play_status = "READY!"
    else: 
        play_status = "LOCKED"
    print("--------------------------------------------")
    print("|                                          |")
    print("|************GAME SETUP MENU:**************|")
    print("|                                          |")
    print(f"|    A. GAME MODE            [{game_mode_status}]     |")
    print("|                                          |")
    print(f"|    B. BOARD SIZE           [{board_size}]     |")
    print("|                                          |")
    print(f"|    C. SIDE SELECTION       [{team_selection}]     |")
    print("|                                          |")
    print("|    D. VIEW RULES           [OPTIONAL]    |")
    print("|                                          |")
    print(f"|    E. PLAY CHECKERS!       [{play_status}]      |")
    print("|                                          |")
    print("|         [PLEASE COMPLETE SETUP]          |")
    print("|                                          |")
    print("--------------------------------------------")
    setup = input("Select option A to E: ")

    if setup.upper() == "A":
        clear()
        a_select_game_mode()
    elif setup.upper() == "B":
        clear()
        b_select_board_size()
    elif setup.upper() == "C":
        clear()
        c_side_selection()
    elif setup.upper() == "D":
        clear()
        d_view_rules()
    elif setup.upper() == "E":
        clear()
        e_start_game()
    else:
        print("Please make a valid choice")

setup_screen()




