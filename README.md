# python-blyat

*A delightful collection of handpicked terminal games made with Python.*

> **Finally, an English version of python-blyat is available!**
>
> The game collection and menus are now available in English. Hangman also supports multiple languages for its computer-generated words.

## 🎮 Game Collection

**python-blyat** is a curated selection of classic games, all connected through a simple, user-friendly terminal menu. The collection includes:

* 🚢 **Battleship** – A turn-based naval guessing game
* 🪢 **Hangman** – The classic word-guessing challenge
* 🎯 **Tic Tac Toe** – A strategic 2-player grid game
* 🃏 **Blackjack** – A fast-paced card showdown
* 🔢 **2048** – The popular number puzzle

## 💰 Easy Money Management System

**python-blyat** comes with a built-in, lightweight money management system to track your in-game currency and bets.

## 🚀 How to Start

Make sure you have **Python** installed. Then, launch the main menu from your terminal:

```bash
python3 games.py
```

## 🪢 Hangman – Language Selection

When playing **Hangman against the computer**, you can choose between **English, German, and French** word lists.

The language is selected in `hangman.py` by commenting/uncommenting the corresponding URL in `pick_random_word_online()`.

```python
def pick_random_word_online():

    url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/de/de_50k.txt"
    #url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/en/en_50k.txt"
    #url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/fr/fr_50k.txt"
```

### German

```python
url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/de/de_50k.txt"
```

### English

```python
url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/en/en_50k.txt"
```

### French

```python
url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/fr/fr_50k.txt"
```

**Only one URL should be active at a time.**

## ⚙️ Windows 10 Output Fix

By default, PowerShell and the legacy Windows Console may not interpret ANSI escape sequences (`\033[…m`) correctly.

If the color codes are displayed as raw text instead of colors, enable **Virtual Terminal processing** using one of the methods below.

### 1. Via the Registry

1. Press `Win + R`.
2. Type `regedit` and press **Enter**.
3. Confirm the UAC prompt.
4. Navigate to:

```text
HKEY_CURRENT_USER\Console
```

5. Create or modify the following DWORD value:

```text
VirtualTerminalLevel
```

6. Set its value to:

```text
1
```

ANSI escape sequences such as `\033[1;31m...\033[0m` should now be interpreted correctly.

### 2. Via PowerShell

Alternatively, run the following command in PowerShell:

```powershell
Set-ItemProperty
```
