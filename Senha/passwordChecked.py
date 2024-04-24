import os 
from random import *

user_pwd = input("\n\nEnter password\n: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','@','.','&']

pw = ''
while (pw != user_pwd):
    pw = ''
    for term in range(len(user_pwd)):
        guess_pwd = pwd[randint(0,38)]
        pw = str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password... Please Wait")
        os.system('cls')
print(f"Your Password is: {pw}")

