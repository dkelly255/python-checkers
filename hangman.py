from os import system, name
from random import choice


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


def clear():
        """
        Clears the terminal for formatting purposes
        """
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


welcome_screen()

# Initialise key variables
# Word variables
word_list = ["try", "to", "setup", "hangman", "game", "using", "python"]
answer_unhidden = choice(word_list)
answer_hidden = ["Guess The Word: "]
answer_hidden.extend(["_ "] * len(answer_unhidden))
# Guess variables
guesses_remaining = 8
guesses_used = 0
incorrect_guesses = 0
previous_guesses = ["Previous Guesses: "]

print(word_list)
print(answer_unhidden)
print(answer_hidden)



# Display main game screen
# clear()
# draw_gallows(incorrect_guesses)
print("".join(answer_hidden))
print(f"Guesses Used So Far: {guesses_used}")
print(f"Guesses Remaining: {guesses_remaining}")