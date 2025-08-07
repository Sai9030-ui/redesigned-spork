import random

# Words the player might guess
WORDS = ['python', 'hangman', 'developer', 'interface', 'variable', 'function', 'keyboard']

# Choose a random word
word_to_guess = random.choice(WORDS).lower()
guessed_letters = set()
correct_letters = set(word_to_guess)
max_attempts = 6
attempts_left = max_attempts

# Display placeholders for the word
def get_display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])

# Greet the player
print("👋 Welcome to the Hangman Game!")
print("📝 I’ve picked a word. You need to guess it, one letter at a time.")
print(f"❗ You have {max_attempts} incorrect attempts before you lose the game.\n")

# Game loop
while attempts_left > 0:
    print(f"Word: {get_display_word()}")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    guess = input("🔤 Type a letter and press Enter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter only a single letter (A-Z).\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You’ve already guessed that letter. Try a different one.\n")
        continue

    guessed_letters.add(guess)

    if guess in correct_letters:
        print("✅ Good guess!\n")
        if correct_letters.issubset(guessed_letters):
            print(f"🎉 Congratulations! You’ve guessed the word: **{word_to_guess}**")
            break
    else:
        attempts_left -= 1
        print(f"❌ Nope! The letter '{guess}' is not in the word. Attempts left: {attempts_left}\n")

# End of game
if not correct_letters.issubset(guessed_letters):
    print(f"\n💀 Game Over! The word was: **{word_to_guess}**")
