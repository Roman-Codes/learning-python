import random

print("Welcome to the number guessing game!")

number = random.randint(0,100)

game_over = False

difficulty = input("Choose difficulty. 'Hard' or 'Easy'. ").lower()

attempts = 5 if difficulty == 'hard' else 10

def make_a_guess():
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input('Make a guess: '))
    if guess < number:
        print('Too Low! Guess Again!')
        return attempts - 1
    elif guess > number:
        print('Too High! Guess Again!')
        return attempts - 1
    else:
        print(f'You guessed correctly it is {guess}')
        global game_over
        game_over = True

while not game_over:
    if attempts == 0:
        game_over = True
    make_a_guess()