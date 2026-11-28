import random
import string
import secrets


chars = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$&"
length: int = 1
length_max = int(input("password length value: ")).strip()
print("jacks password generator")
def gen_pass():
    upcase = string.ascii_uppercase
    password = ""
    remaining_length = length_max - length
    for _ in range (length_max):
        charater = secrets.choice(chars)
        random.shuffle(charater)
        password += charater
        if len(password) == length_max:
            print(password)

gen_pass()
input("\nPress Enter to exit...")