import random
random_number = random.randint(1,10)

while True:
    user = int(input("Guess a number between 1 and 10: "))
    if random_number > user:
        print("Too low, try again!")
    elif random_number < user:
        print("Too high, try again!")
    elif random_number == user:
        print("You guessed it! You won!")
        question = input("Do you want to keep playing? (y/n) ")
        if question == "y":
            random_number = random.randint(1, 10)
            user = int(input("Guess a number between 1 and 10: "))
        else:
            print("Thank you for playing")
            break
