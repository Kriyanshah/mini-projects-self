# snake water gun game the less readable code
import random

# 1 for snake, -1 for water, 0 for gun
t = int(input("Enter the number of rounds you want to play: "))
for i in range(t):
    print("                 Round", i+1)
    computer = random.choice([-1, 0, 1]) 
    youstr = input("Enter your choice (s, w, g): ").lower()
    youdict = {"s": 1, "w": -1, "g": 0}
    reversedict = {1 : "snake", -1 : "water", 0 : "gun"}
    you = youdict[youstr]

    print(F"you chose {reversedict[you]} and computer chose {reversedict[computer]}")

    if you == computer:
        print("It's a tie!")
    else:
        if (computer-you) == -2 or (computer-you) == 1:
            print("You win!")
        elif (computer-you== -1) or (computer-you) == 2:
            print("You lose!")
        else:
            print("Something went wrong!")
print("                Thanks for playing!")