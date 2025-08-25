import random

# create a bag with 10 marbles
bag = ('green', 'green', 'black', 'green', 'green', 'red', 'white', 'green', 'red', 'red')

# starting amount of money
starting_purse = 1000
# current money amount
purse = starting_purse
# result of last round
result = 0
# how many rounds
rounds = 3
# last marble
marble = 'none'
# welcome user to game
print(f'You start the game with {starting_purse} rupees')

# loop drawing marbles
for draw in range(1, rounds + 1):
    while True:
        try:
            bet = int(input(f'current purse: {purse} Last draw: {marble} \nRound{draw}- How much you want to bet?: '))
            if bet <= 0:
                print('Bet must be a positive whole number.')
                continue
            if bet > purse:
                print('You cannot bet more than your current purse.')
                continue
            break
        except ValueError:
            print('Please enter a valid whole number for the bet.')

    # choosing marble
    marble = random.choice(bag)
    # win or loss
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10 * bet
    elif marble == 'white':
        result = -5 * bet
    else:
        result = -bet

    # calc win or loss/ result and new amount
    purse += result

    # lose game if lose half of money
    if purse < 0.5 * starting_purse:
        print('You lost half of your money. PLAY AGAIN LATER!')
        break

    # print results
    print(f'New purse amount: {purse} : last result: ({marble}) : {result}')
    print('')
# print final results/summary
print(f'starting/ending purse = {starting_purse}/{purse}')
print(f'gain/loss = {(purse - starting_purse) / starting_purse * 100}%')
