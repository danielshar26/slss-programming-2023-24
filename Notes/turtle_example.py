# Turtle example
# Author: Daniel
# 21 Nov 2023

import turtle

# --- CONSTANTS
TURTLE_MAGNITUDE = 20

# create a turtle
michaelangelo = turtle.Turtle()

# get some instrutions
print("""To give commands, type:
F - to go forward
L - to go left
R - to go right
B - to go backwards
STOP - to stop the code""")

# repeat the below code indefinitely
done = False 

while not done:
    command = input("Where should I go? ").strip(",.?!").lower()

    # based on those instructions from the user, move the turtle on the screen
    if command.strip(",.?!") == "f":
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command.strip(",.?!") == "l":
        michaelangelo.left(90)
    elif command.strip(",.?!") == "r":
        michaelangelo.right(90)
    elif command.strip(",.?!") == "b":
        michaelangelo.forward(-TURTLE_MAGNITUDE)
    elif command == "stop":
        done = True

