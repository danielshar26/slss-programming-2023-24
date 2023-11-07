age=int(input("how old are you? "))
endAge= age + 26
print(f"you will be {endAge} in 2049")

#This asks the judge to enter their score.
viewer_one = float(input("Enter the score you see fit viewer number 'ONE'"))
viewer_two = float(input("Enter the score you see fit viewer number 'TWO'"))
viewer_three = float(input("Enter the score you see fit viewer number 'THREE'"))
viewer_four = float(input("Enter the score you see fit viewer number 'FOUR'"))
viewer_five = float(input("Enter the score you see fit viewer number 'FIVE'"))

#This adds up the scores from all of the judges.
math = viewer_one + viewer_two + viewer_three + viewer_four + viewer_five

#This verifies the total score is equal or greater then 50 and responds accordingly.
if math >= 50:
    print(f"The viewers have given a POSTIVE score of: {math}")
else:
    print(f"The viewers have given a NEGATIVE score of: {math}")
sandwhich=input("do you want a sandwhich for 5$ (yes/no) ")
frenchfries=input("do you want some french fries for 3$ (yes/no) ")
finalCost=0
if sandwhich.lower()== "yes":
    finalCost+=5
if frenchfries.lower()=="yes":
    finalCost+=3
tax=finalCost* 0.14
print(f"${tax+ finalCost}")