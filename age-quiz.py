# ask user to input their age in years
age = int(input("Enter your age in years"))
# if over 40 print 'You're over the hill'
if age < 65:
 print("You're over the hill")
# if user enters >=100 print 'sorry you're dead
elif age >= 100:
 print("Sorry you're dead")
# if user inputs >=65 print 'enjoy your retirement'
elif age >= 65:
 print("Enjoy your retirement")
# if user enters <13 print 'you qualify for the kiddie discount'
elif age < 13:
 print("You qualify for the kiddie discount")
# if user enters 21 print 'congrats on your 21st'
elif age==21:
 print("Congrats on your 21st")
# for anything else print 'Age is but a number' 
else:
 print("Age is but a number")                          