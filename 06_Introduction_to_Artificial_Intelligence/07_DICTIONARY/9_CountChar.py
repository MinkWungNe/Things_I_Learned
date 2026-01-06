greetings = "hello! how are you?"

charDict = {}

# Decompose string, count number of each character in the string
print('Using normal dict decomposing --------------------------------------')
for char in greetings:
    if char not in charDict.keys():
        charDict[char] = 1  # new char
    else:
        charDict[char] += 1 # existed char, increase it by 1

for key, value in charDict.items():
    print(key, ":", value)
    
# .get() use to get the values
print('Using .get() -------------------------------------------------------')
for char in greetings:
    charDict[char] = charDict.get(char, 0)+1  # get(key, initial value)

for key, value in charDict.items():
    print(key, ":", value)