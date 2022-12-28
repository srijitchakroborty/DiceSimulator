import random
print("Welcome to Dice Simulator. Let's roll the dice...")
while True:
    options=[1,2,3,4,5,6]
    dice=random.choice(options)
    print(f"The number chosen by dice is {dice}")
    inp = input("Press 'Enter' to roll the dice again. To stop press 'q' or 'Q' and then press 'Enter'.\n")
    if inp=="q" or inp=="Q":
        print("Thank you for using Dice Simulator")
        exit()