import datetime;
now = datetime.datetime.now()

userInput = input("Please enter your birthday in YYYY/MM/DD Format ")

if (len(userInput) == 10):
    userDays = (userInput[8:10])
    userMonths = (userInput[5:7])
    userYears = (userInput[0:4])
    millenniums = (now.year - int(userYears))/1000
    centuries = (now.year - int(userYears))/100
    decades = (now.year - int(userYears))/10
    testyears = now.year - int(userYears)
    testmonths = now.month - int(userMonths)
    testdays = now.day - int(userDays)
    timeDif = (testyears * 365 + testmonths * 30.4 + testdays)
    smallerTimeDif = (timeDif * 24)
    years= int(timeDif/365)
    months = timeDif * 365 * 30.4
    days = timeDif * 365
    hours = timeDif * 24
    minutes = timeDif * 24 * 60
    seconds = timeDif * 24 * 60 * 60
    print ("You are ", millenniums, "millenniums old.")
    print ("You are ", centuries, "centuries old.")
    print ("You are ", decades, "decades old.")
    print ("You are ", years, "years old.")
    print ("You are ", months, "months old.")
    print ("You are ", days, "days old.")
    print ("You are ", hours, "hours old.")
    print ("You are ", minutes, "minutes old.")
    print ("You are ", seconds, "seconds old.")
else:
    print ("You piece of garbage you didn't enter in the format.")

