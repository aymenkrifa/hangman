import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list).lower()
display = ["_"] * len(chosen_word)

print(f"{hangman_art.logo}\nPssst, the solution is {chosen_word}")

number_lives = 6

while ("_" in display) and (number_lives != 0):
    user_guess = input("Guess a letter: ").lower()

    if user_guess not in chosen_word:
        print(f"{user_guess.upper()} IS NOT IN THE WORD, YOU LOSE A LIFE")
        number_lives -= 1
    elif user_guess in display:
        print(f"YOU HAVE ALREADY GUESSED {user_guess.upper()}")

    for _ in range(len(chosen_word)):
        if chosen_word[_] == user_guess:
            display[_] = chosen_word[_]

    print(f"{' '.join(display)} | Number of lives left: {number_lives}")
    print(hangman_art.stages[number_lives])

if number_lives == 0:
    print("Unfortunately, you lose :(")
else:
    print("Congratulations, you win!")
