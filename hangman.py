# Attempted rebuild from scratch
from os import system, name
from random import choice

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



def game_won():
    print("You have won")


def game_lost():
    print("You have won")


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


def display_correct_guess_notification():
    print("CORRECT GUESS NOTIFICATION PLACEHOLDER")


def display_incorrect_guess_notification():
    print("INCORRECT GUESS NOTIFICATION PLACEHOLDER")


welcome_screen()

# Initialise key variables
# Answer bank & Word variables
word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]
answer = choice(word_list)
answer_hidden = ["Guess The Word: "]
answer_hidden.extend(["_ "] * len(answer))
# Guess variables
guesses_remaining = 8
guesses_used = 0
incorrect_guesses = 0
previous_guesses = ["Previous Guesses: "]
print_previous_guesses = "".join(previous_guesses)
# Gallows variables
gallows_stage = 0

# for indice, letter in enumerate(answer, start=1):
#     print(indice, letter)

def initial_checks():
    if not ("_ " in answer_hidden):
        game_won()

    if not (guesses_remaining > 0):
        game_lost()

# Display main game screen
# clear()
# draw_gallows(incorrect_guesses)
def main_game_screen():
    print("*Main Game Screen*\n")
    print("".join(answer_hidden))
    print(f"Guesses Used So Far: {guesses_used}")
    print(f"Guesses Remaining: {guesses_remaining}")
    print("".join(previous_guesses))


def validate_guess():
    while True:
        user_guess = input("Please guess a letter: ").lower()    
        if len(user_guess) == 1:
            if user_guess.isalpha():
                if not (user_guess in previous_guesses):
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


def answer_check(user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden):
        
    previous_guesses.append(user_guess + ", ") 
    guesses_used += 1

    if user_guess in answer:
        display_correct_guess_notification()
        reveal_letter_in_answer(user_guess, answer, answer_hidden)
    else:
        display_incorrect_guess_notification()
        gallows_stage += 1
        incorrect_guesses += 1

    return user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden



while "_ " in answer_hidden:
    if gallows_stage == 8:
        break
    else:
        clear()
        main_game_screen()
        draw_gallows(gallows_stage)
        user_guess = validate_guess()
        user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden = answer_check(user_guess, previous_guesses, gallows_stage, incorrect_guesses, guesses_used, answer, answer_hidden)
        clear()
    main_game_screen()
    draw_gallows(gallows_stage)
    
    if gallows_stage == 8:
        print(f"Sorry You Lost - the answer was {answer}")
    else:
        print(f"Congratulations You Won - the answer was {answer}")


