print("===Level 1 ===\n")
import random
num = random.randint(1, 30)

# get initial guess with validation
while True:
    try:
        guess = int(input("Guess a number 1-30: "))
        break
    except ValueError:
        print("Please enter a valid whole number.")

guess_limit = 5
guess_num = 0

while guess_num < guess_limit:
    if guess != num:
        guess_num += 1
        # check closeness using absolute difference
        if abs(guess - num) <= 5:
            try:
                guess = int(input(f'{guess_num}: {guess} cmmon you are very close 🥺. Guess again: '))
            except ValueError:
                print('Invalid input — counting as a guess. Please enter a number next time.')
                continue
        else:
            try:
                guess = int(input(f'{guess_num}: {guess} ohh You are far 😒. Guess again: '))
            except ValueError:
                print('Invalid input — counting as a guess. Please enter a number next time.')
                continue
    if guess == num:
        print(f"You won!🥳 It was {num}.😎")
        break

if guess != num:
    print("You have no chances left 😞. It was ", num)