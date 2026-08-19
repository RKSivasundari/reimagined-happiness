import random

# Visual stages for the hangman drawing
HANGMAN_PICS = [
    """
   +---+
       |
       |
       |
      ===""",
    """
   +---+
   O   |
       |
       |
      ===""",
    """
   +---+
   O   |
   |   |
       |
      ===""",
    """
   +---+
   O   |
  /|   |
       |
      ===""",
    """
   +---+
   O   |
  /|\\  |
       |
      ===""",
    """
   +---+
   O   |
  /|\\  |
  /    |
      ===""",
    """
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""",
]

# Word pool for the game
WORDS = [
    "python",
    "developer",
    "hangman",
    "algorithm",
    "terminal",
    "variable",
    "function",
    "computer",
]


def get_valid_guess(guessed_letters):
    """Prompts until the user enters a single, un-guessed letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess


def play_hangman():
    while True:
        secret_word = random.choice(WORDS)
        guessed_letters = set()
        incorrect_guesses = 0
        max_attempts = len(HANGMAN_PICS) - 1

        print("=========================")
        print("   WELCOME TO HANGMAN!   ")
        print("=========================")

        while incorrect_guesses < max_attempts:
            # Display state
            print(HANGMAN_PICS[incorrect_guesses])

            word_display = [
                char if char in guessed_letters else "_" for char in secret_word
            ]
            print("\nWord: " + " ".join(word_display))

            used_str = ", ".join(sorted(guessed_letters)) if guessed_letters else "None"
            print(f"Guessed letters: {used_str}\n")

            # Win check
            if "_" not in word_display:
                print(f"🎉 You win! You guessed the word: {secret_word.upper()}")
                break

            # Get and record player guess
            guess = get_valid_guess(guessed_letters)
            guessed_letters.add(guess)

            if guess in secret_word:
                print(f"--> Good guess! '{guess}' is in the word.\n")
            else:
                incorrect_guesses += 1
                remaining = max_attempts - incorrect_guesses
                print(
                    f"--> Incorrect! '{guess}' is not in the word. "
                    f"({remaining} attempts left)\n"
                )

        else:
            # Loss condition
            print(HANGMAN_PICS[incorrect_guesses])
            print(f"☠️ Game Over! The secret word was: {secret_word.upper()}")

        # Ask whether the player wants another game
        while True:
            play_again = input("\nPlay again? (y/n): ").lower().strip()

            if play_again in ("y", "n"):
                break

            print("Please enter 'y' for yes or 'n' for no.")

        if play_again == "n":
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    play_hangman()