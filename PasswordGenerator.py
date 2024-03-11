import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
password = []

print("Welcome to my password generator")
size = int(input("How many characters would you like in your password?\n"))
amount_of_num = int(input("How many numbers would you like in your password?\n"))
amount_of_symbols = int(input("How many symbols would you like in your password?\n"))

for k in range(amount_of_symbols):
    password += random.choice(symbols)
for j in range(amount_of_num):
    password += random.choice(digits)
for i in range(size - amount_of_num - amount_of_symbols):
    password += random.choice(letters)

random.shuffle(password)

password = "".join(password)


print(f"Your password is {password}")




