two_ways = "rsecwyadrkd"
print(two_ways)

# print the string with step 2
print(two_ways[::2])

# print the string with step -2 (start backward with step 2)
print(two_ways[::-2])

# concatcinate 2 strings
daya = 'cười'
dayb = ' vui'
combo = daya + dayb
print(combo)    # should be 'cười vui'

# copy a string 5 times
motcuoi = ":)"
namcuoi = motcuoi*5
print(namcuoi)  # should be ':):):):):)'

# [Replace] or [Delete] sub string
favorites = "I like cooking, my family, and my friends"
print(favorites)
#favorites[0] = "U" -> Wrong

    # Same stuff but using sub string
favorites = "I like cooking, my family, and my friends"
from_pos_one = favorites[1:]    # make a string contains all the thing after 'I' in the string
favorites = "U" + from_pos_one  # Overide the string with 'U' at the start and the substring
print(favorites)
    # Same stuff but using .slit()
favorites = "I like cooking, my family, and my friends"
parts = favorites.split("I")    # string containts all the thing after "I"
favorites = "U" + parts[1]

    # Same stuff but using .replace()
favorites = "I like cooking, my family, and my friends"
favorites = favorites.replace(",", ";")
print(favorites)

# Count substring using .count()
hobbies = "I like going to the movies, traveling, and singing"
print(hobbies)
stringcount = hobbies.count('ing') # count amount of string contains 'ing'
print(stringcount)

# round up
num = 1.23456
print('round up to .xx: ' + str(round(num,2)))
print('round up to .xx:', str(round(num,2)))
print('round up to .xx: {:.2f}'.format(num))
print(f'round up to .xx:')
