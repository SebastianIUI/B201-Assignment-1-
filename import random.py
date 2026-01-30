import random
import os.path
import time 

os.path.join(os.path.dirname(__file__))

List = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "1","2","3","4","5","6","7","8","9","0",
        "!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]",":",";","'","<",">",",",".","?","/","|","~","`"]   


choice = input("Would you like to include special characters in your password? (y/n): ")

Length = input("Enter the desired length of your password:")

special_chars = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]",":",";","'","<",">",",",".","?","/","|","~","`"]

if choice.lower() == 'y':
    char_list = List
elif choice.lower() == 'n':
    char_list = [c for c in List if c not in special_chars]
elif choice.lower() != 'y' or 'n':
    print("Invalid input. Please enter 'y' or 'n'.")
    exit()
        
for i in range (1):
    Password = random.choices(char_list, k=int(Length))
    Password = ''.join(Password)
    print(Password)


timestamp = time.strftime("%A, %Y-%m-%d %I:%M:%S %p")

output_file = os.path.join(os.path.dirname(__file__), "Generated_Passwords.txt")

with open(output_file, "a", encoding="utf-8") as f:
    f.write(f"{timestamp} | {Password}\n")
