from datetime import datetime

from games_and_tools import googol

last_update = "29.06.2025"

def big_text(text):



    if text == "sparkasse":
        print("\033[1;31m   _____                  __                      \033[0m")
        print("\033[1;31m  / ___/____  ____ ______/ /______ ______________ \033[0m")
        print("\033[1;31m  \__ \/ __ \/ __ `/ ___/ //_/ __ `/ ___/ ___/ _ \\""\033[0m")
        print("\033[1;31m ___/ / /_/ / /_/ / /  / ,< / /_/ (__  |__  )  __/\033[0m")
        print("\033[1;31m/____/ .___/\__,_/_/  /_/|_|\__,_/____/____/\___/ \033[0m")
        print("\033[1;31m    /_/                                           \033[0m")
        print("Bank statement from: "+str(datetime.today().replace(microsecond=0))+"\n")
        print("TD bank is currently under renovation; not all functions are available")
        print(" \n \n \n")
def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")
def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

##########################################################






##########################################################
def bank_main():

    big_text("sparkasse")
    print("\033[1;31m------------------------------------------------------------------------------\033[0m")
    print("Account balance "+googol.display_money_value()+"€")
    print("\033[1;31m------------------------------------------------------------------------------\033[0m")
    print("No money")
    print("ontact the Jobcenter or simply play a game. For each victory you receive:")
    print("\033[1;31m------------------------------------------------------------------------------\033[0m")
    print("- Hangman vs Computer (offline/online): 100€")
    print("")
    print("")
    input("Press Enter to leave the bank...")
    return


if __name__ == "__main__":
     bank_main()