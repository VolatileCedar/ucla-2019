# Fix s so that only the first letter of each name is capitalized
# Hints:
#   1) If you have just one name in a string by itself,
#   you can capitalize it like this:
#       name = "josePH"
#       name = name.capitalize()
#   2) You can split s into a list of individual names
#       Example:
#           myString = "This is a sentence."
#           wordList = myString.split(" ")
#           print(wordList)
#   3) Loop through your list of separated names to capitalize them
#   4) Join the names back together into one string
#       Example:   (not complete)
#           newS = ""
#           for word in wordList:
#               newS = newS+word
#           print(newS)      

s = "josePH JiMmY john jAmes jASMine"
d = s.split(" ")

aList = []
for i in d:
    c = i.capitalize()
    aList.append(c)

newS = ""
for word in aList:
   newS = newS+word
   newS+=" "
print(newS)

#for i in s:
    #print(i,capitalize())



#when you are done, this should print
# Joseph Jimmy John James Jasmine