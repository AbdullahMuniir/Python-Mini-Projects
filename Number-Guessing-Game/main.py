from random import randint

num = randint(1, 100)
you = 0
attempt = 1
# This Loop Compares user input with the number to be guessed
while(num != you):
    you = int(input("Guess The number: "))
    if(num > you):
        print("Higher number please!")
        attempt += 1
    elif(num < you):
        print("Lower number please!")
        attempt += 1
else:
    print(f"You guessed the number correctly in {attempt} Attempts")
# Reads the txt file and checks if empty or not
with open("Least-Attempts.txt") as f:
   content = f.read().strip()
   if content:
        prev_attempt = int(content)
   else:
       prev_attempt = None
# Writes the least number of Attempts in the txt file  
if(prev_attempt is None or attempt < prev_attempt):
    with open("Least-Attempts.txt", "w") as f:
        f.write(str(attempt))