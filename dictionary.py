myDictionary = {
    "wanker":"jerk",
    "knackered":"tired",
    "chuffed":"pleased"
}

print(myDictionary.values()) 
print(myDictionary.keys()) 
print(myDictionary["wanker"])
#print(myDictionary["wanker"]) print(myDictionary["knackered"]) print(myDictionary["chuffed"])

sentence = "I am totally chuffed"
wordList = sentence.split(" ")
print(wordList)

for word in wordList:
    if word in myDictionary:
        print(myDictionary[word])