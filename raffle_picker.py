part_num = int(input("Enter how many participants are taking part today: "))
if part_num < 3:
    print("Please enter at least 3 names")
    exit()

participants = []
for i in range(part_num):
    name = input(f'Enter name #{i+1}: ')
    participants.append(name)

prizes = []
for i in range(3):
    prize = input(f'Enter prize #{i+1}: ')
    prizes.append(prize)

import random
# if there are fewer participants than prizes, reduce number of prizes
num_winners = min(len(participants), len(prizes))
winners = random.sample(participants, num_winners)

print(f'\nTotal number of contestants: {part_num}')
print("\n===🎉Raffle winners===")
for i in range(num_winners):
    if i == 2 and i < len(winners):
        print(f'\n🏆Grand Prize :{winners[i].capitalize()} wins the {prizes[i]} ')
    else:
        print(f'{winners[i].capitalize()} wins the {prizes[i]}')