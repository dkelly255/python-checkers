# Attempted rebuild from scratch
from os import system, name
from random import choice


def initialise_variables():
    # Initialise key variables
    # Answer bank & Word variables
    word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]
    answer = choice(word_list)
    answer_hidden = ["Guess The Word: "]
    answer_hidden.extend(["_ "] * len(answer))
    # Guess variables
    guesses_used = 0
    incorrect_guesses = 0
    previous_guesses = ["Previous Guesses: "]
    # Gallows variables
    gallows_stage = 0
    guesses_remaining = 9 - gallows_stage
    return word_list, answer, answer_hidden, guesses_remaining, guesses_used, incorrect_guesses, previous_guesses, gallows_stage


word_list, answer, answer_hidden, guesses_remaining, guesses_used, incorrect_guesses, previous_guesses, gallows_stage = initialise_variables()


def clear():
        """
        Clears the terminal for formatting purposes
        """
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


def welcome_screen():
        """
        Displays welcome screen to user upon loading
        the application. Allows proceeding to play
        the game upon pressing "Enter"
        """
        clear()
        print("--------------------------------------------")
        print("|                                          |")
        print("|                                          |")
        print("|       W  E  L  C  O  M  E                |")
        print("|                                          |")
        print("|          T O                             |")
        print("|                                          |")
        print("|             P  Y  T  H  O  N             |")
        print("|                                          |")
        print("|                 H  A  N  G  M  A  N      |")
        print("|                                          |")
        print("|                                          |")
        print("|                                          |")
        print("|         [PRESS ENTER TO BEGIN]           |")
        print("|                                          |")
        print("--------------------------------------------")
        input()
        clear()


def draw_gallows(gallows_stage):
    """
    Build up the hangman "gallows" element by
    element based on number of incorrect guesses
    """
    if gallows_stage == 0:
        print("   _________")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 1:
        print("   _________")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 2:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 3:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 4:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |       |")
        print("   |")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 5:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |       |")
        print("   |      /")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 6:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |       |")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 7:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |      /|")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")
    elif gallows_stage == 8:
        print("   _________")
        print("   |       |")
        print("   |       O")
        print("   |      /|\\")
        print("   |       |")
        print("   |      / \\")
        print("   |")
        print("   |")
        print("___|___________")
        print("XXXXXXXXXXXXXXX")
        print("    ")


def main_game_screen(guesses_used, guesses_remaining, incorrect_guesses):
    print("*Main Game Screen*\n")
    print("".join(answer_hidden))
    print(f"Guesses Used So Far: {guesses_used}")
    print(f"Guesses Remaining: {guesses_remaining}")
    print(f"Incorrect Guesses: {incorrect_guesses}")
    print("".join(previous_guesses))


def validate_guess(previous_guesses):
    while True:
        user_guess = input("Please guess a letter: ").lower()    
        if len(user_guess) == 1:
            if user_guess.isalpha():
                if not ((user_guess + ", ") in previous_guesses):
                    return user_guess
                print("You have already guessed this letter")
                continue
            print("Guess must be a letter, please try again")
            continue
        print("Guess must be a single character only, please try again")


def reveal_letter_in_answer(user_guess, answer, answer_hidden):
    
    for index, value in enumerate(answer,start=1):
        if user_guess == value:                    
            answer_hidden[index] = user_guess
    
    return answer_hidden


def answer_check(user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining):
        
    previous_guesses.append(user_guess + ", ") 
    guesses_used += 1
    

    if user_guess in answer:
        reveal_letter_in_answer(user_guess, answer, answer_hidden)
    else:
        gallows_stage += 1
        incorrect_guesses += 1
        guesses_remaining = 9 - gallows_stage

    return user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining


def play_game(previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining):
    while "_ " in answer_hidden:
        if gallows_stage == 8:
            print(f"Sorry You Lost - the answer was '{answer}'\n")
            break
        else:
            clear()            
            main_game_screen(guesses_used, guesses_remaining, incorrect_guesses)            
            draw_gallows(gallows_stage)
            print(f"1. Previous guesses = {previous_guesses}") 
            user_guess = validate_guess(previous_guesses)
            print(f"2. Previous guesses = {previous_guesses}")            
            user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining = answer_check(user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining)            
            clear()
        main_game_screen(guesses_used, guesses_remaining, incorrect_guesses)                    
        draw_gallows(gallows_stage)
        
        if not ("_ " in answer_hidden):               
            print(f"Congratulations You Won - the answer was '{answer}'\n")

welcome_screen()
play_game(previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining)

while True:
    stop_go = input("press y to play again or e to exit: ")
    if stop_go == "e":
        print("GOODBYE")
        break
    elif stop_go == "y":
        word_list, answer, answer_hidden, guesses_remaining, guesses_used, incorrect_guesses, previous_guesses, gallows_stage = initialise_variables()
        play_game(previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden, guesses_remaining)
    else:
        print("Please enter a valid choice - e to exit or y to play again: ")


# import keyboard
# def clear():
#     if name == 'nt':
#         _ = system('cls')
#     else:
#         _ = system('clear')

# game_mode_status = "PENDING"
# board_size = "PENDING"
# team_selection = "PENDING"
# play_status = "LOCKED"

# def begin_game():
#     global board_size
#     if board_size == "DEFAULT":
#         display_board_normal()
#     elif board_size == " LARGE ":
#         display_board_large()
#     else: 
#         display_board_xlarge()

# def display_board_normal():
#     print("                                      ")
#     print("--------------------------------------------")
#     print(f"Game mode:{game_mode_status}, Board Size: {board_size}")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|           A  B  C  D  E  F  G  H         |")
#     print("|                                          |")
#     print("|      0    O  -  &  -  O  -  0  -         |")
#     print("|      1    -  O  -  O  -  @  -  O         |")
#     print("|      2    O  -  O  -  O  -  O  -         |")
#     print("|      3    -  -  -  -  -  -  -  -         |")
#     print("|      4    -  -  -  -  -  -  -  -         |")
#     print("|      5    X  -  X  -  X  -  X  -         |")
#     print("|      6    -  X  -  X  -  X  -  X         |")
#     print("|      7    #  -  X  -  X  -  X  -         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     print("To Be Continued...")

# def e_start_game():
#     global play_status
#     if play_status != "LOCKED":
#         print("--------------------------------------------")
#         print("|                                          |")
#         print("|***************BEGIN GAME*****************|")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|           LET'S PLAY CHECKERS !          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|        [PRESS ENTER TO CONTINUE]         |")
#         print("--------------------------------------------")
#         input("")
#         clear()
#         begin_game()
#     else:
#         print("--------------------------------------------")
#         print("|                                          |")
#         print("|******** GAME LOCKED UNTIL SETUP *********|")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|           PLEASE COMPLETE GAME           |")
#         print("|              SETUP OPTIONS               |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|                                          |")
#         print("|        [PRESS ENTER TO CONTINUE]         |")
#         print("--------------------------------------------")
#         input("")
#         clear()
#         setup_screen()

# def d_view_rules():
#     print("--------------------------------------------")
#     print("|****************GAME RULES****************|")
#     print("|                                          |")
#     print("| 1. Objective of the game is to capture   |")
#     print("|    all of the opposition's pieces        |")
#     print("|                                          |")
#     print("| 2. Pieces can normally only move one     |")
#     print("|    square - diagonally and forwards      |")
#     print("|                                          |")
#     print("| 3. An opposition piece is captured       |")
#     print("|    by jumping diagonally over it         |")
#     print("|                                          |")
#     print("| 4. The capture of an opposition piece    |")
#     print("|    is a compulsory move if possible      |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("--------------------------------------------")
#     setup = input("")
#     clear()        
#     setup_screen()

# def c_side_selection():
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|***********PLEASE CHOOSE A SIDE***********|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|             A. NOUGHTS [ O ]             |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|             B. CROSSES [ X ]             |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|             [PLEASE SELECT]              |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A or B: ")
#     if setup.upper() == "A":
#         clear()
#         side_selected_A()    
#     elif setup.upper() == "B":            
#         clear()        
#         side_selected_B()
#     else:
#         print("Please make a valid choice")

# def side_selected_A():
#     global team_selection 
#     team_selection = "NOUGHTS"
#     print("                                      ")
#     print("--------------------------------------------")
#     print("        You have chosen Team Noughts        ")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|          TEAM NOUGHTS SELECTED           |")
#     print("|                                          |")
#     print("|                  [ O ]                   |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
    
#     setup_screen()

# def side_selected_B():
#     global team_selection 
#     team_selection = "CROSSES"
#     print("                                      ")
#     print("--------------------------------------------")
#     print("        You have chosen Team Crosses        ")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|          TEAM CROSSES SELECTED           |")
#     print("|                                          |")
#     print("|                  [ X ]                   |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def select_board_normal():
#     global board_size 
#     board_size = "DEFAULT"
#     print("                                      ")
#     print("--------------------------------------------")
#     print("You have chosen Board Size: Standard (8 x 8)")
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|           A  B  C  D  E  F  G  H         |")
#     print("|                                          |")
#     print("|      0    O  -  &  -  O  -  0  -         |")
#     print("|      1    -  O  -  O  -  @  -  O         |")
#     print("|      2    O  -  O  -  O  -  O  -         |")
#     print("|      3    -  -  -  -  -  -  -  -         |")
#     print("|      4    -  -  -  -  -  -  -  -         |")
#     print("|      5    X  -  X  -  X  -  X  -         |")
#     print("|      6    -  X  -  X  -  X  -  X         |")
#     print("|      7    #  -  X  -  X  -  X  -         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def select_board_large():
#     global board_size 
#     board_size = " LARGE "
#     print("                                      ")
#     print("-------------------------------------------")
#     print("You have chosen Board Size: Large (9 x 9)  ")
#     print("-------------------------------------------")
#     print("|                                          |")
#     print("|           A  B  C  D  E  F  G  H  I      |")
#     print("|                                          |")
#     print("|      0    O  -  O  -  O  -  O  -  O      |")
#     print("|      1    -  O  -  O  -  O  -  O  -      |")
#     print("|      2    O  -  O  -  O  -  O  -  O      |")
#     print("|      3    -  -  -  -  -  -  -  -  -      |")
#     print("|      4    -  -  -  -  -  -  -  -  -      |")
#     print("|      5    -  -  -  -  -  -  -  -  -      |")
#     print("|      6    -  X  -  X  -  X  -  X  -      |")
#     print("|      7    X  -  X  -  X  -  X  -  X      |")
#     print("|      8    -  X  -  X  -  X  -  X  -      |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|__________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def select_board_extralarge():
#     global board_size 
#     board_size = "X-LARGE"
#     print("                                         ")
#     print("-------------------------------------------------")
#     print("You have chosen Board Size: Extra-Large (10 x 10)")
#     print("-------------------------------------------------")
#     print("|                                               |")
#     print("|                                               |")
#     print("|           A  B  C  D  E  F  G  H  I  J        |")
#     print("|                                               |")
#     print("|      0    O  -  O  -  O  -  O  -  O  -        |")
#     print("|      1    -  O  -  O  -  O  -  O  -  O        |")
#     print("|      2    O  -  O  -  O  -  O  -  O  -        |")
#     print("|      3    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      4    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      5    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      6    -  -  -  -  -  -  -  -  -  -        |")
#     print("|      7    X  -  X  -  X  -  X  -  X  -        |")
#     print("|      8    -  X  -  X  -  X  -  X  -  X        |")
#     print("|      9    X  -  X  -  X  -  X  -  X  -        |")
#     print("|                                               |")
#     print("|                                               |")
#     print("|        [PRESS ENTER TO CONTINUE]              |")
#     print("|_______________________________________________|")
#     input("")
#     clear()
#     setup_screen()

# def b_select_board_size():

#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT BOARD SIZE*************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|    A. STANDARD                           |")
#     print("|                                          |")
#     print("|    B. LARGE                              |")
#     print("|                                          |")
#     print("|    C. EXTRA-LARGE                        |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|            [PLEASE SELECT]               |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A, B or C: ")
#     if setup.upper() == "A":
#         clear()
#         select_board_normal()
#     elif setup.upper() == "B":            
#         clear()        
#         select_board_large()
#     elif setup.upper() == "C":            
#         clear()        
#         select_board_extralarge()        
#     else:
#         print("Please make a valid choice")

# def a_select_game_mode():

#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT GAME MODE**************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|    A. Player1    vs.    Computer         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|    B. Player1    vs.    Player2          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|            [PLEASE SELECT]               |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A or B: ")
#     if setup.upper() == "A":
#         clear()
#         game_mode_A()    
#     elif setup.upper() == "B":            
#         clear()        
#         game_mode_B()
#     else:
#         print("Please make a valid choice")

# def game_mode_A():
#     global game_mode_status 
#     game_mode_status = "P vs. C"
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT GAME MODE**************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|      YOU HAVE SELECTED GAME MODE: A      |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        PLAYER1    vs.   COMPUTER         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     input("")
#     clear()
#     setup_screen()

# def game_mode_B():
#     global game_mode_status 
#     game_mode_status = "P vs. P"
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************SELECT GAME MODE**************|")
#     print("|                                          |")
#     print("|                                          |")
#     print("|      YOU HAVE SELECTED GAME MODE: B      |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        PLAYER1    vs.   PLAYER2          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|        [PRESS ENTER TO CONTINUE]         |")
#     print("|                                          |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     input("")
#     clear()
#     setup_screen()

# def welcome_screen():
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|    W  E  L  C  O  M  E                   |")
#     print("|                                          |")
#     print("|       T O                                |")
#     print("|                                          |")
#     print("|          P  Y  T  H  O  N                |")
#     print("|                                          |")
#     print("|              C  H  E  C  K  E  R  S !    |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|                                          |")
#     print("|         [PRESS ENTER TO BEGIN]           |")
#     print("|                                          |")
#     print("|                                          |")
#     print("--------------------------------------------")    

# welcome_screen()
# input("")
# clear()

# def setup_screen():
#     global play_status
#     global game_mode_status 
#     global board_size 
#     global team_selection 
#     if game_mode_status and board_size and team_selection != "PENDING":
#         play_status = "READY!"
#     else: 
#         play_status = "LOCKED"
#     print("--------------------------------------------")
#     print("|                                          |")
#     print("|************GAME SETUP MENU:**************|")
#     print("|                                          |")
#     print(f"|    A. GAME MODE            [{game_mode_status}]     |")
#     print("|                                          |")
#     print(f"|    B. BOARD SIZE           [{board_size}]     |")
#     print("|                                          |")
#     print(f"|    C. SIDE SELECTION       [{team_selection}]     |")
#     print("|                                          |")
#     print("|    D. VIEW RULES           [OPTIONAL]    |")
#     print("|                                          |")
#     print(f"|    E. PLAY CHECKERS!       [{play_status}]      |")
#     print("|                                          |")
#     print("|         [PLEASE COMPLETE SETUP]          |")
#     print("|                                          |")
#     print("--------------------------------------------")
#     setup = input("Select option A to E: ")

#     if setup.upper() == "A":
#         clear()
#         a_select_game_mode()
#     elif setup.upper() == "B":
#         clear()
#         b_select_board_size()
#     elif setup.upper() == "C":
#         clear()
#         c_side_selection()
#     elif setup.upper() == "D":
#         clear()
#         d_view_rules()
#     elif setup.upper() == "E":
#         clear()
#         e_start_game()
#     else:
#         print("Please make a valid choice")

# setup_screen()

# This Section workings for setting up game
# print("                                      \n--------------------------------------------")
# print("You have chosen Board Size: Standard (8 x 8)")
# print("--------------------------------------------")
# print("|                                          |")
# print("|           A  B  C  D  E  F  G  H         |")
# print("|                                          |")
# print("|      0    O  -  &  -  O  -  0  -         |")
# print("|      1    -  O  -  O  -  @  -  O         |")
# print("|      2    O  -  O  -  O  -  O  -         |")
# print("|      3    -  -  -  -  -  -  -  -         |")
# print("|      4    -  -  -  -  -  -  -  -         |")
# print("|      5    X  -  X  -  X  -  X  -         |")
# print("|      6    -  X  -  X  -  X  -  X         |")
# print("|      7    #  -  X  -  X  -  X  -         |")
# print("|                                          |")
# print("|                                          |")
# print("|        [PRESS ENTER TO CONTINUE]         |")
# print("|__________________________________________|")
# input("")

# coordinates = []
# for x in range(10):
#     coordinates.append(x)
# print(f"coordinates={coordinates}")

# numbers=[]
# numbers = [x for x in range(10)]
# print(f"numbers={numbers}")

# board = []

# def make_row_1(display_lines):
#     row = ["|"]
#     row.extend([" "] * 4)
#     row.extend(["_"] * 8)
#     row.extend([" "] * 6)
#     row.extend(["|"])
#     display_lines.append(row)
#     return display_lines

# def create_board(display_lines):
#     make_row_1(display_lines)
#     return display_lines

# create_board(board)

# def print_board(display_lines):
#     print(display_lines)
#     for row in display_lines:
#         print("".join(row))

# print_board(board)

