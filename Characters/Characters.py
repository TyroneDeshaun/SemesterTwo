class Character:
    charCount = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type
        Character.charCount += 1

    def displayCount(self):
        print ("Total characters %d" % Character.charCount)

    def displayCharacter(self):
        print ("Name : ", self.name, " , Type: ", self.type)

char1 = Character("Tom", "Human")
char2 = Character("The Thang", "Dragon")
char1.displayCharacter()
char2.displayCharacter()
print ("Total Characters %d" % Character.charCount)
