import re

def tokenize(text):
    return re.findall(r'\w+', text.lower())

profane_tokens = {"whitey","pikey","nigga","Crow",}

f = open("twitter.txt", "r") #Read the file
#loop through every line 
for x in f:      
    sentence = x
    tokens = tokenize(sentence)

# Rate: number of occurrences normalized by total number
degree_of_profanity = sum(1 for t in tokens if t in profane_tokens) / len(tokens)
print(degree_of_profanity)
