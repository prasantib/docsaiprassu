#opening and reading the file
with open("pi_digits.txt") as file:
    contents = file.read()
    print(contents.rstrip())
    
#printing each item in the text as a line
filepath = "pi_digits.txt"

with open(filepath) as file:
    for line in file:
        print(line)
#printing each line as a string in a list
filepath = "pi_digits.txt"
with open(filepath) as file:
    lines = file.readlines()
print(lines)
for line in lines:
    print(line.rstrip())

#printing each line together in one string
filepath = "pi_digits.txt"
with open(filepath) as file:
    lines = file.readlines()
pi_str = ''
for line in lines:
    pi_str += line.strip()
    print(pi_str)

filepath = "pi_million_digits.txt"
with open(filepath) as file:
    lines = file.readlines()
pi_str = ''
for line in lines:
    pi_str += line.strip()
print(pi_str[:52] + "...")
print(len(pi_str))
#finding text in a file
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_str:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

#writing text to the file and adding to it.
filename = "programming.txt"
with open(filename, 'w') as file:
    file.write("I love programming.")
filename = "programming.txt"
with open(filename, 'w') as file:
    file.write("I love programming. \n")
    file.write("I love creating new games. \n")
#adding more text to the file
with open(filename, 'a') as file:
    file.write("I also love finding meaning in large datasets. \n")
    file.write("I love creating apps that can run in a browser. \n")
#exceptions
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("The rest of the code can run.")
print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

#file not found        
filepath = "alice.txt"
try:
    with open(filepath, encoding = 'utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filepath + " does not exist."
    print(msg)
    
#splitting text from a white space and printing to a list
title = "Alice in Wonderland"
title.split()

title.split("e")
filepath = "alice.txt"
try:
    with open(filepath, encoding = 'utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filepath + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filepath + " has about " + str(num_words) + "words.")
#using the define function in order to call the function
def count_words(filename):
    try:
        with open(filename, encoding = 'utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
count_words(filepath)

files = ['alice.txt', 'siddartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in files:
    count_words(file)

#using json to store data
import json
numbers = [2,3,5,7,11,13]
filename = "numbers.json"
with open(filename, 'w') as file:
    json.dump(numbers,file)
with open(filename) as file:
    num_ls = json.load(file)
print(num_ls)

username = input("What is your name? ")
filename = "username.json"
with open(filename, 'w') as file:
    json.dump(username, file)
    print("We'll remember when you come back, " + username + "!")
with open(filename) as file:
    username = json.load(file)
    print("Welcome back, " + username)

def greet_user():
    filename = "username.json"
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as file:
            json.dump(username, file)
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()
#using functions to call program
def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as file:
            json.dump(username, file)
            print("We'll remember you when you come back, " + username + "!")
greet_user()
#create new function
def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username
        print("We'll remember you when you come back, " + username + "!")
greet_user()
