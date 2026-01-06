'''
1. Các trường hợp chuỗi. Viết một hàm in một chuỗi cho trước dưới dạng chữ thường, chữ hoa, chữ cái đầu, chữ hoa, và đổi chỗ các chữ cái đầu. Sau đó, gọi hàm hai lần. 
Thực hiện một lần với chuỗi gồm một từ, và một lần với chuỗi gồm ít nhất hai từ. Cuối cùng, gọi hàm cho mỗi phần tử của danh sách các chuỗi sau bằng vòng lặp for:
summer_vacation = ["Hiking trails", "weekEndcampIng", "enjoying nature", "fishing"].
'''
import random

def print_string(string):
    print('-----------------------------------')
    print('Default:', string)
    print('UpperCased:',str.upper(string))
    print('Titled:', str.title(string))
    
    # Randomly change first char of the word
    words = str.split(string)                   # split string into words
    firstchars = [word[0] for word in words]    # attract firstchar from words    NEW WAY TO USE FOR LOOP
    rest = [word[1:] for word in words]         # attract the rest of the words
    
    random.shuffle(firstchars)                  # shuffles up the firstchar list
    
    for i in range(len(words)):
        words[i] = firstchars[i] + rest[i]      # Put words back with random firstchar
        
    print('First chars shuffled:', ' '.join(words)) # use ' '.join() to joins up items in words list with space ' ' between each word.

print_string('test')
print_string('test new')

summer_vacation = ["Hiking trails", "weekEndcampIng", "enjoying nature", "fishing"]

for word in summer_vacation:
    print_string(word)