# aak user to input something
string_sentence= input("type any thing you want")
# inktialise new sentence as empty
new_sentence=""
# convert string into list
for i in range (len(string_sentence)):
# use the condition to alternate upper and lower case for every other letter  
  if i%2 == 0:
# start then alternate upper case for every other letter
    new_sentence += string_sentence[i].upper()
    # every other letter should be lower case
  else:
    new_sentence += string_sentence[i].lower()
    # print final sentence
print(new_sentence)





                      

    

