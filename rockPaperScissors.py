from random import randint
rand_num = randint(0,2)
player = input("Player 1: scissors, rock or paper: ").lower()

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
    print("It's tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    else:
        print("Computer wins")
elif player == "scissors":
    if computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")
else:
    print("Please enter a valid move!")