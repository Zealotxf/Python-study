from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
name = input("What's you name?")
age = input("How old are you?")
sex = input("What's your sex?")

print(f"I'm {name} , {age} years old and I'm a {sex}.")
