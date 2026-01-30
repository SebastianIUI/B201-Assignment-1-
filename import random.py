import random
import os
import time

char_list_all = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "1","2","3","4","5","6","7","8","9","0",
    "!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]",":",";","'","<",">",",",".","?","/","|","~","`"
]

special_chars = [
    "!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]",":",";","'","<",">",",",".","?","/","|","~","`"
]

choice = input("Would you like to include special characters in your password? (y/n): ").lower()
length = input("Enter the desired length of your password: ")

if not length.isdigit():
    print("Password length must be a number.")
    exit()

length = int(length)

if choice == "y":
    char_list = char_list_all
elif choice == "n":
    char_list = [c for c in char_list_all if c not in special_chars]
else:
    print("Invalid input. Please enter 'y' or 'n'.")
    exit()

output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Generated_Passwords.txt")

for _ in range(1000):
    password = "".join(random.choices(char_list, k=length))

    timestamp = time.strftime("%A, %Y-%m-%d %I:%M:%S %p", time.localtime())

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {password}\n")

