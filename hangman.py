import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

display = []
for char in chosen_word:
    display.append("_")
print(logo)
guesses = []

while "_" in display and lives > 0:
    letter = input("Guess a letter: ").lower()
    counter = 0

    if letter in guesses:
        print(f"You have already guesses the letter {letter}. Guess again.")
    else:
        guesses.append(letter)

        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                display[i] = letter
                counter += 1
        if counter == 0:
            print(f"{letter} is not in the word.")
            lives -= 1
    print(" ".join(display))
    print(stages[lives])

if lives > 0:
    print("You Win!")
else:
    print(f"You lose. The word was {chosen_word}")
