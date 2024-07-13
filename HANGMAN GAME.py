import random

def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'php', 'swift', 'kotlin', 'perl', 'csharp', 'html']
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed = []
    tries = 6

    while tries > 0:
        # Display word with placeholders for unguessed letters
        display_word = ''.join(letter if letter in guessed else '_' for letter in word)
        print(f"Word to guess: {display_word}")

        if display_word == word:
            print("Congratulations! You guessed the word.")
            break

        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        elif guess in guessed:
            print("You already guessed that letter.")
            continue
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a valid letter.")
            continue

        guessed.append(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect guess.")
        
        print()  # Just for better readability

    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
