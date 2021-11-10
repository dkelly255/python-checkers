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
