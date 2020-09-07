from cs50 import get_float

# get user input 
while True:
    amount = get_float("Change owed: ")
    
    # keep prompting unless the value is > 0
    if amount > 0:
        break
    
# convert amount to cents
cents = int(amount * 100)

coins = 0
for denom in [25, 10, 5]:
    # number of coins for current denoms
    denom_coins = cents // denom
    coins += denom_coins
    
    # remaining amount
    cents -= denom_coins * denom

# add remaining cents for 1c coins
coins += cents

print(coins)