# Initial import statements to enable use of
# external library functionality within game
from os import system, name
from random import choice


def main():
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


    # Credits: As per readme credits section - this clear terminal function
    # is taken from the methods used by geeksforgeeks.org - see full details
    # and links in credits section of readme
    def clear():
        """
        Clears the terminal for formatting purposes
        """
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    welcome_screen()


    def draw_gallows(incorrect_guesses):
        """
        Build up the hangman "gallows" element by
        element based on number of incorrect guesses
        """
        if incorrect_guesses == 0:
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
        elif incorrect_guesses == 1:
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
        elif incorrect_guesses == 2:
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
        elif incorrect_guesses == 3:
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
        elif incorrect_guesses == 4:
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
        elif incorrect_guesses == 5:
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
        elif incorrect_guesses == 6:
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
        elif incorrect_guesses == 7:
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
        elif incorrect_guesses == 8:
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


    def reset_variables(word_list, answer, guesses_used, guesses_remaining, incorrect_guesses, previous_guesses, attempt):
        """
        Resets all game variables to original/default
        values - used in end_game function as part of
        final game exit/play menu loop
        """        
        word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]

        answer = choice(word_list)
        guesses_used = 0
        guesses_remaining = 8
        incorrect_guesses = 0
        previous_guesses = ["Previous Guesses: "]
        attempt = ["Guess The Word: "]
        attempt.extend(["_ "] * len(answer))

        clear()
        draw_gallows(incorrect_guesses)
        print("".join(attempt))
        print(f"Guesses Used So Far: {guesses_used}")
        print(f"Guesses Remaining: {guesses_remaining}")


    # Provisional rev of "word-list" - the bank of words
    # from which the "answer" will be randomly chosen to
    # enable playing the game

    # Credits: As per readme credits section - this approach of having
    # the bank of wrods in a list was taken from the "Terminal Hangman
    # in Python" repository and overview - the links and detail can
    # be viewed in the "credits" section of readme
    word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]
    # Select a word at random from the word list
    answer = choice(word_list)
    # Set initial numeric guess counting variables - Guesses
    # used, guesses remaining & incorrect guesses
    guesses_used = 0
    guesses_remaining = 8
    incorrect_guesses = 0
    # Setting initial string word display variables - Previous
    # guesses, current attempt, and a joined version of "attempt"
    # for display purposes
    previous_guesses = ["Previous Guesses: "]
    attempt = ["Guess The Word: "]
    attempt.extend(["_ "] * len(answer))

    # Initial paint of game board area - display the early-stage
    # gallows, along with the pre-guess attempt at the answer
    # accompanied by a count of the guesses used and remaining
    clear()
    draw_gallows(incorrect_guesses)
    print("".join(attempt))
    print(f"Guesses Used So Far: {guesses_used}")
    print(f"Guesses Remaining: {guesses_remaining}")


    def run_game(attempt, guesses_used, guesses_remaining, incorrect_guesses, previous_guesses):
        """
        Main game function - takes input from user,
        validates the input, and matches the input
        to the answer, incrementing guess variables
        as the game progresses. Culminates in either
        winning or losing the game.
        """

        while "_ " in attempt and guesses_remaining > 0:

            print("".join(previous_guesses))
            guessed_letter = input("\nPlease enter a letter:")
            guessed_letter = guessed_letter.lower()

            if not guessed_letter.isalpha() or len(guessed_letter) > 1:
                clear()
                draw_gallows(incorrect_guesses)
                print(
                    f"Error: {guessed_letter} is not a letter - please enter a letter\
                    \n")
                print("".join(attempt))
                print(f"Guesses Used So Far: {guesses_used}")
                print(f"Guesses Remaining: {guesses_remaining}")

            elif (guessed_letter + ", ") in previous_guesses:
                clear()
                draw_gallows(incorrect_guesses)
                print(
                    f"Error: '{guessed_letter}' already guessed, please try again\
                    \n")
                print("".join(attempt))
                print(f"Guesses Used So Far: {guesses_used}")
                print(f"Guesses Remaining: {guesses_remaining}")

            else:
                previous_guesses.append(guessed_letter + ", ")
                guesses_used += 1
                guesses_remaining -= 1

                if guessed_letter in answer:
                    index_list = []
                    for i in range(0, len(answer)):
                        if answer[i] == guessed_letter:
                            index_list.append(i)
                            print(f"CHECK HERE{index_list}")
                    for i in index_list:
                        j = i + 1
                        attempt[j] = guessed_letter + " "
                    clear()
                    draw_gallows(incorrect_guesses)
                    print(
                        f"Well done! The letter '{guessed_letter}' is in the answer\
                        \n")
                    print("".join(attempt))
                    print(f"Guesses Used So Far: {guesses_used}")
                    print(f"Guesses Remaining: {guesses_remaining}")

                else:
                    clear()
                    incorrect_guesses += 1
                    draw_gallows(incorrect_guesses)
                    print(
                        f"Sorry! The letter '{guessed_letter}' is not in the answer\
                        \n")
                    print("".join(attempt))
                    print(f"Guesses Used So Far: {guesses_used}")
                    print(f"Guesses Remaining: {guesses_remaining}")

                if not ("_ " in attempt):
                    clear()
                    draw_gallows(incorrect_guesses)
                    print("Congratulations, You have won!\n")
                    print(f"The Word was: '{answer}'")
                    print(f"Guesses Used: {guesses_used}")
                    print(f"Guesses Remaining: {guesses_remaining}")
                    break

                if guesses_remaining == 0:
                    clear()
                    draw_gallows(incorrect_guesses)
                    print("Sorry! You have Lost - No guesses remaining\n")
                    print("".join(attempt))
                    print(f"Guesses Used So Far: {guesses_used}")
                    print(f"Guesses Remaining: {guesses_remaining}")
                    print("\nGame Over! You Have Lost :{")
                    break


    run_game(attempt, guesses_used, guesses_remaining, incorrect_guesses, previous_guesses)


    def end_game():
        """
        Final/closing loop menu to allow the user to either
        exit the application, or play another game, by
        choosing an appropriate key-strike
        """
        loop = True
        while loop:
            decision = input(
                "\nPress 'E' to exit,\nOr...\nPress Any Key Followed \
            by 'Enter' to play again:")
            if decision.lower() == "e":
                print("Goodbye")
                loop = False
            else:
                word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]
                answer = choice(word_list)
                guesses_used = 0
                guesses_remaining = 8
                incorrect_guesses = 0
                previous_guesses = ["Previous Guesses: "]
                attempt = ["Guess The Word: "]
                attempt.extend(["_ "] * len(answer))
                clear()
                draw_gallows(incorrect_guesses)
                print("".join(attempt))
                print(f"Guesses Used So Far: {guesses_used}")
                print(f"Guesses Remaining: {guesses_remaining}")
                run_game(attempt, guesses_used, guesses_remaining, incorrect_guesses, previous_guesses)
    end_game()

main()


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



