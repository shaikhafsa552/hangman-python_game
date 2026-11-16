import random

# ==========================================
#       HANGMAN - PYTHON INTERNSHIP
# ==========================================

WORD_HINTS = {
    "apple": "A fruit that can be red or green.",
    "python": "A popular programming language.",
    "computer": "An electronic computing device.",
    "school": "A place where students learn.",
    "flower": "A beautiful part of a plant.",
    "program": "A set of instructions for a computer.",
    "keyboard": "An input device used for typing.",
    "internet": "A worldwide network of computers."
}

DIFFICULTIES = {
    "1": ("Easy", 6, 10),
    "2": ("Medium", 5, 20),
    "3": ("Hard", 3, 30)
}


def display_welcome():
    print("\n" + "=" * 42)
    print("          WELCOME TO HANGMAN")
    print("       Python Programming Project")
    print("=" * 42)


def choose_difficulty():
    print("\nChoose your difficulty:")
    print("1. Easy   - 6 attempts")
    print("2. Medium - 5 attempts")
    print("3. Hard   - 3 attempts")

    while True:
        choice = input("Enter choice (1-3): ").strip()

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Invalid choice! Please enter 1, 2 or 3.")


def display_word(secret_word, guessed_letters):
    result = ""

    for letter in secret_word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


def play_round():
    difficulty, attempts, points = choose_difficulty()

    secret_word = random.choice(list(WORD_HINTS.keys()))
    guessed_letters = set()
    hint_used = False

    print("\nYou selected:", difficulty)
    print("Type 'hint' to get a clue.")
    print("-" * 42)

    while attempts > 0:

        print("\nWord:", display_word(
            secret_word, guessed_letters
        ))

        print("Attempts remaining:", attempts)
        print("Guessed letters:", 
              ", ".join(sorted(guessed_letters)) or "None")

        if all(letter in guessed_letters
               for letter in secret_word):

            print("\nCongratulations! You won!")
            print("The word was:", secret_word)

            if hint_used:
                points = max(0, points - 5)

            print("Points earned:", points)
            return points

        guess = input("\nEnter a letter or hint: ")
        guess = guess.lower().strip()

        # Hint feature
        if guess == "hint":

            if not hint_used:
                print("HINT:", WORD_HINTS[secret_word])
                hint_used = True
            else:
                print("You have already used your hint!")

            continue

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

    return 0


def main():
    total_score = 0

    display_welcome()

    while True:

        earned_points = play_round()
        total_score += earned_points

        print("\n" + "=" * 42)
        print("YOUR TOTAL SCORE:", total_score)
        print("=" * 42)

        while True:
            play_again = input(
                "\nWould you like to play again? (yes/no): "
            ).lower().strip()

            if play_again in ("yes", "no"):
                break

            print("Please enter yes or no.")

        if play_again == "no":
            break

    print("\nThank you for playing Hangman!")
    print("Your final score:", total_score)
    print("Have a wonderful day!")


# Start the game
if __name__ == "__main__":
    main()
