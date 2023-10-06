import string
import random
ay = 0
password = ""
for ay in range(3):
    i = random.choice(string.ascii_lowercase)
    password += i
for ay in range(2):
    o = random.choice(string.digits)
    password += o
for ay in range(3):
    u = random.choice(string.ascii_lowercase)
    password += u
print(password)
# Created by Leandro Macedo - 2023