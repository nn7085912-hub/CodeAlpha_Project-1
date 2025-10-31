import random  # Step 1: Import random module

def hangman():
    # Step 2: Create a small list of words
    word_list = ["apple", "tiger", "chair", "piano", "beach"]

    # Step 3: Randomly choose a word
    secret_word = random.choice(word_list)

    # Step 4: Initialize variables
    guessed_letters = []
    word_progress = ["_"] * len(secret_word)
    attempts_remaining = 6

    # Step 5: Display intro message
    print("🎯 Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses allowed.\n")

    # Step 6: Main game loop
    while attempts_remaining > 0 and "_" in word_progress:
        print("Word:", " ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {attempts_remaining}")
        
        guess = input("Enter a letter: ").lower()

        # Step 7: Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.\n")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        # Step 8: Check if guess is correct
        if guess in secret_word:
            print("✅ Good guess!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts_remaining -= 1

    # Step 9: Game over message
    if "_" not in word_progress:
        print(f"🎉 Congrats! You guessed the word: {secret_word}")
    else:
        print(f"💀 Out of attempts! The word was: {secret_word}")

# Step 10: Run the game
hangman()
