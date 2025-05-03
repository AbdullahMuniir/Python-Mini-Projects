import random
import string
import time
# Get Username from user
username = input("Enter Username: ")
# Make sure Username is least 8 digit
if(len(username) < 8):
    raise ValueError("Username must be at least 8 Characters")
# Function to Generate password
def generate_pass(length = 8):
    char =  string.ascii_lowercase + string.digits + string.ascii_uppercase
    code = ''.join(random.choice(char) for i in range(length))
    return code
password = generate_pass()
# Print Passwor $ Username
print("Generating password...")
time.sleep(3)
print("here You Go...")
time.sleep(1)
print(f"Username: {username}\nPassword: {password}")
