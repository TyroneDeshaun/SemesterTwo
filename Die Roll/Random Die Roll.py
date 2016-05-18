import random
y1 = random.randint(1,6)
y2 = random.randint(1,6)
y3 = random.randint(1,6)
y4 = random.randint(1,6)
y5 = random.randint(1,6)
y6 = random.randint(1,6)
  

userInput = int(input("How many die do you want to roll?(Up to 5) "))
x = userInput

if x == 1:
    print ("You rolled 1 die")
    print ("Die 1 rolled a " + (str(y1)))

elif x == 2:
    print ("You rolled two die")
    print ("Die 1 rolled a " + (str(y1)))
    print ("Die 2 rolled a " + (str(y2)))

elif x == 3:
    print ("You rolled three die")
    print ("Die 1 rolled a " + (str(y1)))
    print ("Die 2 rolled a " + (str(y2)))
    print ("Die 3 rolled a " + (str(y3)))

elif x == 4:
    print ("You rolled four die")
    print ("Die 1 rolled a " + (str(y1)))
    print ("Die 2 rolled a " + (str(y2)))
    print ("Die 3 rolled a " + (str(y3)))
    print ("Die 4 rolled a " + (str(y4)))

elif x == 5:
    print ("You rolled five die")
    print ("Die 1 rolled a " + (str(y1)))
    print ("Die 2 rolled a " + (str(y2)))
    print ("Die 3 rolled a " + (str(y3)))
    print ("Die 4 rolled a " + (str(y4)))
    print ("Die 5 rolled a " + (str(y5)))

else:
    print ("That isn't 1-5. Get out of here.")
