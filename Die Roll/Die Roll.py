import random
diceRoll = str(input("Type roll to roll a die "))
test = True

while (test==True):
    if diceRoll == ("roll"):
        roll = random.randint(1,6)
        print (roll)
        break
    else:
        print ("Goodbye")

