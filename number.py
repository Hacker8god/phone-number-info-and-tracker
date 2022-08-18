import random
import math
lower=int(input("Enter lower bound:-"))
upper=int(input("Enter lower bound:-"))
x=random.randint(lower, upper)
print("\ntYou've only ", round (math.log(upper-lower +1,)),"chances to guess the integer!\n")
count=0
while count<math.log(upper-lower + 1,2):
    count+=1
    guess=int (input("guess a number:-"))
    if x==guess:
        print("Congratulations you guess right! " ,count,"Try")
        break
    elif x>guess:
        print("You guess too small")
    elif x<guess:
        print("You guess too high")
if count>=math.log(upper-lower +1):
    print("\nThe number is %d" % x)
    print("\ntBetter luck next time!")
else:
    print("Good job..!")