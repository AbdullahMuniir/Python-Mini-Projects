import random
'''
snake = 0
water = 1
gun = 2

'''
computer = random.choice([0, 1, 2])
youStr = input("Enter your Choice 's', 'w', or 'g': ")
youDict = {
    "s": 0,
    "w": 1,
    "g": 2
}
if youStr not in youDict:
    print("Not a Valid Choice!.")
else:
    you = youDict[youStr]

    reverseDict = {
    0: "Snake",
    1: "Water",
    2: "Gun",
    }
    print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

    ''''
    Game Logic:
    computer(0) - you(1) = Lose(-1)
    computer(1) - you(0) = Win(1)
    computer(0) - you(2) = Win(-2)
    computer(2) - you(0) = Lose(2)
    computer(1) - you(2) = Lose(-1)
    computer(2) - you(1) = Win(1)
    -> -1 & 2 = Lose
    -> -2 & 1 = Win
    '''

    if(computer == you):
        print("It's a Draw!")
    elif(computer - you == 1 or computer - you == -2):
        print("You Win!")
    elif(computer - you == -1 or computer - you == 2):
        print("You Lose!")
    else:
        print("Somethig Went Wrong!")
