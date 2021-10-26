# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to e-pect a terminal of 80 characters wide and O4 rows high

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
    print("|         [PRESS ANY KEY TO BEGIN]         |")
    print("|                                          |")
    print("|                                          |")
    print("--------------------------------------------")


welcome_screen()


def setup_screen():
    print("--------------------------------------------")
    print("|                                          |")
    print("|************GAME SETUP MENU:**************|")
    print("|                                          |")
    print("|    A. GAME MODE            [NOT DONE]    |")
    print("|                                          |")
    print("|    B. BOARD SIZE           [NOT DONE]    |")
    print("|                                          |")
    print("|    C. SIDE SELECTION       [NOT DONE]    |")
    print("|                                          |")
    print("|    D. VIEW RULES           [OPTIONAL]    |")
    print("|                                          |")
    print("|                                          |")
    print("|         [PLEASE COMPLETE SETUP]          |")
    print("|                                          |")
    print("--------------------------------------------")


setup_screen()


def create_board_normal():

    print("                                      ")
    print("--------------------------------------------")
    print("You have chosen Board Size: Standard (8 x 8)")
    print("--------------------------------------------")
    print("                                      ")
    print("                                      ")
    print("           A  B  C  D  E  F  G  H")
    print("                                 ")
    print("      0    O  -  &  -  O  -  0  -")
    print("      1    -  O  -  O  -  @  -  O")
    print("      2    O  -  O  -  O  -  O  -")
    print("      3    -  -  -  -  -  -  -  -")
    print("      4    -  -  -  -  -  -  -  -")
    print("      5    X  -  X  -  X  -  X  -")
    print("      6    -  X  -  X  -  X  -  X")
    print("      7    #  -  X  -  X  -  X  -")
    print("                                      ")


create_board_normal()


def create_board_large():

    print("                                      ")
    print("-----------------------------------------")
    print("You have chosen Board Size: Large (9 x 9)")
    print("-----------------------------------------")
    print("                                      ")
    print("                                      ")
    print("           A  B  C  D  E  F  G  H  I")
    print("                            ")
    print("      0    O  -  O  -  O  -  O  -  O")
    print("      1    -  O  -  O  -  O  -  O  -")
    print("      2    O  -  O  -  O  -  O  -  O")
    print("      3    -  -  -  -  -  -  -  -  -")
    print("      4    -  -  -  -  -  -  -  -  -")
    print("      5    -  -  -  -  -  -  -  -  -")
    print("      6    -  X  -  X  -  X  -  X  -")
    print("      7    X  -  X  -  X  -  X  -  X")
    print("      8    -  X  -  X  -  X  -  X  -")
    print("                                      ")


create_board_large()


def create_board_extra_large():

    print("                                         ")
    print("-------------------------------------------------")
    print("You have chosen Board Size: Extra-Large (10 x 10)")
    print("-------------------------------------------------")
    print("                                         ")
    print("                                      ")
    print("           A  B  C  D  E  F  G  H  I  J")
    print("                                 ")
    print("      0    O  -  O  -  O  -  O  -  O  -")
    print("      1    -  O  -  O  -  O  -  O  -  O")
    print("      2    O  -  O  -  O  -  O  -  O  -")
    print("      3    -  -  -  -  -  -  -  -  -  -")
    print("      4    -  -  -  -  -  -  -  -  -  -")
    print("      5    -  -  -  -  -  -  -  -  -  -")
    print("      6    -  -  -  -  -  -  -  -  -  -")
    print("      7    X  -  X  -  X  -  X  -  X  -")
    print("      8    -  X  -  X  -  X  -  X  -  X")
    print("      9    X  -  X  -  X  -  X  -  X  -")
    print("                                      ")


create_board_extra_large()