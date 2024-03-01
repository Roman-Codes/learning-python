import random
import art

art_list = [art.rock, art.paper, art.scissors]
word_list = ["Rock", "Paper", "Scissors"]

player_choice = int(input('Choose your destiny! Rock - 0, Paper  - 1, Scisors - 2\n'))
computer_choice = random.randint(0,2);

if player_choice >= 3:
    print('out of range')

print(f"Player chose {word_list[player_choice]}\n{art_list[player_choice]}")
print(f"Computer chose {word_list[computer_choice]}\n{art_list[computer_choice]}")

if player_choice == computer_choice:
    print("its a draw")
elif player_choice == 0 and computer_choice == 1:
    print("Computer Won")
elif player_choice == 0 and computer_choice == 2:
    print("Player Won")
elif player_choice == 1 and computer_choice == 0:
    print("Player Won")
elif player_choice == 1 and computer_choice == 2:
    print("Computer Won")
elif player_choice == 2 and computer_choice == 0:
    print("Player Won")
elif player_choice == 2 and computer_choice == 1:
    print("Computer Won")