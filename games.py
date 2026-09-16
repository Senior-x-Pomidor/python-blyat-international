last_update = "29.06.2025"

from games_and_tools import battleship
from games_and_tools import tic_tac_toe
from games_and_tools import hangman
from games_and_tools import animation_why
from games_and_tools import game2048
from games_and_tools import blackjack
from games_and_tools import googol
from games_and_tools import bank

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def big_text(text):


    if text == "games":

        print("\033[1;31m   ______                             \033[0m")
        print("\033[1;31m  / ____/____ _ ____ ___   ___   _____\033[0m")
        print("\033[1;33m / / __ / __ `// __ `__ \\ / _ \\ / ___/\033[0m")
        print("\033[1;32m/ /_/ // /_/ // / / / / //  __/(__  ) \033[0m")
        print("\033[1;34m\\____/ \\__,_//_/ /_/ /_/ \\___//____/  \033[0m")
        print("\033[1;34m                                      \033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update)
        print("contributed by: boris (BorisG0)")
        print("  \n \n \n \n")

def games_start():

    clear_terminal()

    big_text("games")
    

    print("Welcome to a fine selection of classics!\n\n" \
    "- All games run without installing additional libraries.\n" \
    "- For the best display, maximize the terminal window.\n" \
    "- To terminate the program, Ctrl+C can be pressed at any time.\n" \
    '- Please do not enter exactly "!@#*()_+{ }|$%^&: <> ? [ ] \\;\', ./".\n\n')

    print(farbig("- 0.    ", 32) + "German TD Bank\n")
    
    print("Currently available games:\n\n")
    print(farbig("- 1.    ", 32) + "Battleship\n")
    print(farbig("- 2.    ", 32) + "Hangman\n")
    print(farbig("- 3.    ", 32) + "Tic-Tac-Toe\n")
    print(farbig("- 4.    ", 32) + "Blackjack\n")
    print(farbig("- 2048. ", 32) + "2048\n")
    print()
    print("Enter the game number (number from" + farbig(" 1-2048", 32) + ") or type" + farbig(" Exit ", 31) + "to quit:")

    game = -1

    while game != 0 and game != 1 and game != 2 and game != 3 and game != 4 and game != 2048 and game != "Exit" :

        game = input("Input:")

        secret = r"""!@#*()_+{ }|$%^&: <> ? [ ] \;', ./"""

        if game == secret:
            animation_why.anim_1()
            clear_terminal()
            games_start()

        try:
            game = int(game)
        except:
            game = game
        
        if game != 0 and game != 1 and game != 2 and game != 3 and game != 4 and game != 2048 and game != "Exit":

            print("Invalid input!")


    if game == 0:
        clear_terminal()
        bank.bank_main()
            
    if game == 1:
        clear_terminal()
        battleship.game_pick_mode_battleship()

    if game ==2:
        clear_terminal()
        hangman.game_pick_mode_hangman()
    
    if game == 3:
        clear_terminal()
        tic_tac_toe.game_pick_mode_tic_tac_toe()

    if game == 4:
        clear_terminal()
        blackjack.blackjack_loop()

    if game == 2048:
        print('starting')
        game2048.start()

    if game == "Exit":
        clear_terminal()
        print(farbig("\n" +"Exit", 31) + "\n")
        return "Exit"
    

#Game start:

g = "notExit"

while g != "Exit":

    g = games_start()






