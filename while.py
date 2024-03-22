# ask user to enter a number
user_input_number=int(input("Enter a number positive or negative between 0 and 100"))
# print this number on the next line
print(user_input_number)
# initialise number of inputs
user_input_count=0 
total=0
# count the number of input
# keep inputting till the number -1 is selected
while user_input_number != -1:
   total += user_input_number
   user_input_count += 1
   user_input_number=int(input("Enter a number positive or negative between 0 and 100"))
   print(user_input_number)   
   # find the average of all numbers entered
ave = float(total/user_input_count)
   # print the average of all inputs
print(f"The average of all your inputs is {ave}")

