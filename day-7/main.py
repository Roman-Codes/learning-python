import random
import art
import word

logo = art.logo
stages = art.stages

word_list = word.word_list

chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display += "_"

game_over = False

lives = len(stages)

print(logo)

while not game_over:
    guessed_letter = input('Guess the letter: ').lower()

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            print('You got it!')
            display[position] = guessed_letter

    if guessed_letter not in chosen_word:
        print("Chuck Testa!")
        print(stages[lives - 1])
        lives -= 1

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("Victory")
    elif lives == 0:
        game_over = True
        print("You Loose!")