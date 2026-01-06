# Author: Titles
classics = {'Austen': 'Pride and Prejudice',
            'Shelley': 'Frankenstein',
            'Joyce': 'Ulyssessss'}

print('Dictionary: -------------------------------------------------------')
print(classics, end='\n\n')

# As a dict_items
print('Dictionary as dict_items: -----------------------------------------')
print(classics.items(), end='\n\n')

# As a list
print('Dictionary as a list: ---------------------------------------------')
print(list(classics.items()), end='\n\n')

# Print Authors as a dict_items
print('Author: -----------------------------------------------------------')
print(classics.keys(), end='\n\n')

# Print list of Authors
print('Author as list: ---------------------------------------------------')
print(list(classics.keys()), end='\n\n')

# Print titles as a dict_items
print('Titles as dict_items: ---------------------------------------------')
print(classics.values(), end='\n\n')

# Print titles as a list
print('Titles as list: ---------------------------------------------------')
print(list(classics.values()), end='\n\n')

# Assume The last title is wrong, set it to the right one 'Yeah'
print('Wrong title: ' + classics['Joyce'])
classics['Joyce'] = 'Yeah'
print('Corrected title: ' + classics['Joyce'])

# Add two new books:
# Gulliver's Travels by Swift
# Jane Eyre by Bronte
classics['Swift'] = 'Gulliver\'s Travels'
classics.update({'Bronte': 'Jane Eyre'})
print(classics)

# Deleting the first first book
del classics['Austen']
classics.pop('Joyce')
print(classics)
