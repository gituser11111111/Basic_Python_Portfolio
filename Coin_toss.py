import random

count = 0
user_input = int(input("How many coin tosses would you like to be performed?: "))
games_played = 0
num = random.randint(0, 1)

for num in range(0, user_input):
    while True:
        games_played += 1
        num = random.randint(0, 1)
        if count == user_input:
            break
        if num == 0:
            print("heads")
        elif num == 1:
            print("tails")
        break
print('Total tosses: ', games_played)
