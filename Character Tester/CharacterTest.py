import random
x = random.randint(1,600)

name = str(input("Type in your character's name. "))

class Character:
    charCount = 0
    
    def __init__(self ,name, hp, species):
        self.name = name
        self.characterHp = hp
        Character.charCount +=1
        self.species = species

    
    def displayCount(self):
        print ("Total Characters %d" % Character.charCount)

    def displayCharacter(self):
        print ("Name : ", self.name, " , HP: ", self.characterHp, " , Type: ", self.species)

if x >= 500:
    species = "Dragon"
elif x >=400:
    species = "Goblin Captain"
elif x >= 250:
    species = "Hero"
else:
    species = "Grunt"

if x >= 500:
    monster1 = Character(name , x, species)
    import Dragon
    monster1.displayCharacter()
elif x >=400:
    monster2 = Character(name , x, species )
    import GoblinCaptain
    monster2.displayCharacter()
elif x >= int(250):
    monster3 = Character(name , x, species)
    import Hero
    monster3.displayCharacter()
else:
    monster4 = Character(name, x, species)
    import Grunt
    monster4.displayCharacter()


diceRoll = str(input("Type roll to roll for your strength number. "))
test = True
while (test==True):
    if diceRoll == ("roll"):
        strength = random.randint(1,10)
        break
    else:
        print ("Goodbye")
        break
        
diceRoll2 = str(input("Type roll to roll for your intelligence number. "))
while (test==True):
    if diceRoll2 == ('roll'):
        intelligence = random.randint(1,10)
        break
    else:
        print ("Goodbye")
        break
diceRoll3 = str(input("Type roll to roll for your luck number. "))
while (test==True):
    if diceRoll3 == ('roll'):
        luck = random.randint(1,10)
        break
    else:
        print("Goodbye")
        break
print("Your overall stats are ")
print("Strength is " + str(strength))
print("Intelligence is " + str(intelligence))
print("Luck is " + str(luck))

goldAmount1 = str(input("Type in roll to roll for the amount of gold you start with. "))
while (test==True):
    if goldAmount1 == ('roll'):
        gold = random.randint(1,100)
        print("Your starting gold is " + str(gold))
        break
    else:
        print('Goodbye')
        break

print('Starting gold is ' + str(gold))
startadventure = str(input("Do you want to go on an adventure? ").lower())
while (test==True):
    if startadventure == ('yes'):
        break
    else:
        print("Why waste so much time then?")
        print("Bye")
        break
