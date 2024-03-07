import random
from subprocess import check_output
from data import data
import art

print(art.logo)

vs_image = art.vs


def generate_pick_string(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"

def play_game():
    score = 0
    game_over = False
    pick_a = random.choice(data)
    pick_b = random.choice(data)

    while not game_over:
        pick_a = pick_b
        pick_b = random.choice(data)
        
        while pick_a == pick_b:
            pick_b = random.choice(data)

        print(f"Compare A: {generate_pick_string(pick_a)}")
        print(vs_image)
        print(f"Against B: {generate_pick_string(pick_b)}")

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (choice == "a" and pick_a['follower_count'] > pick_b['follower_count']) or (choice == "b" and pick_a['follower_count'] < pick_b['follower_count']):
            score += 1
            print('Great success!')
        else:
            print(f'You loose! You got score of {score}')
            game_over = True

play_game()