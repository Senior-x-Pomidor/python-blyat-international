last_update = "27.06.2025"

import random
import urllib.request
from games_and_tools import vigenere
from games_and_tools import googol

hangman_pictures =['''
          
          
          
          
          
          
          
          
          
          ''','''
     ┌      
     │      
     │      
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \ ''','''
     ┌─────┐
     │      
     │      
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \ ''','''
     ┌─────┐
     │     │
     │      
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │     |
     │     |
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|
     │     |
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|\\
     │     |
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|\\
     │     |
     │    / 
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (O
     │    /|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \ ''','''
     ┌─────┐
     │     │
     │    (O)
     │    /|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (O)
     │   _/|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (O)
     │   _/|\_
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (x)
     │   _/|\_
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (x)
     │   _/|\_
     │     |
     │    / \\
     │   GAME
     │   OVER
  ───┴───   
 /       \  ''']

words_offline = [
    "Haus", "Baum", "Auto", "Straße", "Fahrrad",
    "Wasser", "Feuer", "Luft", "Erde", "Himmel",
    "Hund", "Katze", "Vogel", "Fisch", "Pferd",
    "laufen", "springen", "schlafen", "denken", "sehen",
    "reden", "schreiben", "lesen", "lernen", "spielen",
    "schön", "groß", "klein", "schnell", "langsam",
    "hell", "dunkel", "kalt", "warm", "freundlich",
    "rot", "blau", "grün", "gelb", "weiß",
    "Buch", "Tisch", "Stuhl", "Fenster", "Tür",
    "Liebe", "Angst", "Freude", "Hoffnung", "Mut","Zwetschge", "Schmetterling", "Dachgeschoss", "Schnürsenkel", "Wortspiel",
    "Unabhängigkeit", "Zustand", "Verständnis", "Rücksicht", "Einverständnis",
    "Schattenseite", "Widerspruch", "Geistesblitz", "Zweifel", "Geduld",
    "Entscheidung", "Achtsamkeit", "Gleichgewicht", "Zuneigung", "Verzweiflung",
    "Lichtblick", "Vergangenheit", "Zukunft", "Gegenwart", "Verhalten",
    "Verpflichtung", "Selbstvertrauen", "Mitgefühl", "Sicherheit", "Bedeutung",
    "Erinnerung", "Vorstellung", "Einstellung", "Beziehung", "Verbindung",
    "Lebensfreude", "Traurigkeit", "Einsamkeit", "Gemeinschaft", "Geborgenheit",
    "Möglichkeit", "Herausforderung", "Verantwortung", "Begeisterung", "Zufriedenheit",
    "Bescheidenheit", "Toleranz", "Neugier", "Ordnung", "Kreativität",
    "Veränderung", "Entwicklung", "Sprachgefühl", "Fremdwort", "Unwort",
    "Missverständnis", "Widerspiegelung", "Gedankenwelt", "Gedankenreise", "Wortschatz",
    "Abenteuerlust", "Spiegelbild", "Feinfühligkeit", "Zielsicherheit", "Wertschätzung",
    "Weisheit", "Sehnsucht", "Fernweh", "Heimweh", "Dankbarkeit",
    "Vertrauen", "Verlust", "Versuchänglichkeit", "Komplexität", "Differenzierung",
    "Doppeldeutigkeit", "Ehrlichkeit", "Offenheit", "Wahrnehmung", "Beobachtung",
    "Vernunft", "Instinkt", "Tageslicht", "Mondschein", "Sternenhimmel",
    "Nebelschleier", "Regenschauer", "Gewitter", "Schneeflocke", "Frost",
    "Tauwetter", "Glätte", "Eisregen", "Blitzschlag", "Donner",
    "Flutwelle", "Erdrutsch", "Vulkanausbruch", "Hitzewelle", "Dürre",
    "Hungersnot", "Lawine", "Sturmflut", "Orkan", "Tornado",
    "Wirbelsturm", "Säugling", "Jugendlicher", "Erwachsener", "Rentner",
    "Wissenschaftler", "Philosoph", "Dichter", "Denker", "Künstler",
    "Schriftsteller", "Komponist", "Dirigent", "Erfinder", "Techniker",
    "Mechaniker", "Bergarbeiter", "Bauer", "Zimmermann", "Maurer",
    "Handwerker", "Gärtner", "Koch", "Bäcker", "Fleischer", "Zwischenzeit", "Zeitumstellung", "Rückenlehne", "Sicherheitsabstand", "Geschwindigkeitsbegrenzung",
    "Wortneuschöpfung", "Rechtschreibfehler", "Leitplanke", "Autobahnausfahrt", "Kreuzung",
    "Abzweigung", "Gegenverkehr", "Rücksichtslosigkeit", "Sprachverwirrung", "Rollenverteilung",
    "Sinneswandel", "Buchstabensalat", "Großschreibung", "Kleinigkeit", "Alltäglichkeit",
    "Zufallstreffer", "Verschwörung", "Märchenhaftigkeit", "Geräuschkulisse", "Denkfehler",
    "Abstellgleis", "Entscheidungsfreiheit", "Fingerspitzengefühl", "Konzentrationsschwäche", "Überforderung",
    "Lichtgeschwindigkeit", "Antriebslosigkeit", "Gleichgültigkeit", "Bequemlichkeit", "Verletzlichkeit",
    "Kunstverständnis", "Technologie", "Gedankengang", "Kraftaufwand", "Buchhaltung",
    "Rechtsprechung", "Anerkennung", "Unterbewusstsein", "Entschlossenheit", "Zielstrebigkeit",
    "Sinnfrage", "Fremdscham", "Selbstbewusstsein", "Bewusstseinszustand", "Zwangsvorstellung"
]

words_offline_halfmeier = ["Qualitätsmanagement", "Qualitätssicherung", "Qualitätsplanung", "Qualitätslenkung", "Qualitätsverbesserung", "Prozessqualität", "Produktqualität", "Kundenanforderungen", "Kundenzufriedenheit", "Qualitätsaudit", "Fehlermanagement", "Reklamationsmanagement", "Beschwerdemanagement", "KVP", "Kontinuierlicher Verbesserungsprozess", "Six Sigma", "Lean Management", "TQM", "Total Quality Management", "ISO 9001", "DIN EN ISO", "Zertifizierung", "Auditor", "Auditbericht", "Auditplan", "Auditfeststellung", "Normen", "Richtlinien", "Risikomanagement", "FMEA", "Fehlermöglichkeits- und Einflussanalyse", "Ishikawa-Diagramm", "Pareto-Analyse", "PDCA-Zyklus", "Plan-Do-Check-Act", "Qualitätsregelkarte", "Statistische Prozesskontrolle", "SPC", "Qualitätskennzahlen", "Kennzahlensystem", "Prozessanalyse", "Prozessoptimierung", "Messmittelmanagement", "Messsystemanalyse", "Kalibrierung", "Validierung", "Verifizierung", "Lieferantenbewertung", "Lieferantenmanagement", "Wareneingangsprüfung", "Stichprobenprüfung", "Qualitätskosten", "Fehlerkosten", "Präventionskosten", "Internes Audit", "Externes Audit", "Managementbewertung", "Dokumentation", "Verfahrensanweisung", "Arbeitsanweisung", "Prozessbeschreibung", "Handbuch", "QM-Handbuch", "Abweichungsmanagement", "Change Management", "Lessons Learned", "CAPA", "Corrective and Preventive Action", "Root Cause Analysis", "Ursachenanalyse", "Benchmarking", "Null-Fehler-Strategie"
    
]

letter_ls =[]
wrong_letters_ls = [] 

def clear_terminal():

    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def big_text(text):

    x = -5

    if text == "hangman":
        print("\033[1;31m    __  __                                            \033[0m"+" "*(10-x) + "\033[1;37m      ,%%%%%%%%,\033[0m")
        print("\033[1;31m   / / / /____ _ ____   ____ _ ____ ___   ____ _ ____ \033[0m"+" "*(10-x) + "\033[1;37m     %%o%%/%%%%%%\033[0m")
        print("\033[1;33m  / /_/ // __ `// __ \\ / __ `// __ `__ \\ / __ `// __ \\""\033[0m"+" "*(10-x) + "\033[1;37m    %%%%\\%%%<%%%%%\033[0m")
        print("\033[1;32m / __  // /_/ // / / // /_/ // / / / / // /_/ // / / /\033[0m"+" "*(10-x) + "\033[1;37m    %%>%%%/%%%%o%%\033[0m")
        print("\033[1;34m/_/ /_/ \\__,_//_/ /_/ \\__, //_/ /_/ /_/ \\__,_//_/ /_/ \033[0m"+" "*(10-x) + "\033[1;37m    %%%%%o%%\\%%//%\033[0m")
        print("\033[1;34m                     /____/                           \033[0m"+" "*(10-x) + "\033[1;37m    %\\o%\\%%/%o/%%'\033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update+" "*(26-x) + "\033[1;37m      '%%\ `%/%%%'\033[0m")
        print(" "*(63-x)+"\033[1;37m        '%| |%|%'\033[0m")
        print(" "*(63-x)+"\033[1;37m          | | (O\033[0m")
        print(" "*(63-x)+"\033[1;37m          | | |\\\033[0m")
        print(" "*(63-x)+"\033[1;37m          | | >>\033[0m")
        print(" "*(63-x)+"\033[1;37m          | |\033[0m")
        print(" "*(63-x)+"\033[1;37m         /   \\""\033[0m")
        print("^"*(63-x)+"\033[1;37m^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")

def difficulty():



    print("Choose difficulty:")
    print("- This affects the number of available attempts:\n ")

    print(farbig("1. Easy   ", 32) + "15 attempts\n")
    print(farbig("2. Medium ", 32) + "10 attempts\n")
    print(farbig("3. Hard   ", 32) + " 5 attempts\n")
    print(farbig("4. Exit   ", 31) + "Return to the menu\n")

    difficulty = 0

    while difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4:

        try:
            difficulty = int(input("Enter a number (1-4):\n"))
        except:
            difficulty = 0
        
        if difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4:

            print("Invalid input!")
            
    if difficulty in (1, 2, 3):
        clear_terminal()
        big_text("hangman")
        print("Difficulty", difficulty, "has been selected!\n")
        input("Press Enter to continue:\n")
        return difficulty
    
    if difficulty == 4:
        clear_terminal()
        game_pick_mode_hangman()

def word_input():

    clear_terminal()

    big_text("hangman")

    print("Now enter the secret word:\n")
    word = str(input())

    if len(word)>0 and word[0] == "#":

        word = vigenere.decrypt(word)

    global letter_ls
    letter_ls = [] 

    for letter in word:
        letter_ls.append(letter)

def guess_word():
    global letter_ls
    global wrong_letters_ls
    answer = False  # Fix: Initialize answer to avoid UnboundLocalError

    diffi = difficulty()
    word_input()
    show = ["_" for _ in letter_ls]

    # Setze die erlaubte Anzahl an Fehlversuchen je nach Schwierigkeitsgrad
    if diffi == 1:
        max_turns = 15
    elif diffi == 2:
        max_turns = 10
    else:
        max_turns = 5

    misses = 0
    turn = 1
    wrong_letters_ls = []

    while misses < max_turns and "_" in show:
        turn = turn+1
        clear_terminal()
        big_text("hangman")
        print(f"Errors: {misses} of {max_turns}" + " "*17 + f"Turn No. {turn-1}")

        # Bild proportional zur Fehleranzahl anzeigen
        pic_index = min(int(misses * (len(hangman_pictures) - 1) / max_turns), len(hangman_pictures)-1)
        print(hangman_pictures[pic_index] + "\n")

        print("Wort: " + " ".join(show))
        print("Wrong letters or words: " + ", ".join(wrong_letters_ls))
        print("Enter a letter or guess the whole word:\n")
        guess = input().lower()

        if guess.lower() == "".join(letter.lower() for letter in letter_ls):
            answer = True
            break
        
        if guess.lower() == "":

            print("No input!")
            input("Press Enter...")

            continue


        if guess.upper() in wrong_letters_ls or guess in [l.lower() for l in show]:
            print("Letter has already been guessed!")
            input("Press Enter...")
            continue

        found = False
        for index, letter in enumerate(letter_ls):
            if letter.lower() == guess:
                show[index] = letter
                found = True

        if found:
            print("Hit!\n")
        else:
            print("Nope!")
            wrong_letters_ls.append(guess.upper())
            misses += 1

        input("Press Enter for the next attempt...")

    clear_terminal()
    big_text("hangman")
    print(f"Errors: {misses} of {max_turns}" + " "*17 + f"Turn No. {turn-1}")
    # Nach Spielende das finale Bild anzeigen
    pic_index = min(int(misses * (len(hangman_pictures) - 1) / max_turns), len(hangman_pictures) - 1)
    print(hangman_pictures[pic_index]+"\n")
    if "_" not in show:
        print("Congratulations! The word was:", "".join(letter_ls))
    elif answer == True:
        print("Congratulations! The word was:", "".join(letter_ls))
    else:
        print("Unfortunately, you lost! The word was:", "".join(letter_ls))

    letter_ls = []
    wrong_letters_ls = []
    input("Press Enter to continue:\n")

def computer_hangman():
    clear_terminal()
    big_text("hangman")
    print("Please choose a game mode:\n ")
    print(farbig("1. Computer (Offline)", 32) + " Random selection from stored words (german)\n")
    print(farbig("2. Computer (Online) ", 32) + " Random selection of words from the internet (50k words, connection required)(german-default)\n")
    print(farbig("3. Exit              ", 31) + " \n---Back\n")

    mode = 0
    while mode not in (1, 2, 3, 666):
        try:
            mode = int(input("Enter a number (1-3):"))
        except:
            mode = 0
        if mode not in (1, 2, 3, 666):
            print("Invalid input!")
    clear_terminal()
    return mode

def game_pick_mode_hangman():

    clear_terminal()

    big_text("hangman")

    print("Please choose a game mode:\n ")
    print(farbig("1. 1 vs many  ", 32) + " min. 2 players\n---One player enters a word, the others guess! (or enter an encrypted word)\n")
    print(farbig("2. Computer   ", 32) + " min. 1 player\n---Play against the computer\n")
    print(farbig("3. Vigenère   ", 32) + "                \n---Create a Vigenère cipher\n")
    print(farbig("4. Exit       ", 31) + " \n---Close game\n")

    mode = 0

    while mode != 1 and mode != 2 and mode != 3 and mode != 4:

        try:
            mode = int(input("Zahl eingeben (1-4):"))
        except:
            mode = 0
        
        if mode != 1 and mode != 2 and mode != 3 and mode != 4:

            print("Invalid input!")
            
    if mode == 1:
        clear_terminal()
        game_hangman_1_v_many()

    if mode == 2:
        clear_terminal()
        game_hanman_computer_offline_online()
    
    if mode == 3:
        clear_terminal()
        vigenere.create_chiffre_hangman()
        
    if mode == 4:
        clear_terminal()
        return
    
def game_hangman_1_v_many():


    clear_terminal()
    big_text("hangman")
    guess_word()
    game_pick_mode_hangman()
        
def pick_random_word():

    if zz == 666:

        random_word = random.choice(words_offline_halfmeier)
    else:

        random_word = random.choice(words_offline)

    global letter_ls
    letter_ls = [] 

    for letter in random_word:
        letter_ls.append(letter)

    if zz == 666:
        print("Das geheime Maschinenbau-Wort wurde vom Computer bestimmt!")
        input("Enter drücken...")

    else:
        print("The secret word was chosen by the computer!")
        input("Press Enter...")

def pick_random_word_online():

    url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/de/de_50k.txt"
    #url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/en/en_50k.txt"
    #url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/fr/fr_50k.txt"
    
    global letter_ls
    letter_ls = [] 

    try:
        # Datei öffnen und Zeilen direkt durchiterieren
        with urllib.request.urlopen(url) as resp:
            # Jede Zeile decodieren und nur das erste Token (das Wort) nehmen
            word = [line.decode('utf-8').split()[0] 
                for line in resp 
                    if line.strip()]
        random_word = random.choice(word)
        for letter in random_word:
            letter_ls.append(letter)
        print("The secret word was chosen by the computer from the depths of the Internet!")
        input("Press Enter...")
    except Exception as e:
        # Fallback message for network errors
        return f"Error while retrieving: {e}"

def game_hanman_computer_offline_online():

    global letter_ls
    global wrong_letters_ls
    global zz
    answer = False  # Fix: Initialize answer to avoid UnboundLocalError

    zz = computer_hangman()

    big_text("hangman")
    diffi = difficulty()

    if zz == 666:

        pick_random_word()

    if zz == 1:

        pick_random_word()
    
    elif zz == 2:

        pick_random_word_online()


    show = ["_" for _ in letter_ls]

    # Setze die erlaubte Anzahl an Fehlversuchen je nach Schwierigkeitsgrad
    if diffi == 1:
        max_turns = 15
    elif diffi == 2:
        max_turns = 10
    else:
        max_turns = 5

    misses = 0
    turn = 1
    wrong_letters_ls = []

    while misses < max_turns and "_" in show:
        turn = turn+1
        clear_terminal()
        big_text("hangman")
        print(f"Errors: {misses} of {max_turns}" + " "*17 + f"Turn No. {turn-1}")

        # Bild proportional zur Fehleranzahl anzeigen
        pic_index = min(int(misses * (len(hangman_pictures) - 1) / max_turns), len(hangman_pictures)-1)
        print(hangman_pictures[pic_index] + "\n")

        print("Word: " + " ".join(show))
        print("Wrong letters or words: " + ", ".join(wrong_letters_ls))
        print("Enter a letter or guess the whole word:\n")
        guess = input().lower()

        if guess.lower() == "".join(letter.lower() for letter in letter_ls):
            answer = True
            break

        if guess.lower() == "":

            print("No input!")
            input("Press Enter...")

            continue


        if guess.upper() in wrong_letters_ls or guess in [l.lower() for l in show]:
            print("Letter has already been guessed!")
            input("Press Enter...")
            continue

        found = False
        for index, letter in enumerate(letter_ls):
            if letter.lower() == guess:
                show[index] = letter
                found = True

        if found:
            print("Hit!\n")
        else:
            print("Nope!")
            wrong_letters_ls.append(guess.upper())
            misses += 1

        input("Press Enter for the next attempt...")

    clear_terminal()
    big_text("hangman")
    print(f"Errors: {misses} of {max_turns}" + " "*17 + f"Turn No. {turn-1}")
    # Nach Spielende das finale Bild anzeigen
    pic_index = min(int(misses * (len(hangman_pictures) - 1) / max_turns), len(hangman_pictures) - 1)
    print(hangman_pictures[pic_index])
    if "_" not in show:
        print("Congratulations! The word was:", "".join(letter_ls))
        googol.update_value_file("+", 100)
    elif answer == True:
        print("Congratulations! The word was:", "".join(letter_ls))
        googol.update_value_file("+", 100)
    else:
        print("Unfortunately, you lost! The word was:", "".join(letter_ls))

    letter_ls = []
    wrong_letters_ls = []
    input("Press Enter to continue:\n")
    game_pick_mode_hangman()


if __name__ == "__main__":
    game_pick_mode_hangman()
