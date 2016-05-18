def DailyLife():
   choiceNumerouno = input("You wake up in the morning. Do you want to get out of bed? ")
if (choiceNumerouno) == "Yes":
    print ("You get out of bed.")

else:
    DailyLife()


DailyLife()
