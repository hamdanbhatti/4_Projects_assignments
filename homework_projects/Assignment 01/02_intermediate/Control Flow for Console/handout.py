import random

ROUNDS = 5

def start_game():
    total_score = 0
    print("=== High-Low Challenge ===")
    print("-" * 30)
    for round_num in range(ROUNDS):
        print(f"\n[Round {round_num + 1}]")
        player_num = random.randint(1, 100)
        cpu_num = random.randint(1, 100)
        print(f"Your draw: {player_num}")
        choice = input("Predict! Will the computer's number be (h)igher or (l)ower than yours? ").strip().lower()
        
        if choice not in {'h', 'l'}:
            print("Oops! That's not a valid choice. This round won't count.")
            continue

        if (choice == 'h' and cpu_num > player_num) or (choice == 'l' and cpu_num < player_num):
            print(f"Correct! Computer's number was {cpu_num}. +20 points.")
            total_score += 20
        elif cpu_num == player_num:
            print(f"It's a tie! Both got {cpu_num}. No points this round.")
        else:
            print(f"Wrong! Computer's number was {cpu_num}. No points.")

    max_possible = ROUNDS * 20
    print("\n--- Game finished! ---")
    print(f"Score: {total_score} out of {max_possible}")
    print(f"Accuracy: {(total_score / max_possible) * 100:.1f}%")

if __name__ == "__main__":
    start_game()