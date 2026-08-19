# 🎯 Hangman Game

A simple command-line Hangman game built with Python.

The player tries to guess a randomly selected word one letter at a time. Every incorrect guess adds another part to the hangman drawing. Guess the word before the hangman is complete!

## 🎮 How to Play

1. The game randomly selects a secret word.
2. The word is displayed as underscores.
3. Enter one letter at a time.
4. Correct guesses reveal the letter in the word.
5. Incorrect guesses add a part to the hangman drawing.
6. You win if you reveal the entire word.
7. You lose if you reach the maximum number of incorrect guesses.

## ✨ Features

* 🎲 Random word selection
* 🔤 Letter-by-letter guessing
* 🎨 ASCII hangman drawings
* ❤️ Limited number of attempts
* 🚫 Prevents duplicate guesses
* ✅ Input validation
* 📋 Displays previously guessed letters
* 🏆 Win and loss conditions

## 🛠️ Built With

* Python 3
* `random` module
* Command-line interface

No external Python packages are required.

## 📁 Project Structure

```text
hangman/
│
├── main.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check by running:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Clone the repository

```bash
git clone https://github.com/RKSivasundari/reimagined-happiness.git
```

### 3. Enter the project directory

```bash
cd reimagined-happiness
```

### 4. Run the game

```bash
python main.py
```

## 🎮 Example

```text
=========================
   WELCOME TO HANGMAN!
=========================

Word: _ _ _ _ _ _

Guessed letters: None

Guess a letter: p

--> Good guess! 'p' is in the word.

Word: p _ _ _ _ _
```

## 📚 What I Learned

This project helped me practice:

* Variables
* Lists
* Sets
* Strings
* Functions
* `if` / `else` statements
* `while` loops
* List comprehensions
* Input validation
* Random selection
* Basic game logic

## 🚧 Future Improvements

Possible features to add in the future:

* [ ] Add difficulty levels
* [ ] Add word categories
* [ ] Add a score system
* [ ] Add multiple rounds
* [X] Add a play-again option
* [ ] Add a larger word database
* [ ] Add hints
* [ ] Add a high-score system

## 👤 Author

**RKSivasundari**

This project was created as a Python learning project.
