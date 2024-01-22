import time
import random
import os

darkfirstquestion=input("Is your favorite color red, yes or no? ")
capequestion=input("Do you like capes, yes or no? ")
if darkfirstquestion.capitalize()=="No" and capequestion.capitalize()=="Yes":
    print("You are part of the Dark Side")
elif capequestion.capitalize() and darkfirstquestion.capitalize()=="Yes":
    print("You are now part of the Dark Side")
else:
    print("You are now part of the Light Side")