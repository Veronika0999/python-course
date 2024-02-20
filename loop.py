#EXERCISE: Screaming Repeating
times = int(input("How many times do I have to tell you? "))

for y in range(times):
   print("CLEAN UP YOUR ROOM")

#EXERCISE: Unlucky Numbers
for number in range(1, 21):
    if number == 4 or number == 13:
        print(f"{number} is UNLUCKY!")
    elif number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")