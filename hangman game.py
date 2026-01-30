import random

words = ["python", "apple", "banana", "orange", "grapes"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("🎮 Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", used_letters)
    print("Attempts left:", attempts)

    letter = input("Guess a letter: ").lower()

    if letter in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)