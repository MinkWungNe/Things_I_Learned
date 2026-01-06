'''
    - Đọc file 'purchases.txt'
    - Phân tích dữ liệu tìm ra min-max-total, in ra màn hình
    - Ghi dữ liệu min-max-total vào file 'purchases_out.txt' 
'''
from pathlib import Path
cur_dir = Path(__file__).parent

# a. Read file and attract data into a list
def read(fileIn):
    file_path = cur_dir / fileIn
    
    numbers = []
    
    with open(file_path, 'r') as file: # 'r' mean 'read'; fileIn now declared as 'file'
        for line in file:
            line = line.rstrip('\n') # at the end of every lines there is a '\n' to determine when to go to new line
            
            print('Dòng in sau khi tách dòng:', line)
            print('--------------------------')
            
            if line != "":
                so = float(line)
                numbers.append(so)
    return numbers

r = read('purchases.txt')
print(r)

# b. Find min-max-total
def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    
    return minimum, maximum, total

mi,ma,to = calculate(r)
print('Minimum:', mi)
print('Maximum:', ma)
print('Total:', to)

# c. Write

def write(fileOut, mi, ma, to):
    filepath = cur_dir / fileOut
    with open(filepath, 'w') as file:
        file.write('Minimum: ' + str(mi) + '\n')
        file.write('Maximum : ' + str(ma) + '\n')
        file.write('Total: ' + str(to) + '\n')
    
write('purchases_Out.txt', mi, ma, to)