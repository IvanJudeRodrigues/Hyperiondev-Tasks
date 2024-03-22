# ask user for time to complete smimming in the triathlon
swimming_time=int(input("what is your swimming time in minutes"))
print(swimming_time)
# ask user for time to complete cycling in the triathlon
cycling_time=int(input("what is your cycling time in minutes"))
print(cycling_time)
# ask user for time to complete running in the triathlon
running_time=int(input("what is your running time in minutes"))
print(running_time)
# qualifying time is time for whole triathlon
qualifying_time=swimming_time+cycling_time+running_time
# print qualifying time
print(qualifying_time)
# there are different awards for different times
if qualifying_time <=100:
    print("Provincial colours")
elif qualifying_time <=105:
    print("provincial half colours")
elif qualifying_time <=110:
    print("provincial scroll")
else: 
    print("no award")
