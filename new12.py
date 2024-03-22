# ask user to imput some sentence
string_sentence=input("Type any thing you want")
# print this sentence
print(string_sentence)
# convert string into a list of words
split_sentence=string_sentence.split()
# print list
print(split_sentence)
# initialise new sentence as empty
new_sentence=""
# the range is the number of words in the list
for i in range(len(split_sentence)):
# use the condition to alternate every word    
    if i%2==0:
# start with upper case     
      new_sentence += split_sentence[i].upper()+ " "
# then alternate lower case      
    else:
      new_sentence += split_sentence[i].lower()+ " "
# print the final altewrnating word from upper to lower case      
      
print(new_sentence)

