import random

choices = ["rock", "paper", "scissors", "quit"]

computer = choices[random.randint(0, 2)]

computer_win_count = 0
player_win_count = 0
gamesPlayed = 0

while True:
    gamesPlayed += 1
    computer = choices[random.randint(0, 2)]
    user_input = input("Choose: rock, paper, scissors, or quit: ")
    if user_input == computer:
        print("Human choice:", user_input, "Computer choice:", computer, "Tie")
    elif user_input == "rock":
        if computer == "scissors":
            player_win_count += 1
            print("Human choice:", user_input, "Computer choice:", computer, "player wins")
        else:
            computer_win_count += 1
            print("Human choice:", user_input, "Computer choice:", computer, "computer wins")
    elif user_input == "scissors":
        if computer == "paper":
            player_win_count += 1
            print("Human choice:", user_input, "Computer choice:", computer, "player wins")
        else:
            computer_win_count += 1
            print("Human choice:", user_input, "Computer choice:", computer, "computer wins")
    elif user_input == "paper":
        if computer == "rock":
            player_win_count += 1
            print('Human choice:', user_input, 'Computer choice:', computer, 'player wins')
        else:
            computer_win_count += 1
            print('Human choice:', user_input, 'Computer choice:', computer, 'computer wins')
    else:
        print("Computer wins: ", computer_win_count)
        print("Player wins: ", player_win_count)
        break